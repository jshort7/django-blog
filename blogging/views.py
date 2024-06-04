from django.views.generic import DetailView, ListView

from blogging.models import Post


# Create your views here.
class PostListView(ListView):
    published = Post.objects.exclude(published_date__exact=None)


class PostDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = 'blogging/detail.html'