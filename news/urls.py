from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('detail/<int:pk>', views.news_detail, name='news_detail'),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
    # path('filter/<int:pk>', views.news_date_filter, name='news_date_filter'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
