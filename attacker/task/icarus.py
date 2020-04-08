from locust import TaskSet, task, between
from data.icarus import STATIC_DATA


class Behavior(TaskSet):
    @task(1)
    def index(self):
        # Home
        for i in range(len(STATIC_DATA["home"])):
            self.client.get(STATIC_DATA["home"][i])

    @task(1)
    def promo(self):
        # Promo
        for i in range(len(STATIC_DATA["promo"])):
            self.client.get(STATIC_DATA["promo"][i])

    @task(1)
    def manage_product(self):
        # Manage Product
        for i in range(len(STATIC_DATA["manage_product"])):
            self.client.get(STATIC_DATA["manage_product"][i])

    @task(1)
    def statistic_overview(self):
        # Statistic Overview
        for i in range(len(STATIC_DATA["statistic_overview"])):
            self.client.get(STATIC_DATA["statistic_overview"][i])

    @task(1)
    def my_campaign(self):
        # My Campaign
        for i in range(len(STATIC_DATA["my_campaign"])):
            self.client.get(STATIC_DATA["my_campaign"][i])

    @task(1)
    def manage_campaign(self):
        # Manage Campaign List
        for i in range(len(STATIC_DATA["manage_campaign"])):
            self.client.get(STATIC_DATA["manage_campaign"][i])

    @task(1)
    def manage_campaign_detail(self):
        # Manage Campaign Detail
        for i in range(len(STATIC_DATA["manage_campaign_detail"])):
            self.client.get(STATIC_DATA["manage_campaign_detail"][i])
