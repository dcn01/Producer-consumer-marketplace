"""
This module represents the Consumer.

Computer Systems Architecture Course
Assignment 1
March 2020
"""

from threading import Thread
import time

class Consumer(Thread):
    """
    Class that represents a consumer.
    """

    def __init__(self, carts, marketplace, retry_wait_time, **kwargs):
        """
        Constructor.

        :type carts: List
        :param carts: a list of add and remove operations

        :type marketplace: Marketplace
        :param marketplace: a reference to the marketplace

        :type retry_wait_time: Time
        :param retry_wait_time: the number of seconds that a producer must wait
        until the Marketplace becomes available

        :type kwargs:
        :param kwargs: other arguments that are passed to the Thread's __init__()
        """
        Thread.__init__(self, **kwargs)
        self.name = kwargs['name'] #id cons
        self.carts = carts
        self.marketplace = marketplace
        self.retry_wait_time = retry_wait_time

    def run(self):

        #generez un id unic pentru fiecare cos de cumparaturi

        for cart in self.carts:
            id_cart = self.marketplace.new_cart()

        #parcurg lista de operatii, adaug/scot obiecte din cos
        #daca nu merge sa adaug in cos, astept cat trebuie si incerc din nou

            for prod in cart:
                for _ in range(prod['quantity']):
                    if prod['type'] == "add":
                        not_done = self.marketplace.add_to_cart(id_cart, prod['product'])
                        while not not_done:
                            not_done = self.marketplace.add_to_cart(id_cart, prod['product'])
                            time.sleep(self.retry_wait_time)
                    else:
                        self.marketplace.remove_from_cart(id_cart, prod['product'])

            #public fiecare produs ramas in cos

            final_list = self.marketplace.place_order(id_cart)
            for prod in final_list:
                print (str(self.name) + " " + "bought" + " " +  str(prod))
