# 🌍 AI Travel Planner

An AI-powered web application that generates personalized travel itineraries based on the destination, trip duration, preferences and budget.

Built with **Flask**, **OpenAI API** and **Unsplash API**.

---

## ✨ Features

- 🤖 AI-generated travel itineraries
- 📅 Day-by-day planning
- 💰 Budget-aware recommendations
- ❤️ Personalized based on user interests
- 🖼️ Destination image from Unsplash
- 💾 Save itineraries with SQLite
- 📖 Travel history
- ⚠️ Error handling and input validation

---

## 🛠️ Technologies

- Python
- Flask
- OpenAI API
- Unsplash API
- SQLite
- Bootstrap 5

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/ai-travel-planner.git
cd ai-travel-planner
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it.

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
OPENAI_API_KEY=your_key
UNSPLASH_ACCESS_KEY=your_key
```

Run the application:

```bash
python run.py
```

Open your browser at:

```
http://127.0.0.1:5000
```

---

## 📂 Project Structure

```
app/
├── services/
├── utils/
├── database.py
├── routes.py
└── __init__.py

static/
templates/
tests/

run.py
requirements.txt
README.md
```

---

## 🔮 Future Improvements

- User authentication
- Interactive maps
- PDF export
- Share itineraries
- Weather integration
- Multi-language support

---

## 📄 License

This project was created for educational and portfolio purposes.