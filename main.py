"""MasterSchool sprint assessment:
main should test for now only the Product class"""
from products import Product
from store import Store

def call_dispatcher(choice):
    """sets menu logic as dispatcher pattern"""
    menu = {
        "1": "list_products",
        "2": "show_total_amounts",
        "3": "make_order",
        "4": quit_programm
    }
    return menu.get(choice)


def start():
    "initiates logic by asking for a choice"
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
    return choice


def quit_programm():
    exit()

def main():
    # setup initial stock of inventory
    mac = Product("MacBook Air M2", price=1450, quantity=100),
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    pixel = Product("Google Pixel 7", price=500, quantity=250)
    # create product list for shop instance
    product_list = [mac, bose, pixel]
    # setup shop instance best_buy
    best_buy = Store(product_list)

    choice = start()
    call_dispatcher(choice)


if __name__ == "__main__":
    main()