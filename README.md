# 🛒 E-Commerce Price Tracker Bot

A Flask-based web application that allows users to track prices of products from e-commerce platforms and get notified via email when the product price drops below their desired value. Built for smart shoppers who never want to miss a deal.

---

## 📌 Features

- 🔐 User registration and login system
- 🎯 Track product prices by entering URL and target price
- 📬 Email notifications when price matches or drops below your input
- 💾 MongoDB Atlas for scalable, cloud-hosted NoSQL storage
- 🌐 Clean and responsive UI using Bootstrap

---

## 🚀 Getting Started

### 🔧 Installation
# Clone the repository
git clone <repo-url>
cd E-Commerce-Price-Tracker

# Install Python dependencies
pip install -r requirements.txt

**⚙️ Configuration**
Before running the app, configure your MongoDB URI in app.py:
app.config['MONGO_URI'] = "your-mongodb-uri"
💡 Use MongoDB Atlas to get a free cloud-hosted NoSQL database.

▶️ Running the App
./run

🧪 Tech Stack
Technology | Purpose
Python | Backend programming
Flask | Lightweight web framework
MongoDB | NoSQL database
HTML5 | Webpage structure
CSS3 | Styling
JavaScript | Frontend interactivity
Bootstrap | Responsive frontend design

📁 Project Structure
E-Commerce-Price-Tracker/
├── static/             # CSS, JS files
├── templates/          # HTML templates
├── app.py              # Main Flask app
├── run                 # Run script
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation

