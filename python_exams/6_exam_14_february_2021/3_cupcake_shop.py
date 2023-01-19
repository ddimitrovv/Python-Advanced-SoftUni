# Maria is opening a cupcake shop. Help her manage her inventory to improve stock availability.
#
# Write a function called stock_availability which receives:
#     • an inventory list of boxes with different kinds of cupcake flavours
#     • "delivery" or "sell" as second parameter
#     • there might or might not be any other parameters – numbers or strings at the end
#
# In case of "delivery"  to the shop was delivered new boxes with different kinds of cupcakes:
#     • You should add the boxes at the end of the inventory list
#     • There will be always at least one box delivered
# In case of "sell" Maria has a client, and she is selling different boxes with cupcakes:
#     • If there is a number as another parameter, it means that Maria has sold that many boxes with cupcakes,
#       and you should remove them from the beginning of the inventory list
#     • If there is/are string/s as another parameter/s, it means that Maria has sold ALL cupcake boxes
#       of the ordered flavour/s. Beware that not everything the buyer has ordered might be in stock,
#       so you should check if the order is valid.
#     • If there are no other parameters, it means that Maria has sold only the first box of cupcakes,
#       and you should remove  it of the inventory list
# For more clarifications, see the examples below.
# Input
#     • There will be no input
#     • Parameters will be passed to your function
# Output
#     • The function should return a new inventory list
#     • All commands will be valid

from collections import deque


def sell_cupcakes(stock, products):
    if products:
        try:
            for i in range(products[0]):
                stock.popleft()
        except TypeError:
            stock = [x for x in stock if x not in products]
    else:
        stock.popleft()
    return stock


def delivery_products(stock, products):
    for item in products:
        stock.append(item)
    return stock


def stock_availability(inventory, condition, *args):
    order = [x for x in args]

    on_stock = deque(inventory)
    if condition == 'sell':
        on_stock = sell_cupcakes(on_stock, order)
    if condition == 'delivery':
        on_stock = delivery_products(on_stock, order)

    return list(on_stock)


print(
    stock_availability(
        ["choco", "vanilla", "banana"], "delivery", "caramel", "berry"
    )
)

print(
    stock_availability(
        ["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"
      )
)

print(
    stock_availability(
        ["chocolate", "vanilla", "banana"], "sell"
    )
)

print(
    stock_availability(
        ["chocolate", "vanilla", "banana"],
        "sell",
        3
    )
)

print(
    stock_availability(
        ["chocolate", "chocolate", "banana"],
        "sell",
        "chocolate"
    )
)

print(
    stock_availability(
        ["cookie", "chocolate", "banana"],
        "sell",
        "chocolate"
    )
)

print(
    stock_availability(
        ["chocolate", "vanilla", "banana"],
        "sell",
        "cookie"
    )
)
