from locust import TaskSet, task, between
from data.zeus import STATIC_DATA


class Behavior(TaskSet):
    @task(1)
    def index(self):
        # Home
        for i in range(len(STATIC_DATA["home"])):
            self.client.get(STATIC_DATA["home"][i])

    @task(1)
    def membership(self):
        # Membership
        for i in range(len(STATIC_DATA["membership"])):
            self.client.get(STATIC_DATA["membership"][i])

    @task(1)
    def shop(self):
        # Shop
        for i in range(len(STATIC_DATA["shop"])):
            self.client.get(STATIC_DATA["shop"][i])

    @task(1)
    def pdp(self):
        # PDP
        for i in range(len(STATIC_DATA["PDP"])):
            self.client.get(STATIC_DATA["PDP"][i])
