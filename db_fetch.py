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


