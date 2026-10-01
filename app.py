import requests
import streamlit as st

# ---------- Page config ----------
st.set_page_config(page_title="AI Chat", page_icon="✨", layout="centered")

# ---------- Custom CSS ----------
st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at top left, #1e1b4b 0%, #0f172a 45%, #020617 100%);
    }
    .main-title {
        text-align: center;
        font-size: 2.4rem;
        font-weight: 800;
        background: linear-gradient(90deg, #818cf8, #c084fc, #f472b6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0;
    }
    .subtitle {
        text-align: center;
        color: #94a3b8;
        margin-bottom: 1.5rem;
    }
    [data-testid="stChatMessage"] {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 0.9rem 1rem;
        backdrop-filter: blur(8px);
    }
    [data-testid="stSidebar"] {
        background: rgba(15, 23, 42, 0.85);
        border-right: 1px solid rgba(255, 255, 255, 0.08);
    }
    .stButton > button {
        border-radius: 12px;
        border: none;
        background: linear-gradient(90deg, #6366f1, #a855f7);
        color: white;
        font-weight: 600;
        width: 100%;
    }
    .stButton > button:hover { filter: brightness(1.15); color: white; }
    #MainMenu, footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Sidebar settings ----------
with st.sidebar:
    st.header("⚙️ Settings")
    api_url = st.text_input(
        "API URL", "ADD_NGROK_LINK/generate"  # add your API URL (ngrok link)
    )
    # Better: put this in .streamlit/secrets.toml as API_TOKEN
    try:
        default_token = st.secrets["API_TOKEN"]
    except Exception:
        default_token = "secret123"
    token = st.text_input("API Token", default_token, type="password")
    max_length = st.slider("Max length", 100, 4000, 2000, step=100)
    st.divider()
    if st.button("🗑️ Clear chat"):
        st.session_state.messages = []
        st.rerun()

# ---------- Header ----------
st.markdown('<p class="main-title">✨ AI Chat</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Ask me anything</p>', unsafe_allow_html=True)

# ---------- Chat state ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar="🧑" if msg["role"] == "user" else "🤖"):
        st.markdown(msg["content"])


# ---------- API call ----------
def ask_api(prompt: str) -> str:
    try:
        res = requests.post(
            api_url,
            headers={
                "Authorization": f"Bearer {token}",
                "ngrok-skip-browser-warning": "true",
            },
            json={"prompt": prompt, "max_length": max_length},
            timeout=120,
        )
        res.raise_for_status()
        return res.json()["response"]
    except requests.exceptions.Timeout:
        return "⚠️ The request timed out. Is your server running?"
    except requests.exceptions.ConnectionError:
        return "⚠️ Could not connect. Check the URL / ngrok tunnel."
    except requests.exceptions.HTTPError as e:
        return f"⚠️ Server error: {e}"
    except (KeyError, ValueError):
        return "⚠️ Unexpected response format from the API."


# ---------- Input ----------
if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="🧑"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Thinking..."):
            answer = ask_api(prompt)
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
