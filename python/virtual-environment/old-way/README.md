# Virtual Environment - Old Way (pip + venv)

This is the traditional Python virtual environment workflow using the built-in `venv` module and `pip` package manager.

## Setup Steps

### 1. Create a Virtual Environment

```bash
python -m venv .venv
```

### 2. Activate the Virtual Environment

**Windows (CMD):**
```bash
.venv\Scripts\activate
```

**Windows (PowerShell):**
```bash
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
source .venv/bin/activate
```

### 3. Install Packages

```bash
pip install rich python-dotenv openai tiktoken requests
```

### 4. Freeze Dependencies

```bash
pip freeze > requirements.txt
```

This saves **all** installed packages (including transitive dependencies) with pinned versions into `requirements.txt`.

### 5. Install from requirements.txt

When setting up the project on a new machine:

```bash
pip install -r requirements.txt
```

### 6. Deactivate the Virtual Environment

```bash
deactivate
```

## File Structure

```
old-way/
├── .venv/              # Virtual environment (not committed to git)
├── main.py             # Entry point
├── requirements.txt    # Pinned dependencies (pip freeze output)
└── README.md
```

## Limitations of This Approach

- `pip freeze` dumps **all** packages (direct + transitive), making it hard to tell which ones you actually installed
- No built-in lock file mechanism — dependency resolution can differ across machines
- No separation between dev and production dependencies
- Slower package installation compared to modern tools like `uv`

> See the `new-way/` folder for the modern approach using `uv`.
