"""
This module represents the Marketplace.

Computer Systems Architecture Course
Assignment 1
March 2020
"""
class Marketplace:
    """
    Class that represents the Marketplace. It's the central part of the implementation.
    The producers and consumers use its methods concurrently.
    """
    def __init__(self, queue_size_per_producer):
        """
        Constructor

        :type queue_size_per_producer: Int
        :param queue_size_per_producer: the maximum size of a queue associated with each producer
        """
        #prod_dict este dictionarul pt producatori si produsele lor,cons_dict este pt cosurile de
        #cumparaturi si produsele din ele si id_removed_prod este dictionarul pentru a tine minte id
        #producatorului pt produsele  adaugate intr-un cos pentru a stii in caz de remove unde sa
        #adaug produsul respectiv

        self.queue_size_per_producer = queue_size_per_producer
        self.prod_dict = dict()
        self.cons_dict = dict()
        self.id_removed_prod = dict()

        #liste din care aleg id pentru producatori si cosurile de cumparaturi

        self.idprod = list(range(0, 1000))
        self.idcons = list(range(0, 1000))

    def register_producer(self):
        """
        Returns an id for the producer that calls this.
        """
        id_p = self.idprod[1]
        self.idprod.remove(id_p)
        self.prod_dict[str(id_p)] = []
        return str(id_p)

    def publish(self, producer_id, product):
        """
        Adds the product provided by the producer to the marketplace

        :type producer_id: String
        :param producer_id: producer id

        :type product: Product
        :param product: the Product that will be published in the Marketplace

        :returns True or False. If the caller receives False, it should wait and then try again.
        """
        if self.queue_size_per_producer > len(self.prod_dict[producer_id]):
            self.prod_dict[producer_id].append(product)
            return True
        return False

    def new_cart(self):
        """
        Creates a new cart for the consumer

        :returns an int representing the cart_id
        """
        id_c = self.idcons[1]
        self.idcons.remove(id_c)
        self.cons_dict[int(id_c)] = []
        return int(id_c)

    def add_to_cart(self, cart_id, product):
        """
        Adds a product to the given cart. The method returns

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to add to cart

        :returns True or False. If the caller receives False, it should wait and then try again
        """
        for dict_idlist, dictprodlist in self.prod_dict.items():
            if product in dictprodlist:
                dictprodlist.remove(product)
                self.id_removed_prod[cart_id] = dict_idlist
                self.cons_dict[cart_id].append(product)
                return True
        return False

    def remove_from_cart(self, cart_id, product):
        """
        Removes a product from cart.

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to remove from cart
        """
        if product in self.cons_dict[cart_id]:
            self.cons_dict[cart_id].remove(product)#adaug in cos
            self.prod_dict[self.id_removed_prod[cart_id]].append(product)#sterg din prod

    def place_order(self, cart_id):
        """
        Return a list with all the products in the cart.

        :type cart_id: Int
        :param cart_id: id cart
        """
        return self.cons_dict[cart_id]
