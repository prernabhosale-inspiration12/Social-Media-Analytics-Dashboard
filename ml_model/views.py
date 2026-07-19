from django.shortcuts import render
from .models import Prediction

import joblib
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "post_popularity_model.pkl"))
encoder = joblib.load(os.path.join(BASE_DIR, "label_encoder.pkl"))


def ml_prediction(request):

    prediction = None

    if request.method == "POST":

        likes = int(request.POST["likes"])
        comments = int(request.POST["comments"])
        shares = int(request.POST["shares"])

        data = pd.DataFrame(
            [[likes, comments, shares]],
            columns=["Likes", "Comments", "Shares"]
        )

        result = model.predict(data)

        prediction = encoder.inverse_transform(result)[0]

        Prediction.objects.create(
            likes=likes,
            comments=comments,
            shares=shares,
            prediction=prediction
        )

    history = Prediction.objects.order_by("-created_at")[:10]

    return render(
    request,
    "ml_model/predict.html",
    {
        "prediction": prediction,
        "history": history,
    }
)