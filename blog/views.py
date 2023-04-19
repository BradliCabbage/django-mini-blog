from django.shortcuts import render
from blog.models import Author, Blog

from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import datetime

from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
@login_required
def index(request):
    """View function for home page of the site"""
    num_blogs = Blog.objects.all().count()
    num_authors = Author.objects.all().count()

    context = {
        "num_blogs": num_blogs,
        "num_authors": num_authors
    }

    return render(request, "index.html", context=context)

class BlogListView(LoginRequiredMixin, generic.ListView):
    model = Blog

class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author

class BlogDetailView(LoginRequiredMixin, generic.ListView):
    model = Blog

class AuthorDetailView(LoginRequiredMixin, generic.ListView):
    model = Author

def blog_comment_create(request):
    if request.method == "POST":
        form = AddComentForm(request.POST)

        if form.is_valid():
          description = form.data.get("description")
          if description == "":
              return HttpResponseRedirect(request.META["HTTP_REFERER"])
          blog_title = form.data.get("blogtitle")
          blog_comment = BlogComment(description=description)
          blog_comment.post_date = datetime.datetime.now()
          blog_comment.author = request.user
          blog_comment.blog = Blog.object.get(title=blog_title)
          blog_comment.save()
          return HttpResponseRedirect(request.META["HTTP_REFERER"])
        else:
          return HttpResponseRedirect(reverse("index"))