from locust import TaskSet, task
from data.gossinc import STATIC_DATA


class Behavior(TaskSet):
    @task(1)
    def index(self):
        len_data = len(STATIC_DATA["assets"])
        if len_data == 0:
            pass

        for i in range(len_data):
            self.client.get(STATIC_DATA["assets"][i], headers={"referer":  "https://www.tokopedia.com/payment/withdrawal"})
