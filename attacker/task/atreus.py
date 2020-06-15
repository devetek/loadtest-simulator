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
    def hot(self):
        len_data = len(STATIC_DATA["hot"])
        if len_data == 0:
            pass

        # hot
        for i in range(len_data):
            self.client.get(STATIC_DATA["hot"][i])

    @task(1)
    def p(self):
        len_data = len(STATIC_DATA["p"])
        if len_data == 0:
            pass

        # Home
        for i in range(len_data):
            self.client.get(STATIC_DATA["p"][i])

    @task(1)
    def notifcenter(self):
        len_data = len(STATIC_DATA["notif-center"])
        if len_data == 0:
            pass

        # Home
        for i in range(len_data):
            self.client.get(STATIC_DATA["notif-center"][i])

    @task(1)
    def content(self):
        len_data = len(STATIC_DATA["content"])
        if len_data == 0:
            pass

        # Home
        for i in range(len_data):
            self.client.get(STATIC_DATA["content"][i])

    @task(1)
    def myorder(self):
        len_data = len(STATIC_DATA["myorder"])
        if len_data == 0:
            pass

        # Home
        for i in range(len_data):
            self.client.get(STATIC_DATA["myorder"][i])
    
    @task(1)
    def action(self):
        len_data = len(STATIC_DATA["action"])
        if len_data == 0:
            pass

        # Home
        for i in range(len_data):
            self.client.get(STATIC_DATA["action"][i])

    @task(1)
    def onboard(self):
        len_data = len(STATIC_DATA["onboard"])
        if len_data == 0:
            pass

        # Home
        for i in range(len_data):
            self.client.get(STATIC_DATA["onboard"][i])

    @task(1)
    def appcheck(self):
        len_data = len(STATIC_DATA["appcheck"])
        if len_data == 0:
            pass

        # Home
        for i in range(len_data):
            self.client.get(STATIC_DATA["appcheck"][i])

    @task(1)
    def aftersq(self):
        len_data = len(STATIC_DATA["aftersq"])
        if len_data == 0:
            pass

        # Home
        for i in range(len_data):
            self.client.get(STATIC_DATA["aftersq"][i])

    @task(1)
    def broadcastchat(self):
        len_data = len(STATIC_DATA["broadcastchat"])
        if len_data == 0:
            pass

        # Home
        for i in range(len_data):
            self.client.get(STATIC_DATA["broadcastchat"][i])

    @task(1)
    def cart(self):
        len_data = len(STATIC_DATA["cart"])
        if len_data == 0:
            pass

        # Home
        for i in range(len_data):
            self.client.get(STATIC_DATA["cart"][i])

    @task(1)
    def belilangsung(self):
        len_data = len(STATIC_DATA["belilangsung"])
        if len_data == 0:
            pass

        # Home
        for i in range(len_data):
            self.client.get(STATIC_DATA["belilangsung"][i])

    @task(1)
    def catalog(self):
        len_data = len(STATIC_DATA["catalog"])
        if len_data == 0:
            pass

        # Home
        for i in range(len_data):
            self.client.get(STATIC_DATA["catalog"][i])

    @task(1)
    def deposit(self):
        len_data = len(STATIC_DATA["deposit"])
        if len_data == 0:
            pass

        for i in range(len_data):
            self.client.get(STATIC_DATA["deposit"][i])

    @task(1)
    def epharmacy(self):
        len_data = len(STATIC_DATA["epharmacy"])
        if len_data == 0:
            pass

        for i in range(len_data):
            self.client.get(STATIC_DATA["epharmacy"][i])

    @task(1)
    def error(self):
        len_data = len(STATIC_DATA["error"])
        if len_data == 0:
            pass

        for i in range(len_data):
            self.client.get(STATIC_DATA["error"][i])

    @task(1)
    def favorite(self):
        len_data = len(STATIC_DATA["favorite"])
        if len_data == 0:
            pass

        for i in range(len_data):
            self.client.get(STATIC_DATA["favorite"][i])

    @task(1)
    def feed(self):
        len_data = len(STATIC_DATA["feed"])
        if len_data == 0:
            pass

        for i in range(len_data):
            self.client.get(STATIC_DATA["feed"][i])

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