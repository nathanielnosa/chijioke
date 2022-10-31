from django.shortcuts import render
from .models import africanews
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def index(request):
    africa = africanews.objects.order_by('-date_posted').filter(published=True).filter(flag=False)

    paginator = Paginator(africa, 12)
    page = request.GET.get('page')
    paged_africa = paginator.get_page(page)
    
    context = {
        'africa': paged_africa
    }

    return render(request,'africanews/africanews.html',context)  


def africanewsdetail(request,slug_id):
    thelocal =africanews.objects.filter(slug=slug_id).first()

    context= {
      'post':thelocal,
  }
    return render(request,'africanews/africa.html',context)