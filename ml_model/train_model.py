import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("ml_model/dataset/social_media_posts.csv")

# Convert engagement labels to numbers
encoder = LabelEncoder()
data["Engagement"] = encoder.fit_transform(data["Engagement"])

# Features
X = data[["Likes", "Comments", "Shares"]]

# Target
y = data["Engagement"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train Model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Prediction
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy : {accuracy*100:.2f}%")

# Save Model
joblib.dump(model, "ml_model/post_popularity_model.pkl")
joblib.dump(encoder, "ml_model/label_encoder.pkl")

print("Model Saved Successfully!")