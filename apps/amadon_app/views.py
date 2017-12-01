from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'amadon_app/index.html')

def process(request):
    if request.method == "POST":
        if not 'quantityOrder' in request.session:
                request.session['quantityOrder'] = 0 # set to 0 for starting point
        if not 'priceOrder' in request.session:
                request.session['priceOrder'] = 0 # set to 0 for starting point.
        # if request.method == "POST":
        #     if request.POST['product_id'] == 'item1': #'product_id' is the name of the input field in HTML. 
        #         price = 20 # if statement price set to 20
        #         #POST for 'product_id' is for everything with in the <form>. POST is input that within the <select>
                
        #     elif request.POST['product_id'] == 'item2': #'item2' is the value in the input field in HTML
        #         price = 30 # if else statement above price set to 30
        #     elif request.POST['product_id'] == 'item3':
        #         price = 5 # if else statement above price set to 5

        
       
        price = int(request.POST['quantity']) * int(request.POST['ProductPrice']) 
        request.session['ProductPrice'] = price
            #set session 'checkoutPrice'(later will be total price currently nothing) = to which ever 'product_id' * price
        request.session['quantityOrder'] += int(request.POST['quantity'])
            #set session 'quantityOrder' to add to keep track of all order quantity.
        request.session['priceOrder'] += price
            # set priceOrder to add the total 'price' to show on 'checkoutPrice'
        return redirect('/checkout')

def checkout(request):
    return render(request, 'amadon_app/checkout.html')

def back(request):
    return redirect('/')