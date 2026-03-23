
import streamlit as st
import base64

st.set_page_config(page_title="Ancient Chicken Grimoire 🍗📖", layout="centered")

# --- SOUND ---
def autoplay_audio(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            st.markdown(f"""
            <audio autoplay loop>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """, unsafe_allow_html=True)
    except:
        pass

# --- STYLING ---
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600&family=Great+Vibes&display=swap" rel="stylesheet">

<style>

/* BACKGROUND */
body {
    background: radial-gradient(circle at top, #2b1d0e, #120a04);
}

/* BOOK */
.book {
    width: 380px;
    height: 520px;
    margin: auto;
    perspective: 2000px;
}

.book-inner {
    width: 100%;
    height: 100%;
    transform-style: preserve-3d;
    animation: openBook 1.8s ease forwards;
}

@keyframes openBook {
    0% { transform: rotateY(90deg); }
    100% { transform: rotateY(0deg); }
}

/* PAGE */
.page {
    position: relative;
    width: 100%;
    height: 100%;
    background: linear-gradient(135deg, #f5e6c8, #e8d3a1);
    border-radius: 12px;
    padding: 25px;
    color: #3b2b1a;
    box-shadow:
        inset 0 0 40px rgba(0,0,0,0.5),
        0 25px 50px rgba(0,0,0,0.7);
    border: 3px solid #5a3e1b;
}

/* PAPER TEXTURE */
.page::before {
    content: "";
    position: absolute;
    inset: 0;
    background: url("https://www.transparenttextures.com/patterns/paper.png");
    opacity: 0.25;
}

/* BOOK FOLD */
.page::after {
    content: "";
    position: absolute;
    left: 50%;
    top: 0;
    width: 2px;
    height: 100%;
    background: rgba(0,0,0,0.25);
}

/* TITLE */
.title {
    font-family: 'Cinzel', serif;
    font-size: 28px;
    text-align: center;
    color: #5a3e1b;
    margin-bottom: 10px;
}

/* DOODLE */
.doodle {
    text-align:center;
    font-size: 45px;
    margin-bottom: 10px;
    animation: float 2s infinite;
}

/* FLOAT */
@keyframes float {
    0%,100% { transform: translateY(0); }
    50% { transform: translateY(-6px); }
}

/* INGREDIENTS */
.ingredient {
    font-family: 'Great Vibes', cursive;
    font-size: 20px;
    margin: 6px 0;
}

/* SPARKLES */
.sparkle {
    position: fixed;
    font-size: 14px;
    animation: sparkle 2s infinite;
}

@keyframes sparkle {
    0%,100% {opacity:0;}
    50% {opacity:1;}
}

/* HEARTS */
.heart {
    position: fixed;
    bottom: 0;
    font-size: 18px;
    animation: hearts 6s linear infinite;
}

@keyframes hearts {
    0% {transform: translateY(100vh);}
    100% {transform: translateY(-10vh); opacity:0;}
}

/* COOKING */
.cooking {
    font-size: 60px;
    text-align:center;
    animation: cook 1s infinite alternate;
}

@keyframes cook {
    from { transform: rotate(-5deg); }
    to { transform: rotate(5deg); }
}

/* BUTTON */
button[kind="primary"] {
    background: linear-gradient(45deg, #8b5e3c, #c69c6d);
    color: white;
    border-radius: 20px;
    border: none;
}

</style>
""", unsafe_allow_html=True)

# --- EFFECTS ---
for i in range(10):
    st.markdown(f"<div class='sparkle' style='left:{i*10}%; top:{i*7}%'>✨</div>", unsafe_allow_html=True)

for i in range(10):
    st.markdown(f"<div class='heart' style='left:{i*10}%'>💖</div>", unsafe_allow_html=True)

# --- BOOK UI (FIXED HTML) ---
st.markdown("""
<div class="book">
  <div class="book-inner">
    <div class="page">

      <div class="title">Ancient Chicken Elixir 🍗📜</div>

      <div class="doodle">🐔✨🍳</div>

      <h4>Ingredients</h4>

      <div class="ingredient">🌶️ Chilli Powder</div>
      <div class="ingredient">🧂 Salt</div>
      <div class="ingredient">🍋 Lemon</div>
      <div class="ingredient">🌰 Tamarind</div>
      <div class="ingredient">🍯 Honey</div>
      <div class="ingredient">🍬 Brown Sugar</div>
      <div class="ingredient">🥢 Soy Sauce</div>

    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# --- BUTTON ---
if st.button("Unleash Recipe Magic 💫"):
    st.success("The grimoire awakens... 🔥")

    st.markdown("<div class='cooking'>🍳🔥🐔</div>", unsafe_allow_html=True)

    st.markdown("""
    ### 👩‍🍳 Ritual Steps
    1️⃣ Blend sacred spices 💫  
    2️⃣ Coat the chicken 🐔  
    3️⃣ Rest ⏳  
    4️⃣ Cook over flame 🔥  
    5️⃣ Feast 🍽️✨  
    """)

    autoplay_audio("assets/sizzle.mp3")







