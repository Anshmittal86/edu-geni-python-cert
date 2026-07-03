# UV - Python Package & Project Manager

UV is an extremely fast Python package installer and project manager, written in Rust. It is a drop-in replacement for `pip`, `venv`, `pyenv`, and more.

---

## 1. Installation

```bash
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Using pip
pip install uv
```

After installation, verify it:

```bash
uv --version
```

---

## 2. Initialize a New Project

```bash
uv init my-project
cd my-project
```

This creates a project structure with:

- `pyproject.toml` — project metadata and dependencies
- `hello.py` — sample Python file
- `.python-version` — pinned Python version

To initialize in the current directory:

```bash
uv init
```

---

## 3. Creating a Virtual Environment

```bash
# Create a virtual environment (creates .venv folder)
uv venv

# Create with a specific Python version
uv venv --python 3.12
```

---

## 4. Activating the Virtual Environment

```bash
# Windows (PowerShell)
.venv\Scripts\activate

# Windows (CMD)
.venv\Scripts\activate.bat

# macOS / Linux
source .venv/bin/activate
```

---

## 5. Installing Packages

```bash
# Add a package to the project (updates pyproject.toml + installs)
uv add requests

# Add multiple packages
uv add flask fastapi uvicorn

# Add a dev dependency
uv add --dev pytest

# Install all dependencies from pyproject.toml
uv sync

# Remove a package
uv remove requests
```

---

## 6. Running Python Files

```bash
# Run a Python file using uv (automatically uses the project's venv)
uv run hello.py

# Run with arguments
uv run app.py --port 8000

# Run a module
uv run -m pytest
```

> `uv run` automatically creates a virtual environment and installs dependencies if needed — no manual activation required.

---

## 7. Python Version Management

```bash
# List available Python versions
uv python list

# Install a specific Python version
uv python install 3.12

# Install multiple versions
uv python install 3.10 3.11 3.12

# Pin a Python version for the project
uv python pin 3.12

# Use a specific version when creating a venv
uv venv --python 3.11
```

---

## 8. Deactivating the Virtual Environment

```bash
deactivate
```

This works the same way regardless of the OS — just run `deactivate` in the terminal where the venv is active.

---

## Quick Reference

| Task                     | Command                    |
| ------------------------ | -------------------------- |
| Install uv               | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| Init project             | `uv init`                  |
| Create venv              | `uv venv`                  |
| Activate venv            | `source .venv/bin/activate` |
| Add package              | `uv add <package>`         |
| Remove package           | `uv remove <package>`      |
| Install all dependencies | `uv sync`                  |
| Run a file               | `uv run <file.py>`         |
| Install Python version   | `uv python install 3.12`   |
| Pin Python version       | `uv python pin 3.12`       |
| Deactivate venv          | `deactivate`               |
