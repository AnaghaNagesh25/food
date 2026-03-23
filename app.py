```python id="insaneapp123"
import streamlit as st
import base64

st.set_page_config(page_title="Magical Chicken Steak 🍗📖", layout="centered")

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

# --- CSS + FONTS ---
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=Poppins&display=swap" rel="stylesheet">

<style>

/* Background */
body {
    background: radial-gradient(circle at top, #fff0f5, #ffe4e1);
}

/* BOOK */
.book {
    width: 360px;
    height: 480px;
    margin: auto;
    perspective: 2000px;
}

.book-inner {
    width: 100%;
    height: 100%;
    transform-style: preserve-3d;
    animation: openBook 2s ease forwards;
}

@keyframes openBook {
    0% { transform: rotateY(90deg); }
    100% { transform: rotateY(0deg); }
}

/* PAGE */
.page {
    position: absolute;
    width: 100%;
    height: 100%;
    background: #fffdf7;
    border-radius: 15px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.25);
    padding: 20px;
}

/* Title */
.title {
    font-family: 'Great Vibes', cursive;
    font-size: 38px;
    color: #d6336c;
    text-align: center;
}

/* Ingredients */
.ingredient {
    font-family: 'Poppins', sans-serif;
    font-size: 16px;
    margin: 4px;
    animation: float 3s infinite;
}

/* Floating animation */
@keyframes float {
    0%,100% { transform: translateY(0); }
    50% { transform: translateY(-8px); }
}

/* Doodle */
.doodle {
    font-size: 55px;
    text-align:center;
    animation: bounce 1.5s infinite;
}

@keyframes bounce {
    0%,100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}

/* PAGE FLIP */
.flip {
    animation: flipPage 1s forwards;
}

@keyframes flipPage {
    from { transform: rotateY(0); }
    to { transform: rotateY(-180deg); }
}

/* HEARTS */
.heart {
    position: fixed;
    bottom: 0;
    animation: hearts 6s linear infinite;
    font-size: 20px;
}

@keyframes hearts {
    0% {transform: translateY(100vh); opacity:1;}
    100% {transform: translateY(-10vh); opacity:0;}
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

/* FLOATING INGREDIENTS */
.floaty {
    position: fixed;
    font-size: 22px;
    animation: floaty 4s infinite;
}

@keyframes floaty {
    0% {transform: translateY(0px) rotate(0deg);}
    50% {transform: translateY(-20px) rotate(10deg);}
    100% {transform: translateY(0px) rotate(0deg);}
}

/* COOKING SCENE */
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
    background: linear-gradient(45deg, #ff9aa2, #ffc3a0);
    border-radius: 20px;
    border: none;
}

</style>
""", unsafe_allow_html=True)

# --- FLOATING EFFECTS ---
for i in range(15):
    st.markdown(f"<div class='heart' style='left:{i*6}%'>💖</div>", unsafe_allow_html=True)

for i in range(12):
    st.markdown(f"<div class='sparkle' style='left:{i*8}%; top:{i*7}%'>✨</div>", unsafe_allow_html=True)

floating_items = ["🌶️","🍋","🍯","🥢","🍬","🌰"]
for i, item in enumerate(floating_items):
    st.markdown(
        f"<div class='floaty' style='left:{i*15}%; top:{(i*10)%80}%'>{item}</div>",
        unsafe_allow_html=True
    )

# --- BOOK UI ---
st.markdown("""
<div class="book">
  <div class="book-inner">
    <div class="page">

      <div class="title">Chicken Steak 🍗</div>

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
if st.button("Open Magic Recipe 💕"):
    st.success("✨ The book comes alive...")

    st.markdown("""
    <div class='cooking'>🍳🔥🐔</div>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### 👩‍🍳 Steps
    1️⃣ Mix ingredients 💫  
    2️⃣ Coat chicken 🐔  
    3️⃣ Rest 20 mins ⏳  
    4️⃣ Cook till golden 🔥  
    5️⃣ Serve & enjoy 🍽️✨  
    """)

    autoplay_audio("assets/sizzle.mp3")
```



