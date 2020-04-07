from time import sleep
from locust import HttpLocust, TaskSet, task, between
import json
from data import STATIC_DATA

class UserBehavior(TaskSet):
    @task(2)
    def index(self):
        # Home
        # TODO: collecting data random from data/__init__
        self.client.get("/")
    

    @task(1)
    def membership(self):
        # Membership
        for i in range(len(STATIC_DATA["membership"])):
            self.client.get(STATIC_DATA["membership"][i])

    @task(1)
    def shop(self):
        # Shop
        # TODO: collecting data random from data/__init__
        self.client.get("/shop")
    
    @task(1)
    def pdp(self):
        # PDP
        # TODO: collecting data random from data/__init__
        self.client.get("/shop/product")
 
 
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5, 15)