from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#class view function nist ke loginrequird bezarim vase hmin azin use mikonim
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    #bayad to render dict befrestim vase hmin post dict kardim
    #baad mitonim be motaqayer haye toe dict ke sakhtim dastresi dashte bashim
    context = {
        "posts":Post.objects.all()
    }
    return render(request, "home.html", context)


class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = "posts" #vase inke to template home esmesh posts
    ordering = ['-date_posted']
    paginate_by = 5


#only show posts of one specific author not anyone else
class UserPostListView(ListView):
    model = Post
    template_name = 'user_posts.html'
    context_object_name = "posts" #vase inke to template home esmesh posts
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Any]:
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-date_posted")


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


#mesl hamon login required vali vase class
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    #inja be templates migim fqt title o content mikhaym
    fields = ['title','content']

    #form override mikonim ke nvisnde post current user bashe
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    #inam az template post_form estfde mikone mesl create

    #vase userpass check mikone bbine author post khode user ke edit kone
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False



class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    #success bayad bashe bedone delete shode koja bere
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False



def about(request):
    return render(request,"about.html", {"title":"about"})