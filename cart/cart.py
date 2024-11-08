from store.models import Product

class Cart():

    def __init__(self, request):
        self.session = request.session

        # Get the current session key if it exists
        cart = self.session.get('session_key')

        # if session key doesnt exist, create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}


        # make sure cart is available on all pages of site
        self.cart = cart

    
    def add(self, product, quantity):  
        
        product_id = str(product.id)
        product_qty = str(quantity)
        #product_size = str(size)
        # Logic
        if product_id in self.cart:
            pass
        else:
            #self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)
            #self.cart[product_id] = int(product_size)

        self.session.modified = True


    def __len__(self):
        return len(self.cart)


    
    def get_prods(self):
        # get ids from cart
        product_ids = self.cart.keys()

        #use ids to look up products in DB model
        products = Product.objects.filter(id__in=product_ids)

        return products
    
    def get_quants(self):
        quantities = self.cart

        return quantities
    
    """def get_size(self):
        size = self.cart

        return size"""
