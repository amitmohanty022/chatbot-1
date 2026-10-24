# 💬 OpenAI Chatbot (Streamlit)

A simple Streamlit chat app that streams answers from the OpenAI API and keeps the conversation history for the session.

## 🔗 Live demo

Not hosted yet. Deploy it for free on Streamlit Community Cloud: click the badge (or go to https://share.streamlit.io → **Create app**) and use repository `amitmohanty022/chatbot-1`, branch `main`, main file `streamlit_app.py`.

[![Deploy on Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/deploy?repository=amitmohanty022/chatbot-1&branch=main&mainModule=streamlit_app.py)

No secrets are needed: users type their own [OpenAI API key](https://platform.openai.com/api-keys) into the app.

## Model

Defaults to `gpt-6-luna`. The original `gpt-3.5-turbo` was shut down by OpenAI on 23 October 2026 ([OpenAI deprecations](https://developers.openai.com/api/docs/deprecations/)). Set the `OPENAI_MODEL` environment variable to use a different model.

## Run locally

```bash
git clone https://github.com/amitmohanty022/chatbot-1.git
cd chatbot-1
pip install -r requirements.txt
streamlit run streamlit_app.py
```

You can also open the repo in GitHub Codespaces; the included dev container installs everything and starts the app.

## Author

**Amit Kumar Mohanty** · [GitHub](https://github.com/amitmohanty022) · [LinkedIn](https://www.linkedin.com/in/amitkrmohanty/)

Based on the [Streamlit chatbot template](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps).
