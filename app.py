
import streamlit as st
import base64

st.set_page_config(page_title="Cute Chicken Steak 🍗", layout="centered")

# --- Sound ---
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

# --- ADVANCED CSS ---
st.markdown("""
<style>

/* Background glow */
body {
    background: radial-gradient(circle at top, #fff0f5, #ffe4e1);
}

/* Floating hearts */
@keyframes hearts {
    0% {transform: translateY(100vh) scale(1); opacity:1;}
    100% {transform: translateY(-10vh) scale(1.5); opacity:0;}
}

.heart {
    position: fixed;
    bottom: 0;
    font-size: 20px;
    animation: hearts 6s linear infinite;
}

/* Sparkles */
@keyframes sparkle {
    0%,100% {opacity:0;}
    50% {opacity:1;}
}

.sparkle {
    position: fixed;
    font-size: 14px;
    animation: sparkle 2s infinite;
}

/* Floating ingredients */
@keyframes floaty {
    0% {transform: translateY(0px) rotate(0deg);}
    50% {transform: translateY(-20px) rotate(10deg);}
    100% {transform: translateY(0px) rotate(0deg);}
}

.floaty {
    position: fixed;
    animation: floaty 4s ease-in-out infinite;
    font-size: 22px;
}

/* Card with 3D tilt */
.card {
    background: white;
    padding: 25px;
    border-radius: 25px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.15);
    text-align:center;
    transform: perspective(1000px) rotateX(5deg);
    transition: 0.3s;
}

.card:hover {
    transform: perspective(1000px) rotateX(0deg) scale(1.02);
}

/* Ingredients */
.ingredient {
    font-size: 18px;
    animation: floaty 3s ease-in-out infinite;
}

/* Chicken doodle animation */
@keyframes bounceRotate {
    0% {transform: translateY(0) rotate(0deg);}
    50% {transform: translateY(-10px) rotate(10deg);}
    100% {transform: translateY(0) rotate(0deg);}
}

.doodle {
    font-size: 60px;
    animation: bounceRotate 1.5s infinite;
}

/* Button */
button[kind="primary"] {
    background: linear-gradient(45deg, #ff9aa2, #ffc3a0);
    border-radius: 20px;
    border: none;
}

</style>
""", unsafe_allow_html=True)

# --- Floating hearts ---
for i in range(15):
    st.markdown(f"<div class='heart' style='left:{i*7}%'>💖</div>", unsafe_allow_html=True)

# --- Sparkles ---
for i in range(10):
    st.markdown(f"<div class='sparkle' style='left:{i*10}%; top:{i*8}%'>✨</div>", unsafe_allow_html=True)

# --- Floating ingredients ---
floating_items = ["🌶️","🍋","🍯","🥢","🍬","🌰"]
for i, item in enumerate(floating_items):
    st.markdown(
        f"<div class='floaty' style='left:{i*15}%; top:{(i*10)%80}%'>{item}</div>",
        unsafe_allow_html=True
    )

# --- Main Card ---
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
    5️⃣ Enjoy your aesthetic meal 🍽️✨  
    """)

    autoplay_audio("assets/sizzle.mp3")

st.markdown("</div>", unsafe_allow_html=True)



