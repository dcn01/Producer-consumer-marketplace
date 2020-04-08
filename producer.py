"""
This module represents the Producer.

Computer Systems Architecture Course
Assignment 1
March 2020
"""

from threading import Thread
import time

class Producer(Thread):
    """
    Class that represents a producer.
    """

    def __init__(self, products, marketplace, republish_wait_time, **kwargs):
        """
        Constructor.

        @type products: List()
        @param products: a list of products that the producer will produce

        @type marketplace: Marketplace
        @param marketplace: a reference to the marketplace

        @type republish_wait_time: Time
        @param republish_wait_time: the number of seconds that a producer must
        wait until the marketplace becomes available

        @type kwargs:
        @param kwargs: other arguments that are passed to the Thread's __init__()
        """
        Thread.__init__(self, **kwargs)
        self.products = products
        self.marketplace = marketplace
        self.republish_wait_time = republish_wait_time

    def run(self):

        #primesc un id unic pt fiecare producator

        id_prod = self.marketplace.register_producer()
        while True:

        #pentru fiecare produs din lista, parcurg cantitatile si il public
        #daca nu pot publica, astept cat timp trebuie

            for prod in self.products:
                for _ in range(prod[1]):
                    isnt_done = False
                    while not isnt_done:
                        isnt_done = self.marketplace.publish(id_prod, prod[0])
                        if not isnt_done:
                            time.sleep(self.republish_wait_time)
                        time.sleep(prod[2])
