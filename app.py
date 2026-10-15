
import streamlit as st

st.set_page_config(
    page_title="Birthday Surprise 🎂",
    page_icon="🎂"
)

FRIEND_NAME = "Pravalika"  # Change to your friend's name

st.title("🎉 Happy Birthday! 🎂")
st.balloons()

st.header(f"Dear {FRIEND_NAME}, 💖")

st.write("""
🌈 Today is your special day!

You are an amazing friend, and I'm so lucky to have you
in my life. May your birthday be filled with happiness,
love, laughter, and beautiful memories! 💕
""")

st.divider()

st.subheader("💌 A Letter for You")

with st.expander("Click to open your birthday letter 💗"):
    st.write(f"""
    Dear {FRIEND_NAME},

    Thank you for being my best friend.
    Every memory with you is precious to me.

    May all your dreams come true.
    Keep smiling and shining always! ✨

    Happy Birthday, Pavuuuu! 🎂💝
    """)

st.divider()

st.subheader("🎁 Your Special Surprise")

if st.button("Open Your Gift 💝"):
    st.balloons()
    st.write("Love you beyyy! 🫶🎉")



from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent
photo_folder = PROJECT_DIR / "photos"

st.header("📸 Our Beautiful Memories 💕")

if photo_folder.exists():
    photos = [
        p for p in photo_folder.iterdir()
        if p.is_file()
        and p.suffix.lower() in [".jpg", ".jpeg", ".png", ".webp"]
    ]

    if photos:
        columns = st.columns(2)

        for i, photo in enumerate(photos):
            with columns[i % 2]:
                st.image(
                    str(photo),
                    caption=f"Memory {i + 1} 💖",
                    use_container_width=True
                )
    else:
        st.warning(
            "No image files found. Put your actual pictures inside photos."
        )
else:
    st.warning("The photos folder was not found.")





from pathlib import Path

st.divider()
st.header("🎵 Birthday Music Corner 🎶")
st.write("Let's celebrate with music, Bestie! 💖")

PROJECT_DIR = Path(__file__).resolve().parent
music_file = PROJECT_DIR / "music" / "birthday.mp3"

if music_file.is_file():
    st.audio(str(music_file), format="audio/mpeg")
else:
    st.warning("Song not found! Check your music folder.")
    st.write("Expected location:", str(music_file))
