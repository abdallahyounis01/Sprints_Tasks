from django.shortcuts import render, HttpResponse
from .forms import PostForm


def home(request):
    if request.method == 'POST':
        details = PostForm(request.POST)
        if details.is_valid():
            post = details.save(commit=False)
            post.save()
            return HttpResponse("Data Has Been Successfully Submitted")
        else:
            return render(request, 'home.html', {'form': details})
    else:
        form = PostForm(None)
        return render(request, 'home.html', {'form': form})