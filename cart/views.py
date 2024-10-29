from django.shortcuts import render

# Create views for Cart Summary
def cart_summary(request):

    return render(request, 'cart_summary.html', {})


# Adding items to cart
def cart_add(request):

    return render(request, 'cart_add.html', {})

# deleting items from cart
def cart_delete(request):

    return render(request, 'cart_delete.html', {})

# Update items in the cart
def cart_update(request):

    return render(request, 'cart_update.html', {})