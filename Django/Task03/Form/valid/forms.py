from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["username", "gender", "text"]

    def clean(self):
        super(PostForm, self).clean()
        username = self.cleaned_data.get('username')
        text = self.cleaned_data.get('text')
        if len(username) < 6:
            self._errors['username'] = self.error_class(['You Have To Enter More Than 5 Char in The Username Field'])
        if len(text) < 10:
            self._errors['text'] = self.error_class(['You Have To Enter More Than 9 Char in The Text Field'])
        return self.cleaned_data
