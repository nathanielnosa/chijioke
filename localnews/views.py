from django.shortcuts import render
from .models import localnews
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.


def index(request):
    local = localnews.objects.order_by('-date_posted').filter(published=True).filter(flag=False)

    paginator = Paginator(local, 12)
    page = request.GET.get('page')
    paged_local = paginator.get_page(page)
    
    context = {
        'local': paged_local
    }

    return render(request,'localnews/localnews.html',context)  


def localnewsdetail(request,slug_id):
    thelocal =localnews.objects.filter(slug=slug_id).first()

    context= {
      'post':thelocal,
  }
    return render(request,'localnews/local.html',context)
          