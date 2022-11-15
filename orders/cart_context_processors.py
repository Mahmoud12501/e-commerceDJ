from .models import Cart

def get_or_creat_cart(request):
    if request.user.is_authenticated:
        cart,created=Cart.objects.get_or_create(user=request.user)
        print(cart)
        return {'cart_data':cart}
    else:
     return{}