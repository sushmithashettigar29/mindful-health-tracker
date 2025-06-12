import streamlit as st
import pandas as pd
import datetime
import random
import os
import time
import matplotlib.pyplot as plt
import seaborn as sns

# --- App Config ---
st.set_page_config(page_title="MindfulHealth", layout="wide")

# --- Sidebar ---
with st.sidebar:
    st.title("🌱 MindfulHealth")
    st.markdown("Track your health habits, mood, and mindfulness.")
    st.markdown("---")
    st.info("Made with 💖 by Sushmitha | [GitHub](https://github.com/sushmithashettigar29/mindful-health-tracker)")

# --- File path ---
DATA_FILE = "health_data.csv"
if not os.path.exists(DATA_FILE):
    pd.DataFrame(columns=["date", "water", "sleep", "steps", "mood"]).to_csv(DATA_FILE, index=False)

df = pd.read_csv(DATA_FILE)
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])
df["date"] = pd.to_datetime(df["date"]).dt.date

# --- Emoji mapping ---
emoji_map = {
    "Happy 😊": "Happy",
    "Okay 🙂": "Okay",
    "Tired 😴": "Tired",
    "Sad 😢": "Sad",
    "Stressed 😖": "Stressed"
}
reverse_emoji_map = {v: k for k, v in emoji_map.items()}
df["mood"] = df["mood"].replace(emoji_map)

# --- Calculate streak ---
def calculate_streak(dates):
    dates = sorted(set(pd.to_datetime(dates).dt.date), reverse=True)
    streak = 0
    today = datetime.date.today()
    for i, date in enumerate(dates):
        if date == today - datetime.timedelta(days=i):
            streak += 1
        else:
            break
    return streak

# --- Main Tabs ---
tab1, tab2, tab3 = st.tabs(["📅 Daily Tracker", "📈 Progress Graphs", "🧘 Mindful Minutes"])

# --- Tab 1: Daily Tracker ---
with tab1:
    st.header("🗓️ Today's Check-in")
    today = datetime.date.today()
    today_data = df[df["date"] == today]

    streak = calculate_streak(df["date"])
    st.info(f"🔥 Current Streak: {streak} day(s)")

    # Summary Stats
    if len(df) > 6:
        recent = df[df["date"] >= today - datetime.timedelta(days=6)]
        col1, col2, col3 = st.columns(3)
        col1.metric("Avg Sleep", f"{recent['sleep'].mean():.1f} hrs")
        col2.metric("Avg Steps", f"{recent['steps'].mean():.0f}")
        top_mood = recent["mood"].mode()[0]
        col3.metric("Top Mood", reverse_emoji_map[top_mood])

    if today_data.empty:
        with st.form("daily_form"):
            water = st.slider("Water intake (cups)", 0, 15, 8)
            sleep = st.slider("Sleep (hours)", 0, 12, 7)
            steps = st.slider("Steps walked", 0, 20000, 6000)
            mood = st.selectbox("Mood", list(emoji_map.keys()))
            submitted = st.form_submit_button("Submit Entry")

        if submitted:
            mood_plain = emoji_map[mood]
            new_row = pd.DataFrame([[today, water, sleep, steps, mood_plain]],
                                   columns=["date", "water", "sleep", "steps", "mood"])
            df = pd.concat([df, new_row], ignore_index=True)
            df.to_csv(DATA_FILE, index=False)
            st.success("✅ Entry saved!")
            st.balloons()
            st.toast("Great job checking in today! 🌟", icon="👏")
            st.rerun()

    else:
        st.success("You already submitted today's entry.")

        with st.expander("✏️ Edit Today's Entry"):
            default_vals = today_data.iloc[0]
            water = st.slider("Water intake (cups)", 0, 15, int(default_vals["water"]))
            sleep = st.slider("Sleep (hours)", 0, 12, int(default_vals["sleep"]))
            steps = st.slider("Steps walked", 0, 20000, int(default_vals["steps"]))
            mood_list = list(emoji_map.keys())
            current_mood = reverse_emoji_map.get(default_vals["mood"], mood_list[0])
            mood = st.selectbox("Mood", mood_list, index=mood_list.index(current_mood))
            if st.button("Update Entry"):
                df = df[df["date"] != today]
                mood_plain = emoji_map[mood]
                updated = pd.DataFrame([[today, water, sleep, steps, mood_plain]],
                                       columns=["date", "water", "sleep", "steps", "mood"])
                df = pd.concat([df, updated], ignore_index=True)
                df.to_csv(DATA_FILE, index=False)
                st.success("✔️ Entry updated.")
                st.toast("Updated today's health log ✅", icon="🔄")
                st.rerun()

        if st.button("🗑️ Clear Today's Entry"):
            df = df[df["date"] != today]
            df.to_csv(DATA_FILE, index=False)
            st.warning("Today's entry removed.")
            st.rerun()

# --- Tab 2: Progress Graphs ---
with tab2:
    st.header("📊 Your Progress")

    if df.empty:
        st.warning("No data yet. Start with the Daily Tracker tab.")
    else:
        df["date"] = pd.to_datetime(df["date"])
        df.sort_values("date", inplace=True)

        st.subheader("📈 Trends Over Time")
        st.line_chart(df.set_index("date")[["water", "sleep", "steps"]])

        st.subheader("📊 Mood Distribution")
        mood_counts = df["mood"].value_counts().reset_index()
        mood_counts.columns = ["mood", "count"]
        mood_df = pd.DataFrame([{"mood": row["mood"]} for _, row in mood_counts.iterrows() for _ in range(row["count"])])

        fig, ax = plt.subplots(figsize=(8, 3))
        sns.countplot(
            data=mood_df,
            x="mood",
            hue="mood", 
            palette="pastel",
            legend=False,
            ax=ax
        )
        fig.patch.set_alpha(0.0)
        ax.set_facecolor("none")
        ax.set_xlabel("Mood", color="#F9FAFB", fontsize=12)
        ax.set_ylabel("Count", color="#F9FAFB", fontsize=12)
        ax.set_title("Mood Distribution", color="#F9FAFB", fontsize=14)
        ax.tick_params(axis='x', colors="#F9FAFB", labelrotation=15)
        ax.tick_params(axis='y', colors="#F9FAFB")
        st.pyplot(fig)

        st.subheader("📅 Weekly Averages")
        weekly_avg = df.set_index("date").resample("W").mean(numeric_only=True)
        st.line_chart(weekly_avg[["water", "sleep", "steps"]])

        st.download_button("⬇️ Download My Data",
            df.replace(reverse_emoji_map).to_csv(index=False),
            file_name="my_health_data.csv", mime="text/csv")

# --- Tab 3: Mindful Minutes ---
with tab3:
    st.header("💪 Mindful Minutes")
    st.subheader("Choose a Breathing Exercise")
    exercise = st.selectbox("Pick a duration", ["15 seconds", "30 seconds", "Box Breathing (4x4x4x4)"])

    def breathing_timer(seconds):
        with st.empty():
            for i in range(seconds, 0, -1):
                st.metric("Time Left", f"{i} sec")
                time.sleep(1)
            st.success("Great Job! Feel the calm. 😌")

    if st.button("Start Breathing"):
        if exercise == "15 seconds":
            breathing_timer(15)
        elif exercise == "30 seconds":
            breathing_timer(30)
        elif exercise == "Box Breathing (4x4x4x4)":
            for label in ["Inhale", "Hold", "Exhale", "Hold"]:
                st.write(f"**{label}...**")
                breathing_timer(4)

    st.subheader("✨ Quote of the Day")
    st.info(random.choice([
        "One small positive thought can change your day.",
        "You're doing better than you think.",
        "Healthy mind, healthy life.",
        "Take a moment. You deserve peace.",
        "Slow down and breathe deeply.",
        "Consistency is better than perfection."
    ]))

# --- Footer ---
st.markdown("---")
st.markdown("<center><sub>Built with ❤️ using Streamlit | © 2025 MindfulHealth</sub></center>", unsafe_allow_html=True)