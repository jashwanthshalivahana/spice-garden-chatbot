# 🍛 Spice Garden AI Chatbot

An AI-powered chatbot for **Spice Garden Restaurant, Hyderabad** — built with **Flask** and **Groq API**. Answers questions about the menu, timings, location, and handles reservations instantly.

---

## 🖥️ Live Demo

> Deploy your own in 10 minutes using the guide below ↓

---

## ✨ Features

- 💬 Real-time AI chat powered by Groq's ultra-fast LLM
- 🍽️ Pre-configured for restaurant — menu, hours, location, reservations
- 📱 Fully responsive — works on mobile and desktop
- ⚡ Instant replies (Groq is the fastest LLM API available)
- 🎨 Clean dark-themed chat UI

---

## 🗂️ Project Structure

```
spice-garden-chatbot/
├── app.py            ← Flask backend + Groq API + Chat UI (all in one)
├── requirements.txt  ← Python dependencies
└── README.md
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Programming language |
| **Flask** | Web framework — serves the UI and API |
| **Groq API** | Ultra-fast LLM inference (Llama 3.1) |
| **HTML/CSS/JS** | Chat UI embedded in app.py |

---

## ⚙️ Local Setup

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/spice-garden-chatbot.git
cd spice-garden-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your Groq API key

Open `app.py` and find this line near the top:
```python
GROQ_API_KEY = "your_groq_api_key_here"
```
Replace `your_groq_api_key_here` with your actual key from **[console.groq.com](https://console.groq.com)** (free to sign up).

### 4. Run the app
```bash
python app.py
```

Open your browser and go to: **http://127.0.0.1:5000**

---

## 🚀 Deploy to Render (Free)

1. Fork this repo to your GitHub
2. Go to **[render.com](https://render.com)** → Sign up with GitHub
3. Click **New +** → **Web Service** → connect your repo
4. Fill in:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
   - **Instance Type:** Free
5. Click **Create Web Service**
6. Get your live public URL in ~3 minutes 🎉

---

## 🤖 Customising for Your Own Restaurant

Open `app.py` and edit the `SYSTEM_PROMPT` section:

```python
SYSTEM_PROMPT = """You are a helpful assistant for Spice Garden Restaurant, Hyderabad.
Hours: 11 AM - 11 PM daily. Location: Road No. 36, Jubilee Hills.
Specialties: Biryani, Kebabs, Haleem.
For reservations, ask for name and phone — say team confirms in 30 minutes.
Keep replies friendly, under 100 words, always in English unless asked."""
```

Change the restaurant name, location, hours, and specialties to match your own.

---

## 🔑 Getting a Free Groq API Key

1. Go to **[console.groq.com](https://console.groq.com)**
2. Sign up for a free account
3. Click **API Keys** → **Create API Key**
4. Copy the key (starts with `gsk_`) and paste it in `app.py`

---

## 📦 Dependencies

```
flask==3.0.3
groq==1.2.0
python-dotenv==1.0.1
```

---

## 📄 License

This project is open source and free to use for personal and commercial projects.

---

> Built with ❤️ using Flask + Groq API
