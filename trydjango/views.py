from django.http import HttpResponse
from article.models import Article
import random
from django.template.loader import render_to_string

def home_view(request, *args, **kwargs):

    random_id = random.randint(1,3)

    article_obj = Article.objects.get(id=random_id)
    article_list = Article.objects.all()

    my_list=  article_list


    context = {
        "my_list": my_list,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content,
    }
    HTML_STRING= render_to_string("home.html", context=context)


    return HttpResponse(HTML_STRING)

    