from locust import TaskSet, task
from data.ares import STATIC_DATA


class Behavior(TaskSet):
    @task(1)
    def index(self):
        len_data = len(STATIC_DATA["home"])
        if len_data == 0:
            pass

        # Discovery
        for i in range(len_data):
            self.client.get(STATIC_DATA["home"][i])
    
    @task(1)
    def search(self):
        len_data = len(STATIC_DATA["home_args"])
        if len_data == 0:
            pass

        # Discovery Category
        for i in range(len_data):
            self.client.get(STATIC_DATA["home_args"][i])

    @task(1)
    def shop(self):
        len_data = len(STATIC_DATA["invalid"])
        if len_data == 0:
            pass

        # Invalid
        for i in range(len_data):
            self.client.get(STATIC_DATA["invalid"][i])

