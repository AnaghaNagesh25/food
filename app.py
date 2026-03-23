```python
import streamlit as st
import base64

st.set_page_config(page_title="Cute Chicken Steak 🍗", layout="centered")

# --- Load optional sound ---
def autoplay_audio(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            md = f"""
            <audio autoplay loop>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
            st.markdown(md, unsafe_allow_html=True)
    except:
        pass

# --- Title ---
st.markdown(
    "<h1 style='text-align:center; color:#ff6b6b;'>🍗 Cute Chicken Steak 💖</h1>",
    unsafe_allow_html=True
)

# --- CSS Styling ---
st.markdown("""
<style>
@keyframes float {
    0% {transform: translateY(0);}
    50% {transform: translateY(-10px);}
    100% {transform: translateY(0);}
}

@keyframes hearts {
    0% {transform: translateY(100vh); opacity:1;}
    100% {transform: translateY(-10vh); opacity:0;}
}

.heart {
    position: fixed;
    bottom: 0;
    font-size: 20px;
    animation: hearts 6s linear infinite;
}

.card {
    background: white;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    text-align:center;
}

.ingredient {
    animation: float 3s ease-in-out infinite;
    font-size: 18px;
}

.doodle {
    font-size: 50px;
    animation: wiggle 1s infinite;
}

@keyframes wiggle {
    0%,100% { transform: rotate(0deg); }
    50% { transform: rotate(5deg); }
}
</style>
""", unsafe_allow_html=True)

# --- Floating hearts ---
for i in range(10):
    st.markdown(f"<div class='heart' style='left:{i*10}%'>💖</div>", unsafe_allow_html=True)

# --- Main card ---
st.markdown("<div class='card'>", unsafe_allow_html=True)

st.markdown("<div class='doodle'>🐔🔥🍳</div>", unsafe_allow_html=True)

st.subheader("✨ Ingredients")
ingredients = [
    "🌶️ Chilli Powder",
    "🧂 Salt",
    "🍋 Lemon",
    "🌰 Tamarind",
    "🍯 Honey",
    "🍬 Brown Sugar",
    "🥢 Soy Sauce"
]

for item in ingredients:
    st.markdown(f"<div class='ingredient'>{item}</div>", unsafe_allow_html=True)

# --- Button ---
if st.button("Cook Now 💕"):
    st.success("Cooking magic started ✨")

    st.markdown("""
    ### 👩‍🍳 Steps
    1️⃣ Mix all ingredients into a marinade 💫  
    2️⃣ Coat chicken steak nicely 🐔💖  
    3️⃣ Rest for 20 mins ⏳  
    4️⃣ Pan cook till golden & juicy 🔥  
    5️⃣ Enjoy your meal 🍽️✨  
    """)

    autoplay_audio("assets/sizzle.mp3")

st.markdown("</div>", unsafe_allow_html=True)
```
