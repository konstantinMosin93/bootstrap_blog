from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from .models import Post


class MainView(View):
    @staticmethod
    def get(request, *args, **kwargs):
        posts = Post.objects.order_by('-id').all()

        paginator = Paginator(posts, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            'blog/home.html',
            context={'page_obj': page_obj}
        )
