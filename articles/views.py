from django.shortcuts import render

from articles.models import Article


def articles(request):
    articles_ = Article.objects.all()

    my_dict = {
        'title': 'Статьи',
        'articles': articles_,
    }
    return render(request, 'articles/index.html', my_dict)
