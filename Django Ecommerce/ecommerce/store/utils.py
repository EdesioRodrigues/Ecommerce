import json
from .models import *

# função para verificar o carrinho
def cookieCart(request):
        try:
            cart = json.loads(request.COOKIES['cart'])

        except:
            cart = {}
            print('Carrinho:', cart)

        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']

        for i in cart:
            try:
                cartItems += cart[i]['quantity']

                # busca o produto pelo id e calcula o total do item
                product = Product.objects.get(id = i)
                total = (product.price * cart[i]['quantity'])

                # soma o total e a quantidade de itens
                order['get_cart_total'] += total
                order['get_cart_items'] += cart[i]['quantity']

                # representa o item do carrinho
                item = {
                    'product':{
                        'id':product.id,
                        'name':product.name,
                        'price':product.price,
                        'imageURL':product.imageURL
                    },
                'quantity':cart[i]['quantity'],
                'get_total':total

                }
                # adiciona os itens a lista
                items.append(item)

                if product.digital == False:
                    order['shipping'] = True
            except:
                pass
        return {'cartItems':cartItems, 'order':order, 'items':items}

# dois tipos de carrinho, um para usuários autenticados e outro para visita, banco de dados e cookies
def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    return {'cartItems':cartItems, 'order':order, 'items':items}


def guestOrder(request, data):
    return ''
