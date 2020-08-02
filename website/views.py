from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .models import Post
from django.db.models import Q


class PostList(ListView):
    model = Post
    paginate_by = 4

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.order_by('-id')
        return qs

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['items'] = Post.objects.all().count()
        return context

class PostDetail(DetailView):
    model = Post

class PostBusca(PostList):
    num= 0
    template_name = 'website/post_busca.html'
    def get_queryset(self, **kwargs):
        qs = super().get_queryset()
        termo = self.request.GET.get('termo')
        if not termo:
            return qs

        qs = qs.filter(
            Q(title__icontains=termo) |
            Q(content__icontains=termo)
        )
        return qs

class MapaView(TemplateView):
    template_name = 'website/tracado.html'


class TesteView(TemplateView):
    template_name = 'website/teste.html'