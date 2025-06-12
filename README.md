# 🌱 MindfulHealth - Personal Wellness Tracker

**MindfulHealth** is a beginner-friendly, fully interactive health tracker app built with **Python** and **Streamlit**. It helps users log and visualize their daily health habits—such as water intake, sleep, exercise, and mood—while offering calming mindfulness features like breathing exercises and motivational quotes.

## 🌐 Live Demo

[👉 Click here to try MindfulHealth Live!](https://mindful-health-tracker.streamlit.app)

---

## 🚀 Features

### 📅 Daily Tracker

- Log your daily **water intake**, **sleep duration**, **steps walked**, and **mood**
- Update or remove today's entry
- Emoji-based mood tracking for a friendly UI
- Tracks your **streak** and recent averages (last 7 days)

### 📈 Progress Graphs

- Visualize progress with **line charts** and **mood distribution graphs**
- Weekly averages to monitor habits
- Download your personal CSV data with one click

### 🧘 Mindful Minutes

- Breathing exercises (15s, 30s, Box Breathing 4-4-4-4)
- Random motivational quote of the day to encourage self-care

---

## 🛠️ Tech Stack

- **Frontend & UI**: [Streamlit](https://streamlit.io/)
- **Data Handling**: [Pandas](https://pandas.pydata.org/)
- **Visualization**: [Matplotlib](https://matplotlib.org/), [Seaborn](https://seaborn.pydata.org/)
- **Storage**: Local CSV file (`health_data.csv`) – no backend or database required

---

## 📹 Video Demo

Watch the full walkthrough here:  
👉 Demo Video

[![CareTrack Demo](https://img.youtube.com/vi/tKiqx73z1Oo/0.jpg)](https://youtu.be/tKiqx73z1Oo)

---

## 📸 Screenshots

### Daily Tracker Page

![Daily Tracker](./assets//dailytracker.png)

### Progress Graphs Page

![Progress Graph Section](./assets/progressgraph.png)
![Mood Distribution Section](./assets/mooddistribution.png)
![Weekly Report Section](./assets/weeklyavg.png)

### Mindful Minutes Page

![Mindful Minutes Page](./assets/mindfulminutes.png)

---

## 📂 Project Structure

<pre lang="bash"><code>
mindful-health/
├── .streamlit/
│   └── config.toml
├── health_data.csv
├── mindful_health.py
└── README.md
</code></pre>

---

## 🧪 Getting Started

### ✅ Prerequisites

- Python 3.8 or higher
- pip

### 🔧 Installation

```bash
git clone https://github.com/sushmithashettigar29/mindful-health-tracker.git
cd mindful-health-tracker
streamlit run app.py
```

install packages manually:

```bash
pip install streamlit pandas matplotlib seaborn

```

## 📝 License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and distribute for personal and commercial purposes.

---

## 🙌 Contribution

Contributions, issues, and feature requests are welcome!  
Feel free to fork this repo and submit a pull request.

---

## 🙏 Acknowledgements

- Built for Hack4Health 2025
- Powered by Streamlit
- Inspired by the importance of daily wellness & habit tracking

## 💬 Contact

Created with ❤️ by Sushmitha Shettigar  
Reach out via [LinkedIn](https://www.linkedin.com/in/sushmithashettigar/) or [GitHub](https://github.com/sushmithashettigar29)
