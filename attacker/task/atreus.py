from locust import TaskSet, task, between
from data.atreus import STATIC_DATA


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