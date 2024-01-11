from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
    def save(self, commit=True):
        instance = super().save(commit=False)
    
        # Move the uploaded image to the desired directory
        new_image_path = f'post_images/{instance.image.name}'
        instance.image.name = new_image_path
        instance.save()

        return instance