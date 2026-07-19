from django import forms
from .models import Post, Like, Comment


# ==========================
# Post Form
# ==========================

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            "user",
            "department",
            "caption",
            "image",
        ]

        widgets = {

            "user": forms.Select(attrs={
                "class": "form-select"
            }),

            "department": forms.Select(attrs={
                "class": "form-select"
            }),

            "caption": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Write caption..."
            }),

            "image": forms.FileInput(attrs={
                "class": "form-control"
            }),
        }


# ==========================
# Like Form
# ==========================

class LikeForm(forms.ModelForm):

    class Meta:
        model = Like
        fields = [
            "user",
            "post",
        ]

        widgets = {

            "user": forms.Select(attrs={
                "class": "form-select"
            }),

            "post": forms.Select(attrs={
                "class": "form-select"
            }),
        }


# ==========================
# Comment Form
# ==========================

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["user", "post", "comment"]

        widgets = {
            "user": forms.Select(attrs={
                "class": "form-control"
            }),

            "post": forms.Select(attrs={
                "class": "form-control"
            }),

            "comment": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Write your comment here..."
            }),
        }
