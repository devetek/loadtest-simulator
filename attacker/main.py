from locust import HttpLocust, TaskSet, task, between
import json

class UserBehavior(TaskSet):
    @task(2)
    def index(self):
        # Home
        # TODO: collecting data random from data/__init__
        self.client.get("/")

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