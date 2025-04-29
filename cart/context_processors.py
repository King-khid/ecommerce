from .cart import Cart

#create context processors so our cart can work on all pages
def cart(request):
	# return the default data form our Cart
	return {'cart': Cart(request)}


