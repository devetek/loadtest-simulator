from locust import TaskSet, task
from data.poseidon import STATIC_DATA


class Behavior(TaskSet):
    @task(1)
    def index(self):
        len_data = len(STATIC_DATA["discovery"])
        if len_data == 0:
            pass

        # Discovery
        for i in range(len_data):
            self.client.get(STATIC_DATA["discovery"][i])
    
    @task(1)
    def search(self):
        len_data = len(STATIC_DATA["discovery_category"])
        if len_data == 0:
            pass

        # Discovery Category
        for i in range(len_data):
            self.client.get(STATIC_DATA["discovery_category"][i])
    
    @task(1)
    def hot(self):
        len_data = len(STATIC_DATA["discovery_jasa"])
        if len_data == 0:
            pass

        # Discovery Jasa
        for i in range(len_data):
            self.client.get(STATIC_DATA["discovery_jasa"][i])

    @task(1)
    def membership(self):
        len_data = len(STATIC_DATA["discovery_tukar_tambah"])
        if len_data == 0:
            pass

        # Discovery Tukar Tambah
        for i in range(len_data):
            self.client.get(STATIC_DATA["discovery_tukar_tambah"][i])

    @task(1)
    def shop(self):
        len_data = len(STATIC_DATA["invalid"])
        if len_data == 0:
            pass

        # Invalid
        for i in range(len_data):
            self.client.get(STATIC_DATA["invalid"][i])

