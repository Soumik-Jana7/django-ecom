from django.shortcuts import render
from auction.models import AuctionProduct
from auction.models import User
import time
import datetime

# from django_socketio import events

# Create your views here.
def auction(request):
    
    #print(AuctionProduct.objects.all()[0])
    products = AuctionProduct.objects.all()
    for val in products:
        print(val)
        end_time = val.start_time + datetime.timedelta(hours = val.duration_hours, minutes=val.duration_mins)
        print(val.start_time)
        print(end_time)
        val.end_time = end_time
        end_naive = val.end_time.replace(tzinfo=None)
        curr_time = datetime.datetime.now()
        # if(curr_time < end_naive):
        #     val.status = 'open'
        # else:
        #     val.status = 'closed'
        val.save()
    context = {'products' : AuctionProduct.objects.all()}
    print(context)
    return render(request, 'auction.html', context)


def auc_product(request,myid):
    if(request.method == 'POST'):
        curr_time = datetime.datetime.now()
        print('got bid request')
        useremail = request.POST.get('useremail')
        user = User.objects.get(user_email = useremail)
        print(user.user_email)
        raise_amt = int(request.POST.get('bid_amt'))
        product = AuctionProduct.objects.get(id=myid)
        print(curr_time)
        end_naive = product.end_time.replace(tzinfo=None)
        print(end_naive)
        if(curr_time < end_naive):

            if(raise_amt > product.prod_price):
                product.prod_price = raise_amt
                product.save()
            else:
                return render(request, 'auc_product.html', {'product':product, 'bid' : 'fail'})
        else:
            return render(request, 'auc_product.html', {'product':product, 'bid' : 'tle'})

    product = AuctionProduct.objects.filter(id=myid)
    
    return render(request,'auc_product.html',{'product':product[0], 'bid' : 'success'})

def register(request):
    if(request.method == 'POST'):
        print('got user registration')
        username = request.POST.get('name')
        useremail = request.POST.get('email')
        userpass = request.POST.get('password')
        #print(datetime.datetime.now().time())
        user = User(user_name = username, user_email = useremail, password = userpass)
        user.save()
        return render(request, 'index.html')

    return render(request, 'register.html')


