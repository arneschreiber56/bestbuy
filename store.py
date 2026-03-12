class Store:
    """Represents a store that manages a collection of product objects.
    Provides methods for adding and removing products, retrieving
    quantities, listing active products, and processing orders."""

    def __init__(self, products):
        """
        Initialize the store with an initial list of product instances.
        """
        self.products = products


    def add_product(self, shop_product):
        """
        Add a product instance to the store if it is not already listed.
        """
        if shop_product not in self.products:
            self.products.append(shop_product)
        else:
            raise Exception("Entry already listed as a product!")


    def remove_product(self, shop_product):
        """
        Remove a product instance from the store if it exists.
        """
        if shop_product in self.products:
            self.products.remove(shop_product)
        else:
            raise Exception("Your entry is not listed as an existing product!")


    def get_total_quantity(self):
        """
        Return the total quantity of all products in the store.
        """
        total = 0
        for shop_product in self.products:
            total += shop_product.get_quantity()

        return total


    def get_all_products(self):
        """
        Return a list of all active product instances in the store.
        """
        active_products = []
        for shop_product in self.products:
            if shop_product.is_active():
                active_products.append(shop_product)
        return active_products

    def order(self, shopping_list):
        """
        Process a list of (product, quantity) tuples and return the total price.
        """
        total_price = 0
        for instance, quantity in shopping_list:
            total_price += instance.buy(quantity)
        return total_price






