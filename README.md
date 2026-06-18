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
- [Prompting Techniques](#prompting-techniques)
- [References](#references)
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

### Step 4: Docker Setup (Optional - for RAG module)

If you want to use the RAG (Retrieval-Augmented Generation) features, start the Docker containers:

```bash
cd rag
docker compose up -d
```

This will start the necessary services for the RAG module. To stop the services:

```bash
docker compose down
```

---

## 📁 Project Structure

```
genai-python-cert/
├── main.py                              # Main entry point / starter template
├── hello-openai.py                      # Example: Using OpenAI's GPT model
├── hello-gemini.py                      # Example: Using Google's Gemini model
├── terminologies.md                     # Key AI/ML concepts explained
├── pyproject.toml                       # Project dependencies configuration
├── .env.example                         # Example environment variables template
├── .env                                 # Environment variables (create this - see setup below)
├── README.md                            # This file
├── agents/                              # AI agents implementations
│   ├── weather-agent.py                 # Weather agent example
│   ├── weather-agent-pydantic.py        # Weather agent with Pydantic
│   ├── audio-audio-weather-agent.py     # Audio-based weather agent
│   ├── cli-based-coding-agnet.py        # CLI-based coding agent
│   └── web_search.py                    # Web search agent
├── openai-method/                       # OpenAI-specific methods
│   ├── function-calling.py              # Function calling examples
│   └── open-sdk-tool-calling.py         # OpenAI SDK tool calling
├── pydantic/                            # Pydantic data validation examples
│   ├── 01_basics.py                     # Pydantic basics
│   ├── 02_default_value.py              # Default values in Pydantic
│   ├── 03_typing_with_pydantic.py       # Type hints with Pydantic
│   └── 04_field_validation.py           # Field validation examples
├── rag/                                 # Retrieval-Augmented Generation
│   ├── docker-compose.yml               # Docker Compose for RAG services
│   ├── pdf-loader.py                    # PDF loading and processing
│   └── retrieve.py                      # Retrieval examples
├── responses-api/                       # Responses API examples
│   └── hello-openai.py                  # OpenAI API response example
├── streaming/                           # Streaming responses
│   └── stream-openai.py                 # OpenAI streaming example
└── prompts/                             # Prompting techniques and strategies
    ├── zero-shot-prompting.py           # Zero-shot prompting examples
    ├── one-shot-prompting.py            # One-shot prompting examples
    ├── few-shot-prompting.py            # Few-shot prompting examples
    ├── cot-prompting.py                 # Chain-of-Thought prompting examples
    ├── auto-cot-prompting.py            # Automatic Chain-of-Thought examples
    └── structured-output-prompting.py   # Structured output prompting examples
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

## � Prompting Techniques

This project includes examples of various prompting strategies in the `prompts/` folder:

### Available Techniques:

1. **Zero-Shot Prompting** - Directly asking the model without examples
   - File: `zero-shot-prompting.py`
   - Use when: You want direct answers without prior examples

2. **One-Shot Prompting** - Providing a single example before asking
   - File: `one-shot-prompting.py`
   - Use when: One example helps clarify the expected format

3. **Few-Shot Prompting** - Providing multiple examples for better context
   - File: `few-shot-prompting.py`
   - Use when: Multiple examples improve model understanding

4. **Chain-of-Thought (CoT) Prompting** - Encouraging step-by-step reasoning
   - File: `cot-prompting.py`
   - Use when: Complex problem-solving requires logical steps

5. **Automatic Chain-of-Thought** - Enhanced CoT with automated reasoning
   - File: `auto-cot-prompting.py`
   - Use when: Maximizing model reasoning capability

6. **Structured Output Prompting** - Getting responses in specific formats
   - File: `structured-output-prompting.py`
   - Use when: You need consistent, parsable output (JSON, CSV, etc.)

---

## 📚 References

### Research Papers

- **[Attention Is All You Need](https://proceedings.neurips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf)** - The foundational paper introducing the Transformer architecture used in modern LLMs (NeurIPS 2017)

### Visualization & Exploration Tools

- **[TensorFlow Projector](https://projector.tensorflow.org/)** - Visualize high-dimensional vectors and embeddings in 3D space to understand how AI models represent text

### API Compatibility

- **[Google Gemini OpenAI Compatibility](https://ai.google.dev/gemini-api/docs/openai)** - Use Google's Gemini API with OpenAI-compatible code

---

## �🐛 Troubleshooting

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
