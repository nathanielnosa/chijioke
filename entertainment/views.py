from django.shortcuts import render
from .models import entertainment
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def index(request):
    enternews = entertainment.objects.order_by('-date_posted').filter(published=True).filter(flag=False)

    paginator = Paginator(enternews, 12)
    page = request.GET.get('page')
    paged_enternews = paginator.get_page(page)
    
    context = {
        'enternews': paged_enternews
    }

    return render(request,'entertainment/entertainment.html',context)  


def entertainmentdetail(request,slug_id):
    thelocal =entertainment.objects.filter(slug=slug_id).first()

    context= {
      'post':thelocal,
  }
    return render(request,'entertainment/enternews.html',context)    