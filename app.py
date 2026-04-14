from flask import Flask, render_template, request
import joblib
from preprocess import clean_text
import re
import mysql.connector
from mysql.connector import pooling
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

model = joblib.load("model/model.pkl")
tfidf = joblib.load("model/tfidf.pkl")

db_pool = pooling.MySQLConnectionPool(
    pool_name="fake_news_pool",
    pool_size=5,
    host=os.getenv("DB_HOST", "localhost"),
    user=os.getenv("DB_USER", "root"),
    password=os.getenv("DB_PASSWORD", ""),
    database=os.getenv("DB_NAME", "fake_news_db")
)


def get_db():
    return db_pool.get_connection()


def is_valid_news(text):
    words = re.findall(r"[a-zA-Z]{3,}", text)
    return len(words) >= 5


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    confidence = None
    prediction_id = None
    error = None

    if request.method == "POST":
        text = request.form["news"]

        if not is_valid_news(text):
            return render_template("index.html", prediction="Invalid Input", confidence=None, error="Please enter meaningful news text.")

        cleaned = clean_text(text)
        vector = tfidf.transform([cleaned])
        proba = model.predict_proba(vector)[0]

        prediction = "Fake" if proba[1] > 0.5 else "Dependable"
        confidence = round(max(proba) * 100, 2)

        db = get_db()
        cursor = db.cursor()
        try:
            cursor.execute("SELECT model_id FROM model_info LIMIT 1")
            model_id = cursor.fetchone()[0]
            cursor.execute(
                "INSERT INTO news_articles(content, prediction, confidence, model_id) VALUES (%s, %s, %s, %s)",
                (text, prediction, confidence, model_id)
            )
            db.commit()
            prediction_id = cursor.lastrowid
        finally:
            cursor.close()
            db.close()

    return render_template("index.html", prediction=prediction, confidence=confidence, prediction_id=prediction_id, error=error)


@app.route("/feedback", methods=["POST"])
def feedback():
    prediction_id = request.form["prediction_id"]
    comment = request.form["comment"]
    rating = request.form["rating"]

    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute(
            "INSERT INTO feedback(prediction_id, user_comment, rating) VALUES (%s, %s, %s)",
            (prediction_id, comment, rating)
        )
        db.commit()
    finally:
        cursor.close()
        db.close()

    return "Feedback submitted successfully!"


if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG", "false").lower() == "true")
