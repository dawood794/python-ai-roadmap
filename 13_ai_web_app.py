import streamlit as st
from groq import Groq
import urllib.parse

# 1. Futuristic App Layout Configuration
st.set_page_config(
    page_title="Nexus OS Terminal",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Cyberpunk Dark-Theme Layout Style Sheets
st.markdown("""
    <style>
    /* Main Background Elements */
    .main { background-color: #0d1117; color: #c9d1d9; }
    
    /* Custom Navigation Tab Headers */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px 8px 0px 0px;
        padding: 10px 20px;
        color: #8b949e;
        font-weight: bold;
    }
    .stTabs [aria-selected="true"] {
        background-color: #1f6feb !important;
        color: #ffffff !important;
        border-color: #58a6ff !important;
    }
    div[data-testid="stSidebar"] { background-color: #0b0e14; border-right: 1px solid #30363d; }
    
    /* Ensure room at the bottom for the fixed chat bar */
    .block-container {
        padding-bottom: 100px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Persistent Core Memory Allocation (Saves Chat History Across Tabs)
if "engine_messages" not in st.session_state:
    st.session_state.engine_messages = []
if "roadmap_messages" not in st.session_state:
    st.session_state.roadmap_messages = []

# 4. Hardware Verification / Sidebar Controls
with st.sidebar:
    st.title("🔮 Nexus OS")
    st.caption("v2.0.26 // Quantum Core Active")
    st.markdown("---")
    
    st.markdown("### System Diagnostics")
    st.success("📡 Groq Neural Link: CONNECTED")
    st.info("⚡ Model: Llama-3.1-8b-Instant")
    
    st.markdown("---")
    if st.button("🚨 Purge Core Memory (Clear Chats)"):
        st.session_state.engine_messages = []
        st.session_state.roadmap_messages = []
        st.rerun()

# 5. Connect to Groq Secure API Gateway securely via Streamlit Secrets Vault
try:
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
except Exception:
    GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)

# 6. Futuristic Tab Protocol System
tab1, tab2 = st.tabs(["📡 Core Nexus Engine", "🛠️ AI Roadmap Architect"])

# ==========================================
# RENDERING TAB 1 CONTENT
# ==========================================
with tab1:
    st.subheader("📡 Quantum AI Interface")
    st.caption("Direct stream link to the advanced LLM matrix.")
    chat_container_1 = st.container()
    with chat_container_1:
        for msg in st.session_state.engine_messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

# ==========================================
# RENDERING TAB 2 CONTENT
# ==========================================
with tab2:
    st.subheader("🛠️ Neural Roadmap Blueprint Matrix")
    st.caption("Enter a technology or game concept below to synthesize a step-by-step training node map.")
    chat_container_2 = st.container()
    with chat_container_2:
        for msg in st.session_state.roadmap_messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
            if msg["role"] == "assistant" and "image_keyword" in msg:
                if "roblox" in msg["image_keyword"].lower():
                    live_image_url = "https://images.unsplash.com/photo-1542751371-adc38448a05e?w=1080&auto=format&fit=crop"
                elif "learning" in msg["image_keyword"].lower() or "ai" in msg["image_keyword"].lower():
                    live_image_url = "https://images.unsplash.com/photo-1677442136019-21780efad99a?w=1080&auto=format&fit=crop"
                else:
                    live_image_url = "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1080&auto=format&fit=crop"
                st.image(live_image_url, caption=f"Nexus System Visual Interface: {msg['image_keyword'].upper()}")

# ==========================================
# GLOBAL ROOT INPUT BOX (Locked to bottom)
# ==========================================
if user_input := st.chat_input("Send transmission parameter vectors..."):
    st.session_state.engine_messages.append({"role": "user", "content": user_input})
    
    try:
        history = [{
            "role": "system", 
            "content": "You are Nexus OS, a hyper-advanced, elite cyberpunk AI assistant interface. Never output boring Linux server setups or Docker image files. Talk in a premium, ultra-modern developer assistant tone. Use markdown bullet points, code highlights, and clean boxes."
        }]
        for m in st.session_state.engine_messages:
            history.append({"role": m["role"], "content": m["content"]})
        
        completion = client.chat.completions.create(model="llama-3.1-8b-instant", messages=history, temperature=0.5)
        ai_res = completion.choices[0].message.content
        st.session_state.engine_messages.append({"role": "assistant", "content": ai_res})
        st.rerun()
    except Exception as e:
        st.error(f"Execution Error: {e}")