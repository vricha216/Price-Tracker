# Price-Tracker
A Flask-based web application that allows users to track product prices from e-commerce sites and get notified via email when the price drops to their desired amount. Perfect for smart shopping and deal hunting!

---

## 📌 Features

- 🔐 User Registration & Authentication
- 🧠 Create custom bots by entering product URLs and target prices
- 📬 Email alerts when product price drops below or equals target
- 🌐 Web Interface built with Bootstrap for responsiveness
- ☁️ MongoDB Atlas integration for cloud-hosted database

---

## 🚀 Getting Started

### 🔧 Setup & Installation

1. Clone the repository:
   git clone <repo-url>
   cd Price-Tracker
   
Install the dependencies:
pip install -r requirements.txt

Set your MongoDB URI in app.py:
app.config['MONGO_URI'] = "your-mongodb-uri"

Run the application:
./run

💡 Tip: Use MongoDB Atlas for free cloud database hosting.

**🧪 Tech Stack**

**Technology	Purpose**
**Python	Core programming language**

Flask	Web framework
MongoDB	NoSQL database (Atlas hosted)
HTML5	Frontend structure
CSS3	Styling
JavaScript	Frontend interactivity
Bootstrap	Responsive UI framework


**📂 Project Structure**
**Price-Tracker/**
├── static/           # CSS, JS files
├── templates/        # HTML templates
├── app.py            # Main Flask app
├── run               # Run script
├── requirements.txt  # Python dependencies
└── README.md         # Project description
