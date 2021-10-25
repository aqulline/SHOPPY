class Fetch:
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


# Fetch.company_stiller(Fetch(), '0687863886')
