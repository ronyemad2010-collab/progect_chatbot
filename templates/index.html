import streamlit as st

st.set_page_config(
    page_title="Nexora Chat",
    page_icon="💬",
    layout="centered"
)

st.markdown("""
<style>

.stApp{
    background: linear-gradient(135deg,#4a90e2,#6a11cb);
}

.chat-header{
    background:#4a90e2;
    color:white;
    padding:15px;
    border-radius:15px;
    text-align:center;
    font-size:24px;
    font-weight:bold;
    margin-bottom:20px;
}

.user-msg{
    background:#4a90e2;
    color:white;
    padding:10px;
    border-radius:15px 15px 0px 15px;
    margin:5px;
}

.bot-msg{
    background:#eeeeee;
    color:black;
    padding:10px;
    border-radius:15px 15px 15px 0px;
    margin:5px;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="chat-header">💬 Nexora Support</div>',
    unsafe_allow_html=True
)

if "messages" not in st.session_state:
    st.session_state.messages = []

def chatbot_response(msg):

    msg = msg.lower()

    if "مرحبا" in msg:
        return "أهلاً بيك! إزاي أقدر أساعدك؟"

    elif "hello" in msg:
        return "Hi How can I help you"

    return "Nexora AI Response"

for message in st.session_state.messages:

    if message["role"] == "user":
        st.markdown(
            f'<div class="user-msg">{message["content"]}</div>',
            unsafe_allow_html=True
        )

    else:
        st.markdown(
            f'<div class="bot-msg">{message["content"]}</div>',
            unsafe_allow_html=True
        )

user_input = st.chat_input("اكتب رسالتك...")

if user_input:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":user_input
        }
    )

    reply = chatbot_response(user_input)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":reply
        }
    )

    st.rerun()
