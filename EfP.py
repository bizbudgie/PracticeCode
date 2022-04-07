import json

def check_products(products, term):
    for item in products:
        if item['name'].lower() == term.lower():
            return item
    return None


def add_item(products, add_req, search_term):
    if add_req.lower == 'yes'.lower() or add_req.lower() == 'y'.lower():
        new_name = search_term
        new_price = input(f'What will the price of {new_name} be?')
        new_quantity = input(f'How many of {new_name} are in the inventory?')
        new_item = {'name': new_name, 'price': new_price, 'quantity': new_quantity}
        products.append(new_item)
        with open('products.json', 'w') as write_file:
            json.dump(dict(products = products), write_file)
    else:
        pass


def product_search():
    looking = True
    with open('products.json', 'r') as read_file:
        products = json.load(read_file)['products']
    # look for item until found
    found = False
    while not found:
        search_term = input('What is the name of the product?\n')
        result = check_products(products, search_term)
        if result is not None:
            print('{0}\n{1}\n{2}\n'.format(result['name'], result['price'], result['quantity']))
            found = True
        else:
            print('Sorry, that product was not found in our inventory')
            add_req = input('Should this item be added to the inventory?')
            add_item(products, add_req, search_term)


def multitable():
    for x in range(0, 13):
        for y in range(0, 13):
            result = x * y
            print(f'{x} x {y} = {result}')


def main():
    #multitable()
    product_search()


if __name__ == '__main__':
    main()