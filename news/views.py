from django.shortcuts import render, get_object_or_404
from news.models import News


def news_list(request):
    # Вывод новостей#
    news = News.objects.all
    return render(request, 'news/news_list.html', {'news': news})


def news_detail(request, pk):
    new = get_object_or_404(News, id=pk)
    return render(request, 'news/news_detail.html', {'new': new})

