"""MasterSchool Best Buy sprint assessment:
main implements the user interface for the best_buy shop instance, executing
logic as well as the references to the Store and Product classes.
"""

import sys
from products import Product
from store import Store


def call_dispatcher(choice):
    """
    Return the function associated with the selected menu option.
    """
    menu = {
        "1": list_products,
        "2": show_total_amounts,
        "3": make_order,
        "4": quit_programm
    }
    return menu.get(choice)


def start():
    """
    Display the main menu and return the user's choice and valid options.
    """
    print(
""" 
   Store Menu
   -----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit """
    )
    choice = input("Please choose a number: ")
    return choice, ["1", "2", "3", "4"]


def list_products(shop_instance):
    """
    Print all active products in the store with index numbers.
    """
    print("______")
    for index, product in enumerate(shop_instance.get_all_products()):
        print(f"{index + 1}. ", end="")
        product.show()
    print("______")


def show_total_amounts(shop_instance):
    """
    Print the total quantity of all products in the store.
    """
    total = shop_instance.get_total_quantity()
    print(f"Total of {total} items in store")


def get_validated_tuple(product_list, selected_product, selected_quantity):
    """
    Validate product and quantity input and return a tuple (index, quantity).

    Returns:
        False: if the user entered empty input (signals end of order).
        None: if the input is invalid.
        (int, int): valid product index and quantity.
    """
    # empty input ends the order process
    if not selected_product or not selected_quantity:
        return False
    # both values must be integer like str-numbers
    if not selected_product.isdigit() or not selected_quantity.isdigit():
        return None

    selected_product_int = int(selected_product)
    selected_quantity_int = int(selected_quantity)

    # product number must be existing list index
    if not 0 < selected_product_int <= (len(product_list)):
        return None
    # quantity must be positive
    if selected_quantity_int <= 0:
        return None

    return selected_product_int - 1, selected_quantity_int


def make_order(shop_instance):
    """
    Interactively collect product selections and quantities from the user,
    validate them, and process the final order through the store.
    """
    list_products(shop_instance)
    product_list = shop_instance.get_all_products()
    print("When you want to finish order, enter empty text.")

    selection = []

    while True:
        selected_product = input("Which product # do you want? ")
        selected_quantity = input("What amount do you want? ")
        selection_tuple = get_validated_tuple(
            product_list,
            selected_product,
            selected_quantity
        )
        if selection_tuple is None:
            print("Error adding product!")
        elif selection_tuple is False:
            break
        else:
            selection.append(selection_tuple)

    if selection:
        shopping_basket = []
        for index, quantity in selection:
            shopping_basket.append((product_list[index], quantity))
        return shop_instance.order(shopping_basket)


def print_result(result):
    """
    Print the final order result if a purchase was completed.
    """
    if result is not None:
        print("*" * 8)
        print(f"Order made! Total payment: ${result}")


def quit_programm(_):
    """
    Exit the program immediately.
    """
    sys.exit()


def define_product_list():
    """
    Create and return the initial list of predefined Product instances.
    """
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    pixel = Product("Google Pixel 7", price=500, quantity=250)
    return [mac, bose, pixel]


def create_store():
    """
    Create and return a Store instance initialized with predefined products.
    """
    product_list = define_product_list()
    return Store(product_list)


def main():
    """
    Run the main program loop, handle menu navigation, and dispatch actions.
    """
    # products defined in define_product_list and referred to in create_store()
    best_buy = create_store()

    while True:
        choice, list_of_options = start()
        if choice in list_of_options:
            try:
                result = call_dispatcher(choice)(best_buy)
                print_result(result)
            except Exception as error:
                print(error)
        else:
            print("Error with choice, try again!")


if __name__ == "__main__":
    main()
