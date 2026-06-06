# GenAI Python Course 🤖

A beginner-friendly course project to learn and practice **Generative AI** integration using Python. This course covers working with OpenAI's GPT and Google's Gemini models through simple, practical examples.

---

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Project Setup](#project-setup)
- [Project Structure](#project-structure)
- [Running the Examples](#running-the-examples)
- [API Keys Setup](#api-keys-setup)
- [Key Concepts](#key-concepts)
- [Troubleshooting](#troubleshooting)

---

## 📋 Prerequisites

Before you start, make sure you have the following installed on your computer:

- **Python 3.14+** - [Download here](https://www.python.org/downloads/)
- **Git** - [Download here](https://git-scm.com/download/win) (Windows users)
- **UV Package Manager** - Install via: `pip install uv`
- **Text Editor or IDE** - [VS Code](https://code.visualstudio.com/) recommended

---

## 🚀 Project Setup

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd edu-geni-python-cert
```

### Step 2: Create Virtual Environment

```bash
uv venv
```

Activate the virtual environment:

- **Windows**: `.venv\Scripts\activate`
- **macOS/Linux**: `source .venv/bin/activate`

### Step 3: Install Dependencies

```bash
uv sync
```

This will install:

- `openai` - For OpenAI API integration
- `python-dotenv` - For managing environment variables

---

## 📁 Project Structure

```
genai-python/
├── main.py                 # Main entry point / starter template
├── hello-openai.py         # Example: Using OpenAI's GPT model
├── hello-gemini.py         # Example: Using Google's Gemini model
├── terminologies.md        # Key AI/ML concepts explained
├── pyproject.toml          # Project dependencies configuration
├── .env.example            # Example environment variables template
├── .env                    # Environment variables (create this - see setup below)
└── README.md              # This file
```

---

## ▶️ Running the Examples

### 1. Running the Main File

```bash
uv run main.py
```

This will print: `Hello from genai-python!`

### 2. Using OpenAI's GPT Model

```bash
uv run hello-openai.py
```

**Output:** An AI response to "Hello, how are you?"

**Requirements:**

- You need an OpenAI API key
- Set it in a `.env` file (see [API Keys Setup](#api-keys-setup))

### 3. Using Google's Gemini Model

```bash
uv run hello-gemini.py
```

**Output:** An AI response from Google's Gemini model

**Requirements:**

- You need a Google API key
- The script is configured to use Gemini via OpenAI's compatible API

---

## 🔑 API Keys Setup

### For OpenAI (GPT Model)

1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Navigate to **API Keys** section
4. Create a new API key
5. Copy the key

### For Google Gemini Model

1. Go to [Google AI Studio](https://aistudio.google.com/apikey)
2. Create a new API key
3. Copy the key

### Create `.env` File

**Option 1: Copy from `.env.example` (Recommended)**

```bash
# Windows
copy .env.example .env

# macOS/Linux
cp .env.example .env
```

**Option 2: Create `.env` manually**

```bash
# Windows
type nul > .env

# macOS/Linux
touch .env
```

Add your API keys to `.env`:

```
OPENAI_API_KEY=your_openai_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
```

**⚠️ Security Warning:** Never commit `.env` to version control. It's already in `.gitignore` if properly configured.

---

## 📚 Key Concepts

We've compiled important AI/ML terminologies in `terminologies.md`. Key topics include:

- **Tokens** - Small pieces of text processed by AI models
- **Tokenization** - Breaking text into tokens
- **Vectors** - Mathematical representations of text meaning
- **Transformer** - The AI architecture powering modern LLMs
- **Attention Mechanism** - How models focus on important words
- **Temperature** - Controls creativity vs. predictability
- **Top-K & Top-P** - Sampling techniques for text generation

📖 **Read [terminologies.md](terminologies.md) for detailed explanations!**

---

## 🐛 Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'openai'`

**Solution:**

```bash
uv sync
```

### Issue: `API Key not found` or `Authentication failed`

**Solution:**

1. Check that `.env` file exists in the project root
2. Verify API keys are correctly set in `.env`
3. Ensure no extra spaces around the API key value

### Issue: `Command 'uv' not found`

**Solution:**

```bash
pip install uv
```

### Issue: Virtual environment not activated

**Solution:**

- **Windows**: Run `.venv\Scripts\activate`
- **macOS/Linux**: Run `source .venv/bin/activate`

You should see `(.venv)` at the start of your terminal line

### Issue: Python version too old

**Solution:**

```bash
python --version  # Check your version
# If it's below 3.14, install Python 3.14+ from python.org
```

---

## 📖 Course Resources

- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [Google Gemini API Docs](https://ai.google.dev/docs)
- [Python Official Docs](https://docs.python.org/3/)
- [UV Package Manager Docs](https://docs.astral.sh/uv/)

---

## 💡 Next Steps

1. ✅ Run both AI examples successfully
2. ✅ Modify the prompts in `hello-openai.py` and `hello-gemini.py`
3. ✅ Create your own script using the API
4. ✅ Experiment with different models and parameters
5. ✅ Study the concepts in `terminologies.md`

---

## 🤝 Need Help?

- Check the [Troubleshooting](#troubleshooting) section
- Review the example scripts
- Check API provider documentation
- Ask your instructor

**Happy Learning! 🚀**
