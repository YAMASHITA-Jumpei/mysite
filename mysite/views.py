from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Profile, Work, Blog, Education, Experience
from .forms import BlogForm
from django.contrib.auth.mixins import LoginRequiredMixin


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


class CreateBlogView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = BlogForm(request.POST or None)
        return render(request, 'mysite/blog_post.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = BlogForm(request.POST or None)

        if form.is_valid():
            blog_data = Blog()
            blog_data.author = request.user
            blog_data.title = form.cleaned_data['title']
            blog_data.content = form.cleaned_data['content']
            blog_data.save()
            return redirect('mysite:blog_detail', blog_data.id)

        return render(request, 'mysite/blog_post.html', {
            'form': form
        })


class BlogEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        blog_data = Blog.objects.get(id=self.kwargs['pk'])
        form = BlogForm(
            request.POST or None,
            initial={
                'title': blog_data.title,
                'content': blog_data.content
            }
        )
        return render(request, 'mysite/blog_post.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = BlogForm(request.POST or None)

        if form.is_valid():
            blog_data = Blog.objects.get(id=self.kwargs['pk'])
            blog_data.title = form.cleaned_data['title']
            blog_data.content = form.cleaned_data['content']
            blog_data.save()
            return redirect('mysite:blog_detail', self.kwargs['pk'])

        return render(request, 'mysite/blog_post.html', {
            'form': form
        })


class BlogDeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        blog_data = Blog.objects.get(id=self.kwargs['pk'])
        return render(request, 'mysite/blog_delete.html', {
            'blog_data': blog_data,
        })

    def post(self, request, *args, **kwargs):
        blog_data = Blog.objects.get(id=self.kwargs['pk'])
        blog_data.delete()
        return redirect('mysite:blog')


class AboutView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by('-id')[0]
        experience_data = Experience.objects.order_by('id')
        education_data = Education.objects.order_by('id')
        return render(request, 'mysite/about.html', {
                      'profile_data': profile_data,
                      'experience_data': experience_data,
                      'education_data': education_data,
                      })
