import json


class Fetch:
    data = []

    def Product(self, category):
        """
        company_name:
        company_phone:
        image_url:
        product_description:
        product_name:
        product_price:
        stock:
        """
        import firebase_admin
        firebase_admin._apps.clear()
        from firebase_admin import credentials, initialize_app, db
        if not firebase_admin._apps:
            try:
                cred = credentials.Certificate("credential/farmzon-abdcb-c4c57249e43b.json")
                initialize_app(cred, {'databaseURL': 'https://farmzon-abdcb.firebaseio.com/'})
                store = db.reference("Shoppy").child("Products").child(category)
                print("nice")
                stores = store.get()
                print("good")
                return stores
            except:
                return "No Internet!"

    def image_stiller(self, product_id, cate):
        image_list = []
        import firebase_admin
        firebase_admin._apps.clear()
        from firebase_admin import credentials, initialize_app, db
        cred = credentials.Certificate("credential/farmzon-abdcb-c4c57249e43b.json")
        initialize_app(cred, {'databaseURL': 'https://farmzon-abdcb.firebaseio.com/'})
        store = db.reference("Shoppy").child("Products").child(cate)
        stores = store.get()
        for y, x in stores.items():
            if y == product_id:
                for c, v in x['images'].items():
                    image_list.append(v['image_url'])
                    print("getting", image_list)
        return image_list

    def company_stiller(self, phone):
        """
        bio:
        customer_name:
        customer_password:
        customer_phone:
        followers:
        following:
        logo:
        other_number:
        products::
        """
        import firebase_admin
        firebase_admin._apps.clear()
        from firebase_admin import credentials, initialize_app, db
        if not firebase_admin._apps:
            try:
                cred = credentials.Certificate("credential/farmzon-abdcb-c4c57249e43b.json")
                initialize_app(cred, {'databaseURL': 'https://farmzon-abdcb.firebaseio.com/'})
                store = db.reference("Shoppy").child("Company").child(phone)
                print("nice")
                stores = store.get()

                return stores
            except:
                return "No Internet!"

    def company_products(self, phone):
        import firebase_admin
        firebase_admin._apps.clear()
        from firebase_admin import credentials, initialize_app, db
        if not firebase_admin._apps:
            try:
                cred = credentials.Certificate("credential/farmzon-abdcb-c4c57249e43b.json")
                initialize_app(cred, {'databaseURL': 'https://farmzon-abdcb.firebaseio.com/'})
                store = db.reference("Shoppy").child("Company").child(phone).child('products')
                stores = store.get()
                print(stores)
                return stores
            except:
                return "No Internet!"

    def Profile(self, phone):
        """
                bio:
                course:
                date:
                logo:
                phone:
                user_name:

                """
        import firebase_admin
        firebase_admin._apps.clear()
        from firebase_admin import credentials, initialize_app, db
        if not firebase_admin._apps:
            try:
                cred = credentials.Certificate("credential/farmzon-abdcb-c4c57249e43b.json")
                initialize_app(cred, {'databaseURL': 'https://farmzon-abdcb.firebaseio.com/'})
                store = db.reference("Shoppy").child("Users").child(phone)
                print("nice")
                stores = store.get()
                print(stores)

                return stores
            except:
                return "No Internet!"

    def add_order(self, p_id, price, p_name, phone, date):
        import json
        cached = {p_id: {'phone': phone,
                         'price': price,
                         'productName': p_name,
                         'date': date}}
        self.data.append(cached)
        z = self.load()
        self.data.append(z)
        d = {k: v for x in self.data for k, v in x.items()}
        print(d)
        file = open('data/order.json', 'w')
        file.write(json.dumps(d))
        file.close()

    def load(self):
        try:
            file = open('data/order.json', 'r')
            data = json.load(file)

            return data
        except:
            data = {}
            return data

    def Logos(self, name):
        letter = str(name[0]).capitalize()
        import firebase_admin
        firebase_admin._apps.clear()
        from firebase_admin import credentials, initialize_app, db
        if not firebase_admin._apps:
            try:
                cred = credentials.Certificate("credential/farmzon-abdcb-c4c57249e43b.json")
                initialize_app(cred, {'databaseURL': 'https://farmzon-abdcb.firebaseio.com/'})
                store = db.reference("Shoppy").child("Letters").child(letter).child('url')
                stores = store.get()
                print(stores)
                return stores
            except:
                print('No Internet!')
                return "No Internet!"

    def search(self, text):
        import firebase_admin
        firebase_admin._apps.clear()
        from firebase_admin import credentials, initialize_app, db
        if not firebase_admin._apps:
            try:
                cred = credentials.Certificate("credential/farmzon-abdcb-c4c57249e43b.json")
                initialize_app(cred, {'databaseURL': 'https://farmzon-abdcb.firebaseio.com/'})
                store = db.reference("Shoppy").child("Company")
                text = text.capitalize()
                searched = store.order_by_child("customer_name").start_at(text).get()
            except:
                print('No Internet!')
                return "No Internet!"
            return searched


# Fetch.search(Fetch(),'a')
# Fetch.Logos(Fetch(), 'beast')
# x = Fetch.company_stiller(Fetch(), '0628834063')
# Fetch.company_products(Fetch(), '0687863886')
# Fetch.add_order(Fetch(), '00', '080', '9578', 'p[p[op', '090')
# Fetch.load(Fetch())

