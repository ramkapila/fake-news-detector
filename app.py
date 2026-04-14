from flask import Flask, render_template, request
import joblib
from preprocess import clean_text
import re
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin@001",
    database="fake_news_db"
)

cursor = db.cursor()


def is_valid_news(text):
    words = re.findall(r"[a-zA-Z]{3,}", text)
    return len(words) >= 5


app = Flask(__name__)

model = joblib.load("model/model.pkl")
tfidf = joblib.load("model/tfidf.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    confidence = None
    prediction_id = None

    if request.method == "POST":
        text = request.form["news"]

        if not is_valid_news(text):
            return render_template(
                "index.html",
                prediction="Invalid Input",
                confidence="Please enter meaningful news text."
            )

        cleaned = clean_text(text)
        vector = tfidf.transform([cleaned])
        proba = model.predict_proba(vector)[0]

        prediction = "Fake" if proba[1] > 0.5 else "Dependable"
        confidence = round(max(proba) * 100, 2)

        cursor.execute("SELECT model_id FROM model_info LIMIT 1")
        model_id = cursor.fetchone()[0]

        sql = """
        INSERT INTO news_articles(content, prediction, confidence, model_id)
        VALUES (%s, %s, %s, %s)
        """
        val = (text, prediction, confidence, model_id)

        cursor.execute(sql, val)
        db.commit()

        prediction_id = cursor.lastrowid

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        prediction_id=prediction_id
    )

@app.route("/feedback", methods=["POST"])
def feedback():

    prediction_id = request.form["prediction_id"]
    comment = request.form["comment"]
    rating = request.form["rating"]

    sql = """
    INSERT INTO feedback(prediction_id, user_comment, rating)
    VALUES (%s,%s,%s)
    """

    cursor.execute(sql, (prediction_id, comment, rating))
    db.commit()

    return "Feedback submitted successfully!"


if __name__ == "__main__":
    app.run(debug=True)
