from django.shortcuts import render
from .models import Article
from django.contrib.auth.decorators import login_required
# from .forms import AriticleForm
from .forms import ArticleForm



# Create your views here.
def article_detail_view(request, id):
    article_obj = None

    if id is not None:
        article_obj =  Article.objects.get(id=id)
    context = {
        "object": article_obj,
    }


    return render(request, "article/detail.html", context=context)



@login_required
def article_create_view(request):

    # form = AriticleForm(request.POST or None)
    form = ArticleForm(request.POST or None)

    context = {
        "form": form
    }


    if form.is_valid():
        
        article_object = form.save()
        context['form'] = ArticleForm()


        # title = form.cleaned_data.get('title')
        # content = form.cleaned_data.get('content')
        
        # article_obj = Article.objects.create(title=title, content=content)
        # context['object']= article_object
        # context['created']= True

    return render(request, "article/create.html", context=context)



def article_search_view(request):
    query_dict = request.GET
    query = query_dict.get("q")
    article_obj =  None

    try:
        query = int(query_dict.get("q"))
    except:
        query = None

    if query is not None:
        article_obj =  Article.objects.get(id=query)

    context = {
        "object": article_obj 
    }

    return render(request, "article/search.html", context=context)