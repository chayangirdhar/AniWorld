from django.shortcuts import render
from Core.models import AnimeDatabase
# For paginating the data
from django.core.paginator import Paginator ,EmptyPage, PageNotAnInteger

# Create your views here.

def search(request):
    if request.method == 'GET' and 'q' in request.GET:
        q = request.GET.get('q', None)
        if q is not None:
            search = q
            querry = AnimeDatabase.objects.filter(titles__icontains=search)
            p = Paginator(querry,5)
            page = request.GET.get('page',1)
            try:
              data = p.page(page)
            except PageNotAnInteger:
                data = p.page(1)
            except EmptyPage:
                data = p.page(p.num_pages)           
            website_data = {
                'title':'Search Result',
                'datas' : data,
                "q" : q,
            }
            return render(request,'SearchAnime/search.html',website_data)
    else:
        website_data = {
            'title' : 'Search',
        }
        return render(request,'SearchAnime/search.html',website_data)


def detail(request,pk):
    querry = AnimeDatabase.objects.filter(id = pk)
    embed = None
    for i in querry:
        data = i
    if data.trailer:
        embed = data.trailer.split("=")[-1]
    website_data = {
        'data': data,
        'embed': embed
    }
    return render(request,'SearchAnime/detail.html',website_data)
