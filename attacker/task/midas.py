from locust import TaskSet, task
from data.midas import STATIC_DATA


class Behavior(TaskSet):
    @task(1)
    def index(self):
        len_data = len(STATIC_DATA["manage_recomm"])
        if len_data == 0:
            pass

        for i in range(len_data):
            self.client.get(STATIC_DATA["manage_recomm"][i])
    
    @task(1)
    def claim(self):
        len_data = len(STATIC_DATA["claim"])
        if len_data == 0:
            pass

        for i in range(len_data):
            self.client.get(STATIC_DATA["claim"][i])
    
    @task(1)
    def claim_empty(self):
        len_data = len(STATIC_DATA["claim_empty"])
        if len_data == 0:
            pass

        for i in range(len_data):
            self.client.get(STATIC_DATA["claim_empty"][i])

    @task(1)
    def product(self):
        len_data = len(STATIC_DATA["product_create"])
        if len_data == 0:
            pass

        for i in range(len_data):
            self.client.get(STATIC_DATA["product_create"][i])

    @task(1)
    def invalid(self):
        len_data = len(STATIC_DATA["invalid"])
        if len_data == 0:
            pass

        # Invalid
        for i in range(len_data):
            self.client.get(STATIC_DATA["invalid"][i])

