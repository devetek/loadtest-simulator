from locust import HttpLocust, TaskSet, task, between
import json

# Sorry still struct the data, distruct by family, will continue tomorrow
class UserBehavior(TaskSet):
    @task(2)
    def index(self):
        # Home
        # TODO: collecting data random from data/__init__
        self.client.get("/")

    @task(1)
    def about(self):
        # PDP
        # TODO: collecting data random from data/__init__
        self.client.get("/terpusat/demo-terpusat")
 
 
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5, 15)