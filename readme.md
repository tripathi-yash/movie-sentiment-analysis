# 🎬 Movie Review Sentiment Analysis

A Machine Learning + Flask web application that predicts the sentiment of movie reviews (Positive / Negative).

## 🚀 Project Overview
This project uses a trained deep learning model to classify movie reviews into sentiment categories.  
It includes a simple Flask-based web interface for real-time predictions.

## 🧠 Features
- Predict sentiment from text input
- Clean and simple web UI
- Trained ML/DL model (Keras)
- Tokenizer-based text preprocessing
- Easy to run locally

## 🛠️ Tech Stack
- Python
- Flask
- TensorFlow / Keras
- HTML, CSS, JavaScript
- NumPy, Pandas

## 📂 Project Structure
├── app.py
├── model.keras
├── tokenizer.pkl
├── templates/
│ └── index.html
├── requirements.txt
└── README.md

## ⚙️ Installation & Setup
### 1. Clone the repository
```bash
git clone https://github.com/tripathi-yash/movie-sentiment-analysis.git
cd movie-sentiment-analysis

2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Run the application
python app.py

📊 Model Details
Input: Movie review text
Output: Positive / Negative sentiment
Preprocessing: Tokenization + Padding
Model: LSTM / Deep Learning (Keras)

📦 Requirements

Make sure you have:

Python-3.12.10
Flask
tensorflow-2.19.0
keras-3.13.2
NumPy
Pandas