def shopping_cart(*args):
    meals_count = {
        'Soup': 3,
        'Pizza': 4,
        'Dessert': 2,
    }
    meals = {
        'Soup': [],
        'Pizza': [],
        'Dessert': [],
    }

    for info in args:
        if info == 'Stop':
            break

        meal = info[0]
        product = info[1]

        if product not in meals[meal]:
            if len(meals[meal]) < meals_count[meal]:
                meals[meal].append(product)

    output = list()
    if not meals['Dessert'] and not meals['Pizza'] and not meals['Soup']:
        output.append(f'No products in the cart!')
    else:
        for key, value in sorted(meals.items(), key=lambda x: (-len(x[1]), x[0])):
            output.append(f'{key}:')
            if value:
                for item in sorted(value):
                    output.append(f' - {item}')

    return '\n'.join(output)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
    )
)
print(40 * '-')
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
    )
)
print(40 * '-')
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
    )
)
