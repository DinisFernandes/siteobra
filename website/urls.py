from django.urls import path, include
from .views import PostList
from .views import PostDetail
from .views import PostBusca
from .views import MapaView
from .views import TesteView
from django.urls import include

urlpatterns = [
    path('', PostList.as_view(), name="post_list"),
    path('post/<int:pk>/', PostDetail.as_view(), name="post_detail"),
    path('busca/', PostBusca.as_view(), name='post_busca'),
    path('tracado/', MapaView.as_view(), name='tracado'),
    path('teste/', TesteView.as_view(), name='teste'),
]