from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
# from .forms import AriticleForm
from .forms import ArticleForm
from django.http import Http404
from django.db.models import Q


# Create your views here.
def article_detail_view(request, slug=None):
    article_obj = None

    if slug is not None:
        try:
            article_obj =  Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            article_obj =  Article.objects.filter(slug=slug).first()
        except:
            raise Http404


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
        return redirect(article_object.get_absolute_url())

        # title = form.cleaned_data.get('title')
        # content = form.cleaned_data.get('content')
        
        # article_obj = Article.objects.create(title=title, content=content)
        # context['object']= article_object
        # context['created']= True
    return render(request, "article/create.html", context=context)



def article_search_view(request):
    query = request.GET.get('q')    
    qs = Article.objects.all()

    if query is not None:
        qs =  Article.objects.search(query=query)
    context = {
        "object_list": qs 
    }

    return render(request, "article/search.html", context=context)