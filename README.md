# 💬 Chatbot

A simple Streamlit chat app powered by OpenAI. It streams answers as they are generated and keeps the conversation history for the current session.

## How to run (step by step)

You need **Python 3.10 or newer** ([download](https://www.python.org/downloads/)).

**1. Download the project**

```bash
git clone https://github.com/amitmohanty022/chatbot-1.git
cd chatbot-1
```

**2. Create a virtual environment and activate it**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

**3. Install the requirements**

```bash
pip install -r requirements.txt
```

**4. Add your OpenAI API key**

- Create a key at https://platform.openai.com/account/api-keys
- Copy `.env.example` to a new file named `.env`
  - Windows: `copy .env.example .env`
  - macOS / Linux: `cp .env.example .env`
- Open `.env` and paste your key after `OPENAI_API_KEY=`

If you skip this step, the app asks for the key on the page instead.

**5. Start the app**

```bash
streamlit run streamlit_app.py
```

Your browser opens at http://localhost:8501. Type a message in the box at the bottom.

## Settings

| Variable in `.env` | Default | What it does |
|---|---|---|
| `OPENAI_API_KEY` | (empty) | Your OpenAI key |
| `OPENAI_MODEL` | `gpt-6-luna` | The OpenAI model used for replies |

## Troubleshooting

| Problem | Fix |
|---|---|
| `streamlit: command not found` | Activate the virtual environment (step 2) first. |
| `model_not_found` error | Your account may not have that model. Set `OPENAI_MODEL` in `.env` to a model listed at https://platform.openai.com/docs/models |
| `insufficient_quota` error | Add billing credit to your OpenAI account. |
