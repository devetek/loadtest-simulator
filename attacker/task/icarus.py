from locust import TaskSet, task, between
from data.icarus import STATIC_DATA


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
    def bebas_ongkir(self):
        len_data = len(STATIC_DATA["bebas_ongkir"])
        if len_data == 0:
            pass

        # Bebas Ongkir
        for i in range(len_data):
            self.client.get(STATIC_DATA["bebas_ongkir"][i])
    
    @task(1)
    def broadcast(self):
        len_data = len(STATIC_DATA["broadcast"])
        if len_data == 0:
            pass

        # Broadcast Chat
        for i in range(len_data):
            self.client.get(STATIC_DATA["broadcast"][i])

    @task(1)
    def bulk(self):
        len_data = len(STATIC_DATA["bulk"])
        if len_data == 0:
            pass

        # Bulk Add Edit
        for i in range(len_data):
            self.client.get(STATIC_DATA["bulk"][i])

    @task(1)
    def produk_toko_cabang(self):
        len_data = len(STATIC_DATA["produk_toko_cabang"])
        if len_data == 0:
            pass

        # Tokocabang
        for i in range(len_data):
            self.client.get(STATIC_DATA["produk_toko_cabang"][i])

    @task(1)
    def review(self):
        len_data = len(STATIC_DATA["review"])
        if len_data == 0:
            pass

        # PDP Review
        for i in range(len_data):
            self.client.get(STATIC_DATA["review"][i])
    
    @task(1)
    def shop_info(self):
        len_data = len(STATIC_DATA["shop_info"])
        if len_data == 0:
            pass

        # Shop Info
        for i in range(len_data):
            self.client.get(STATIC_DATA["shop_info"][i])

    @task(1)
    def shop_notes(self):
        len_data = len(STATIC_DATA["shop_notes"])
        if len_data == 0:
            pass

        # Shop Notes
        for i in range(len_data):
            self.client.get(STATIC_DATA["shop_notes"][i])
    
    @task(1)
    def power_merchant(self):
        len_data = len(STATIC_DATA["power_merchant"])
        if len_data == 0:
            pass

        # Power Merchant
        for i in range(len_data):
            self.client.get(STATIC_DATA["power_merchant"][i])

    @task(1)
    def tokopedia_print(self):
        len_data = len(STATIC_DATA["tokopedia_print"])
        if len_data == 0:
            pass

        # Tokopedia Print
        for i in range(len_data):
            self.client.get(STATIC_DATA["tokopedia_print"][i])

    @task(1)
    def voucher_toko(self):
        len_data = len(STATIC_DATA["voucher_toko"])
        if len_data == 0:
            pass

        # Voucher Toko
        for i in range(len_data):
            self.client.get(STATIC_DATA["voucher_toko"][i])

    @task(1)
    def dekorasi_toko(self):
        len_data = len(STATIC_DATA["dekorasi_toko"])
        if len_data == 0:
            pass

        # Dekorasi Toko
        for i in range(len_data):
            self.client.get(STATIC_DATA["dekorasi_toko"][i])
    
    @task(1)
    def manage_product(self):
        len_data = len(STATIC_DATA["manage_product"])
        if len_data == 0:
            pass

        # Manage Product
        for i in range(len_data):
            self.client.get(STATIC_DATA["manage_product"][i])
    
    @task(1)
    def manage_campaign(self):
        len_data = len(STATIC_DATA["manage_campaign"])
        if len_data == 0:
            pass

        # Manage Campaign
        for i in range(len_data):
            self.client.get(STATIC_DATA["manage_campaign"][i])
    
    @task(1)
    def myshop_order(self):
        len_data = len(STATIC_DATA["myshop_order"])
        if len_data == 0:
            pass

        # Seller Order Management
        for i in range(len_data):
            self.client.get(STATIC_DATA["myshop_order"][i])
    
    @task(1)
    def promo(self):
        len_data = len(STATIC_DATA["promo"])
        if len_data == 0:
            pass

        # Promo
        for i in range(len_data):
            self.client.get(STATIC_DATA["promo"][i])
    
    @task(1)
    def statistic_overview(self):
        len_data = len(STATIC_DATA["statistic_overview"])
        if len_data == 0:
            pass

        # Statistic Overview
        for i in range(len_data):
            self.client.get(STATIC_DATA["statistic_overview"][i])

    @task(1)
    def statistic_tokocabang(self):
        len_data = len(STATIC_DATA["statistic_tokocabang"])
        if len_data == 0:
            pass

        # Statistic Tokocabang
        for i in range(len_data):
            self.client.get(STATIC_DATA["statistic_tokocabang"][i])

    @task(1)
    def unknown(self):
        len_data = len(STATIC_DATA["unknown"])
        if len_data == 0:
            pass

        # Unknown
        for i in range(len_data):
            self.client.get(STATIC_DATA["unknown"][i])
