from django.shortcuts import render
from .models import stportnews
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.



def index(request):
    sports = stportnews.objects.order_by('-date_posted').filter(published=True).filter(flag=False)

    paginator = Paginator(sports, 12)
    page = request.GET.get('page')
    paged_sports = paginator.get_page(page)
    
    context = {
        'sports': paged_sports
    }

    return render(request,'sportsnews/sportsnews.html',context) 


def sportsnewsdetail(request,slug_id):
    thesport =stportnews.objects.filter(slug=slug_id).first()

    context= {
      'post':thesport,
  }
    return render(request,'sportsnews/sport.html',context)    