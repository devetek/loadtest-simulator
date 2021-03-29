from locust import TaskSet, task
from data.multi import STATIC_DATA


class Behavior(TaskSet):
    @task(1)
    def index(self):
        len_data = len(STATIC_DATA["home"])
        if len_data == 0:
            pass

        # Home
        for i in range(len_data):
            self.client.get(STATIC_DATA["home"][i])
    
    @task(1)
    def search(self):
        len_data = len(STATIC_DATA["search"])
        if len_data == 0:
            pass

        # Search
        for i in range(len_data):
            self.client.get(STATIC_DATA["search"][i])
    
    @task(1)
    def hot(self):
        len_data = len(STATIC_DATA["hot"])
        if len_data == 0:
            pass

        # Hot
        for i in range(len_data):
            self.client.get(STATIC_DATA["hot"][i])

    @task(1)
    def membership(self):
        len_data = len(STATIC_DATA["membership"])
        if len_data == 0:
            pass

        # Membership
        for i in range(len_data):
            self.client.get(STATIC_DATA["membership"][i])

    @task(1)
    def shop(self):
        len_data = len(STATIC_DATA["shop"])
        if len_data == 0:
            pass

        # Shop
        for i in range(len_data):
            self.client.get(STATIC_DATA["shop"][i])

    @task(1)
    def pdp(self):
        len_data = len(STATIC_DATA["PDP"])
        if len_data == 0:
            pass

        # PDP
        for i in range(len_data):
            self.client.get(STATIC_DATA["PDP"][i])
    
    @task(1)
    def other(self):
        len_data = len(STATIC_DATA["else"])
        if len_data == 0:
            pass

        # else
        for i in range(len_data):
            self.client.get(STATIC_DATA["else"][i])
