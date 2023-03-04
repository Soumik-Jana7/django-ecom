from django.shortcuts import render
from auction.models import AuctionProduct

# Create your views here.
def auction(request):
    
    #print(AuctionProduct.objects.all()[0])
    context = {'products' : AuctionProduct.objects.all()}
    print(context)
    return render(request, 'auction.html', context)

# def auc_product(request):
#     current_url = request.resolver_match.url_name
#     print(current_url)
#     return render(request, 'auc_product.html')

def auc_product(request,myid):
    if(request.method == 'POST'):
        print('got bid request')
        raise_amt = request.POST.get('bid_amt')
        product = AuctionProduct.objects.filter(id=myid)
        
    else:
        product = AuctionProduct.objects.filter(id=myid)
        return render(request,'auc_product.html',{'product':product[0]})