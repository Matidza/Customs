from store.models import Product, Profile

class Cart():

    def __init__(self, request):
        self.session = request.session
        # Get request
        self.request = request
        # Get the current session key if it exists
        cart = self.session.get('session_key')

        # if session key doesnt exist, create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}


        # make sure cart is available on all pages of site
        self.cart = cart
    def db_add(self, product, quantity):
        product_id = str(product)
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
        # del with loggedin User
        if self.request.user.is_authenticated:
            # Get current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # Convert  {'3':1, '5':2} to {"3": 1, "5":2}
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")

            # lets save carty to Model
            current_user.update(old_cart=str(carty))
    # Add a product to the cart 
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
        # del with loggedin User
        if self.request.user.is_authenticated:
            # Get current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # Convert  {'3':1, '5':2} to {"3": 1, "5":2}
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")

            # lets save carty to Model
            current_user.update(old_cart=str(carty))

    def __len__(self):
        return len(self.cart)


    
    def get_prods(self):
        # get ids from cart
        product_ids = self.cart.keys()

        # use ids to look up products in DB model
        products = Product.objects.filter(id__in=product_ids)

        return products
    
    def get_quants(self):
        quantities = self.cart

        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = str(quantity)

        # {}
        # Get the cart
        ourcart = self.cart
        # updxate Dict
        ourcart[product_id] = product_qty

        self.session.modified = True
        this = self.cart
        
        if self.request.user.is_authenticated:
            # Get current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # Convert  {'3':1, '5':2} to {"3": 1, "5":2}
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")

            # lets save carty to Model
            current_user.update(old_cart=str(carty))
        return this
    


    def delete(self, product):
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]
        
        self.session.modified = True
        if self.request.user.is_authenticated:
            # Get current user profile
            current_user = Profile.objects.filter(user__id=self.request.user.id)
            # Convert  {'3':1, '5':2} to {"3": 1, "5":2}
            carty = str(self.cart)
            carty = carty.replace("\'", "\"")

            # lets save carty to Model
            current_user.update(old_cart=str(carty))
    
    """def get_size(self):
        size = self.cart

        return size
    """
    def cart_total(self):
        quantities = self.cart
        # {"4": 3, "5":1}

        # Get product IDS
        product_ids = self.cart.keys()
        # lookup those keys in our products database model
        products = Product.objects.filter(id__in=product_ids)
        
        # Get quantities
        quantities = self.cart
        # Start counting at 0
        total = 0
        
        for key, value in quantities.items():
            # Convert key string into into so we can do math
            key = int(key)
            value = int(value)
            for product in products:
                if product.id == key:
                    if product.is_sale:
                        total = total + (product.sale_price * value)
                    else:
                        total = total + (product.price * value)

        return total