from django.shortcuts import render, get_object_or_404, redirect
from news.models import News, Comments
from news.forms import CommentForm
from datetime import datetime, timedelta
from django.core.paginator import Paginator


def news_list(request):
    # Вывод новостей
    news = News.objects.all()
    paginator = Paginator(news, 10)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    return render(request, 'news/news_list.html', {'news': page})


def news_detail(request, pk):
    # вывод полной статьи.
    new = get_object_or_404(News, id=pk)
    comment = Comments.objects.filter(new=pk, moderation=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.new = new
            form.save()
            return redirect(news_detail, pk)

    else:
        form = CommentForm()
    return render(request,
                  'news/news_detail.html',
                  {'new': new,
                  'comments': comment,
                  'form': form})


'''def news_date_filter(request, pk):
    # фильтр новостей по дате.
    news = News.objects.all()

    today = datetime.now()
    if pk == 1:
        now = today - timedelta(minutes=60*24)
        news = news.filter(date_of_creation__gte=now)
    elif pk == 2:
        now = today - timedelta(minutes=60*24*7)
        news = news.filter(date_of_creation__gte=now)
    elif pk == 3:
        now = today - timedelta(minutes=60*24*30)
        news = news.filter(date_of_creation__gte=now)
    elif pk == 4:
        news = news.order_by

    return render(request, 'news/news_list.html', {'news': news})'''







