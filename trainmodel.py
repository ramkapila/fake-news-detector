import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib
from preprocess import clean_text

# Load dataset
df = pd.read_csv("data/train.csv")

# Drop useless column
if 'Unnamed: 6' in df.columns:
    df.drop(columns=['Unnamed: 6'], inplace=True)

# Drop missing values
df.dropna(inplace=True)

# Combine title + text
df['content'] = df['title'] + " " + df['text']
df['content'] = df['content'].apply(clean_text)

# Features and labels
X = df['content']
y = df['class']   # ✅ CORRECT label column

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# TF-IDF
tfidf = TfidfVectorizer(max_features=5000)
X_train_vec = tfidf.fit_transform(X_train)
X_test_vec = tfidf.transform(X_test)

# Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

# Evaluation
y_pred = model.predict(X_test_vec)
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, "model/model.pkl")
joblib.dump(tfidf, "model/tfidf.pkl")
