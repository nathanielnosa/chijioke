from django.shortcuts import render
from .models import worldnews
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.


def index(request):
    world = worldnews.objects.order_by('-date_posted').filter(published=True).filter(flag=False)

    paginator = Paginator(world, 12)
    page = request.GET.get('page')
    paged_world = paginator.get_page(page)
    
    context = {
        'world': paged_world
    }

    return render(request,'worldnews/worldnews.html',context)   



def worldnewsdetail(request,slug_id):
    world = worldnews.objects.filter(slug=slug_id).first()

    context= {
      'post':world,
  }
    return render(request,'worldnews/world.html',context)



def quote(request,slug_id):

    context= {}
    return render(request,'worldnews/quote.html',context)

    # def listing(request, listing_id):
    # listing = get_object_or_404(Listing, pk=listing_id)
    
    # context = {
    #     'listing': listing
    # }

    # return render(request,'listings/listing.html',context)