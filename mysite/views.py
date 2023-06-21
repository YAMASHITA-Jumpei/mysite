from django.shortcuts import render
from django.views.generic import View
from .models import Profile, Work, Blog


class IndexView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by('-id')[0]
        work_data = Work.objects.order_by('-id')
        return render(request, 'mysite/index.html', {
            'profile_data': profile_data,
            'work_data': work_data
        })


class BlogView(View):
    def get(self, request, *args, **kwargs):
        blog_data = Blog.objects.order_by('-id')
        return render(request, 'mysite/blog.html', {
            'blog_data': blog_data
        })


class BlogDetailView(View):
    def get(self, request, *args, **kwargs):
        blog_data = Blog.objects.get(id=self.kwargs['pk'])
        return render(request, 'mysite/blog_detail.html', {
            'blog_data': blog_data
        })
