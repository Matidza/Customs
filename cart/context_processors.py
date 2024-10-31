from .cart import Cart

# create context processor so that pur cart can work in all site pages
def cart(request):

    # Reyurn the default data from our cart

    return {'cart': Cart(request)}