from django.contrib.auth import login
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views import View

from .forms import SignUpForm
from .models import Post


class MainView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        posts = Post.objects.order_by('-id').all()
        paginator = Paginator(posts, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(
            request, 'blog/home.html', context={'page_obj': page_obj}
        )


class PostDetailView(View):
    @staticmethod
    def get(request, slug, *args, **kwargs):
        post = get_object_or_404(Post, url=slug)
        return render(request, 'blog/post_detail.html', context={'post': post})


class SignUpView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'blog/signup.html', context={'form': form})

    @staticmethod
    def post(request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            return render(request, 'blog/signup.html', context={'form': form})
