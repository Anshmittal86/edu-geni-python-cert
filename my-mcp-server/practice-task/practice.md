# Building MCP Tools — Student Practice Set

**Goal:** by the end, you can write an MCP server, expose tools from it, and verify every tool works in MCP Inspector _before_ wiring it into any client.

**Stack:** Python (`mcp` package) or TypeScript (`@modelcontextprotocol/sdk`). Pick one and stay with it.

---

## Setup (do once)

**Python**

```bash
# python
mkdir mcp-practice && cd mcp-practice
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install "mcp[cli]"
```

```bash
# uv
mkdir mcp-practice && cd mcp-practice
uv venv   # Windows: .venv\Scripts\activate
uv add "mcp[cli]"
```

**TypeScript**

```bash
mkdir mcp-practice && cd mcp-practice
npm init -y
npm install @modelcontextprotocol/sdk zod
```

**Launch the Inspector** (Node 18+ required; no install needed):

```bash
# python
npx @modelcontextprotocol/inspector python server.py

# uv
npx @modelcontextprotocol/inspector uv run server.py

# or
npx @modelcontextprotocol/inspector node build/server.js
```

It opens a browser UI. Workflow every time: **Connect → Tools tab → List Tools → pick a tool → fill args → Run.** Watch the notifications/history pane for the raw JSON-RPC — that pane is where you actually learn the protocol.

> Rule for the whole worksheet: **never print to stdout** in a stdio server. `print()` / `console.log()` corrupts the JSON-RPC stream. Log to stderr instead.

---

## Exercise 1 — Hello, tool

Write a server named `practice` exposing one tool:

- `add(a: int, b: int) -> int`

**Starter (Python):**

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("practice")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers and return the sum."""
    return a + b

if __name__ == "__main__":
    mcp.run()
```

**Inspector checks**

1. Does `add` appear under List Tools?
2. Run it with `a=12`, `b=30`. Expect `42`.
3. Read the tool's JSON schema in the Inspector. Where did the parameter types come from? Where did the description come from?

**Now break it deliberately:** delete the docstring and the type hints, reconnect, and look at the schema again. Write down what changed. This is the single most important lesson in the whole set — a model can only call a tool as well as its schema and description describe it.

---

## Exercise 2 — Types beyond int

Add these three tools:

- `greet(name: str, formal: bool = False) -> str`
- `stats(numbers: list[float]) -> dict` — returns `{"count", "mean", "min", "max"}`
- `slugify(text: str, separator: str = "-") -> str`

**Inspector checks**

- Pass an empty list to `stats`. What happens? Fix it so it returns a clean error rather than a stack trace.
- Try passing `"5"` (a string) where a float is expected. Note whether validation happens before your function runs.

---

## Exercise 3 — Errors are a feature

Add `divide(a: float, b: float) -> float`.

Requirements:

- Dividing by zero must return a **tool error with a readable message**, not crash the server.
- After triggering the error, the Inspector must still be connected and other tools must still work.

In Python, raising a normal exception inside a `@mcp.tool()` function is reported back as a tool error — confirm this in the Inspector's response pane, and note the difference between an error _result_ and a transport-level failure.

---

## Exercise 4 — Touching the outside world

Add `read_notes(filename: str) -> str` that reads a `.txt` file from a fixed `notes/` directory.

Security requirements (test each one in the Inspector):

- `../../etc/passwd` → rejected
- `/etc/passwd` → rejected
- a name with no `.txt` extension → rejected
- a file that doesn't exist → friendly error

Then add `write_note(filename: str, content: str) -> str`. Discuss: why is a write tool categorically riskier than a read tool, and what should the description say so a client knows to ask permission?

---

## Exercise 5 — Async and slow work

Add `fetch_title(url: str) -> str` that fetches a page and returns its `<title>`.

- Make the function `async`.
- Set a timeout (5s) and handle it.
- Handle non-200 responses.

**Inspector check:** call it with a valid URL, a 404 URL, and a garbage string like `not-a-url`. All three should produce sensible output, none should hang forever.

---

## Exercise 6 — Resources and prompts

Tools aren't the only primitive. Add:

- A **resource** at `notes://list` returning the filenames in `notes/`.
- A **prompt** called `summarize_note` that takes a filename and returns a message template.

**Inspector check:** use the Resources and Prompts tabs. Write one sentence explaining when you'd model something as a resource instead of a tool. (Hint: who initiates it, and does it have side effects?)

---

## Exercise 7 — A real mini-server (capstone)

Build a **task tracker** server backed by a JSON file:

| Tool            | Signature                                                                 |
| --------------- | ------------------------------------------------------------------------- |
| `add_task`      | `(title: str, priority: str = "medium", due: str \| None = None) -> dict` |
| `list_tasks`    | `(status: str = "open", priority: str \| None = None) -> list[dict]`      |
| `complete_task` | `(task_id: str) -> dict`                                                  |
| `delete_task`   | `(task_id: str) -> dict`                                                  |
| `search_tasks`  | `(query: str) -> list[dict]`                                              |

Requirements:

- `priority` restricted to `low|medium|high` **in the schema**, not just in your code (use an Enum / `Literal` / zod enum). Verify in the Inspector that an invalid value is rejected before your function runs.
- IDs stable across restarts.
- Every tool has a description written for a _model_, not a human: state what it does, when to use it, and what it returns.
- Deleting a nonexistent ID errors cleanly.

**Acceptance test — run entirely in the Inspector, in order:**

1. Add three tasks with different priorities.
2. `list_tasks` with no filters → 3 results.
3. `list_tasks(priority="high")` → only the high one.
4. Complete one; `list_tasks(status="open")` → 2 results.
5. `search_tasks` with a partial word → correct match.
6. Restart the server, reconnect, `list_tasks` → data still there.
7. `complete_task("does-not-exist")` → clean error, server still alive.

---

## Exercise 8 — Ship it

Only after Exercise 7 passes every acceptance test:

1. Register the server with a client. For Claude Desktop that's `claude_desktop_config.json` — use **absolute paths** for the command and the script, and fully quit and relaunch the app (closing the window is not enough).
2. Ask the client, in plain language, to do something requiring two tools in sequence ("add a high priority task to fix the printer, then show me everything open").
3. If the model picks the wrong tool or the wrong arguments, **do not fix the model — fix the descriptions.** Iterate until it gets it right first try.

---

## Debugging cheat sheet

| Symptom                               | Usual cause                                                                               |
| ------------------------------------- | ----------------------------------------------------------------------------------------- |
| Inspector won't connect               | Server crashed on startup — run the command directly in a terminal and read the traceback |
| Connects, zero tools listed           | Decorator missing, or tools registered after `run()`                                      |
| Garbled / parse errors                | Something printed to stdout                                                               |
| Tool listed but always errors         | Schema mismatch — compare the Inspector's arg names to your signature                     |
| Works in Inspector, not in the client | Relative path, or missing runtime on the client's PATH; restart the client                |
