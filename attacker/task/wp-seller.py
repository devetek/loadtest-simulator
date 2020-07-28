from locust import TaskSet, task
from data.wpseller import STATIC_DATA


class Behavior(TaskSet):
    @task(1)
    def index(self):
        len_data = len(STATIC_DATA["home"])
        if len_data == 0:
            pass

        # home
        for i in range(len_data):
            self.client.get(STATIC_DATA["home"][i])

    @task(1)
    def articles(self):
        len_data = len(STATIC_DATA["articles"])
        if len_data == 0:
            pass

        # articles
        for i in range(len_data):
            self.client.get(STATIC_DATA["articles"][i])

    @task(1)
    def article_detail(self):
        len_data = len(STATIC_DATA["article_detail"])
        if len_data == 0:
            pass

        # article_detail
        for i in range(len_data):
            self.client.get(STATIC_DATA["article_detail"][i])

    @task(1)
    def admin_main(self):
        len_data = len(STATIC_DATA["admin_main"])
        if len_data == 0:
            pass

        # admin_main
        for i in range(len_data):
            self.client.get(STATIC_DATA["admin_main"][i])

    @task(1)
    def admin_hide(self):
        len_data = len(STATIC_DATA["admin_hide"])
        if len_data == 0:
            pass

        # admin_hide
        for i in range(len_data):
            self.client.get(STATIC_DATA["admin_hide"][i])

    @task(1)
    def admin_login(self):
        len_data = len(STATIC_DATA["admin_login"])
        if len_data == 0:
            pass

        # admin_login
        for i in range(len_data):
            self.client.get(STATIC_DATA["admin_login"][i])

    @task(1)
    def wp_content(self):
        len_data = len(STATIC_DATA["wp_content"])
        if len_data == 0:
            pass

        # wp_content
        for i in range(len_data):
            self.client.get(STATIC_DATA["wp_content"][i])

    @task(1)
    def wp_includes(self):
        len_data = len(STATIC_DATA["wp_includes"])
        if len_data == 0:
            pass

        # wp_includes
        for i in range(len_data):
            self.client.get(STATIC_DATA["wp_includes"][i])

    @task(1)
    def wp_json(self):
        len_data = len(STATIC_DATA["wp_json"])
        if len_data == 0:
            pass

        # wp_json
        for i in range(len_data):
            self.client.get(STATIC_DATA["wp_json"][i])

    @task(1)
    def microsite_event(self):
        len_data = len(STATIC_DATA["microsite_event"])
        if len_data == 0:
            pass

        # microsite_event
        for i in range(len_data):
            self.client.get(STATIC_DATA["microsite_event"][i])

    @task(1)
    def microsite_kembangkan_usaha(self):
        len_data = len(STATIC_DATA["microsite_kembangkan_usaha"])
        if len_data == 0:
            pass

        # microsite_kembangkan_usaha
        for i in range(len_data):
            self.client.get(STATIC_DATA["microsite_kembangkan_usaha"][i])

    @task(1)
    def microsite_mulai_berjualan(self):
        len_data = len(STATIC_DATA["microsite_mulai_berjualan"])
        if len_data == 0:
            pass

        # microsite_mulai_berjualan
        for i in range(len_data):
            self.client.get(STATIC_DATA["microsite_mulai_berjualan"][i])

    @task(1)
    def microsite_layanan(self):
        len_data = len(STATIC_DATA["microsite_layanan"])
        if len_data == 0:
            pass

        # microsite_layanan
        for i in range(len_data):
            self.client.get(STATIC_DATA["microsite_layanan"][i])

    @task(1)
    def microsite_official_store(self):
        len_data = len(STATIC_DATA["microsite_official_store"])
        if len_data == 0:
            pass

        # microsite_official_store
        for i in range(len_data):
            self.client.get(STATIC_DATA["microsite_official_store"][i])

    @task(1)
    def microsite_order_prioritas(self):
        len_data = len(STATIC_DATA["microsite_order_prioritas"])
        if len_data == 0:
            pass

        # microsite_order_prioritas
        for i in range(len_data):
            self.client.get(STATIC_DATA["microsite_order_prioritas"][i])

    @task(1)
    def microsite_power_merchant(self):
        len_data = len(STATIC_DATA["microsite_power_merchant"])
        if len_data == 0:
            pass

        # microsite_power_merchant
        for i in range(len_data):
            self.client.get(STATIC_DATA["microsite_power_merchant"][i])

    @task(1)
    def microsite_tingkatkan_penjualan(self):
        len_data = len(STATIC_DATA["microsite_tingkatkan_penjualan"])
        if len_data == 0:
            pass

        # microsite_tingkatkan_penjualan
        for i in range(len_data):
            self.client.get(STATIC_DATA["microsite_tingkatkan_penjualan"][i])

    @task(1)
    def microsite_topads(self):
        len_data = len(STATIC_DATA["microsite_topads"])
        if len_data == 0:
            pass

        # microsite_topads
        for i in range(len_data):
            self.client.get(STATIC_DATA["microsite_topads"][i])

    @task(1)
    def microsite_topbot(self):
        len_data = len(STATIC_DATA["microsite_topbot"])
        if len_data == 0:
            pass

        # microsite_topbot
        for i in range(len_data):
            self.client.get(STATIC_DATA["microsite_topbot"][i])

    @task(1)
    def other(self):
        len_data = len(STATIC_DATA["else"])
        if len_data == 0:
            pass

        # else
        for i in range(len_data):
            self.client.get(STATIC_DATA["else"][i])
