import datetime


def get_date():
    return str(datetime.datetime.now()).split(" ")[0]


class Upload_Data:
    # Init firebase with your credentials
    name_admin = ""
    number = 0
    current_time = str(datetime.datetime.now())
    date, time = current_time.strip().split()
    week_day = ""
    day = ""
    admin_product_id = ""
    orders = "1"
    url = []

    def logo(self, logo, phone, name):
        print("Logo START.....")
        if True:
            from firebase_admin import credentials, initialize_app, storage
            print("yes")
            import firebase_admin
            firebase_admin._apps.clear()
            if not firebase_admin._apps:
                print("ok good,,")
                cred = credentials.Certificate("credential/farmzon-abdcb-c4c57249e43b.json")
                default = initialize_app(cred, {'storageBucket': 'farmzon-abdcb.appspot.com'})
                print("WELDING..")
                bucket = storage.bucket()
                blob = bucket.blob("Logos" + "/" + phone + "/" + name + self.id_generator())
                blob.upload_from_filename(logo)
                blob.make_public()
                print("NICE...")
                path = blob.public_url
                print("your file url", Upload_Data.url)
                firebase_admin.delete_app(default)
                return path

    def upload_product_image(self, cate, catee, path, phone, phone_other, name, price, product_name, password, id,
                             description, bio, followers, following, logo, stock, bought):
        print("START.....")
        if True:
            from firebase_admin import credentials, initialize_app, storage
            print("yes")
            import firebase_admin
            firebase_admin._apps.clear()
            if not firebase_admin._apps:
                print("ok good,,")
                cred = credentials.Certificate("credential/farmzon-abdcb-c4c57249e43b.json")
                default = initialize_app(cred, {'storageBucket': 'farmzon-abdcb.appspot.com'})
                print("WELDING..")
                bucket = storage.bucket()
                for i in path:
                    blob = bucket.blob("products" + "/" + cate + "/" + product_name + self.id_generator())
                    blob.upload_from_filename(i)
                    blob.make_public()
                    print("NICE...")
                    Upload_Data.url.append(blob.public_url)
                    print("your file url", Upload_Data.url)
                firebase_admin.delete_app(default)
                image = self.logo(logo, phone, name)
                self.register_admin(phone, phone_other, name, price, product_name, password, id, cate, catee, bio,
                                    followers,
                                    following, image, stock, description, bought)

    def register_admin(self, phone, phone_other, name, price, product_name, password, product_id, cate, catee, bio,
                       followers,
                       following, logo, stock, description, bought):
        if True:
            import firebase_admin
            firebase_admin._apps.clear()
            from firebase_admin import credentials, initialize_app, db
            if not firebase_admin._apps:
                cred = credentials.Certificate("credential/farmzon-abdcb-c4c57249e43b.json")
                initialize_app(cred, {'databaseURL': 'https://farmzon-abdcb.firebaseio.com/'})
                print("Good..", int(phone))
                if cate == "customer":
                    ref = db.reference('Shoppy').child("Company").child(phone)
                    print("New Start")
                    ref.set(
                        {
                            "customer_name": name,
                            "customer_phone": phone,
                            "other_number": phone_other,
                            "customer_password": password,
                            "followers": followers,
                            "following": following,
                            "bio": bio,
                            "logo": logo
                        }
                    )
                    print("Done.. one")
                    ref_products = db.reference('Shoppy').child("Company").child(phone).child("products").child(
                        product_id)
                    ref_products.set(
                        {
                            "product_name": product_name,
                            "product_description": description,
                            "product_price": price,
                            "image_url": Upload_Data.url[0]
                        }
                    )
                    ref_main = db.reference('Shoppy').child("Products").child(catee).child(product_id)
                    ref_main.set(
                        {
                            "product_name": product_name,
                            "product_price": price,
                            "product_description": description,
                            "image_url": Upload_Data.url[0],
                            "company_phone": phone,
                            "bought_times": bought,
                            "company_name": name,
                            "stock": stock
                        }
                    )
                    for i in Upload_Data.url:
                        ref_image = db.reference("Shoppy").child("Products").child(catee).child(product_id).child(
                            "images").child(
                            self.id_generator())
                        ref_image.set({
                            "image_url": i
                        })

                else:
                    ref = db.reference('Shoppy').child("Admin").child(phone)
                    print("New Start")
                    ref.set(
                        {
                            "customer_name": name,
                            "customer_phone": phone,
                            "other_number": phone_other,
                            "customer_password": password
                        }
                    )
                    print("Done.. one")
                    ref_products = db.reference('Shoppy').child("Admin").child(phone).child("products").child(
                        product_id)
                    ref_products.set(
                        {
                            "product_name": product_name,
                            "product_price": price,
                            "product_description": description,
                            "image_url": Upload_Data.url[0]
                        }
                    )
                    ref_main = db.reference('Shoppy').child("Products_admin").child(product_id)
                    ref_main.set(
                        {
                            "product_name": product_name,
                            "product_price": price,
                            "product_description": description,
                            "image_url": Upload_Data.url[0],
                            "admin_phone": phone
                        }
                    )

    def letters(self):
        print("Logo START.....")
        if True:
            from firebase_admin import credentials, initialize_app, storage
            print("yes")
            import firebase_admin
            from string import ascii_uppercase
            firebase_admin._apps.clear()
            if not firebase_admin._apps:
                print("ok good,,")
                cred = credentials.Certificate("credential/farmzon-abdcb-c4c57249e43b.json")
                default = initialize_app(cred, {'storageBucket': 'farmzon-abdcb.appspot.com'})
                print("WELDING..")
                bucket = storage.bucket()
                li = []
                for i in ascii_uppercase:
                    name = i
                    path = '/home/alpha/Documents/Letters/' + name + '.png'
                    blob = bucket.blob("Letters" + '/' + name)
                    blob.upload_from_filename(path)
                    blob.make_public()
                    print("NICE...")
                    path = blob.public_url
                    print("your file url", Upload_Data.url)
                    self.letters_path(path, i)
                    print(path)
                    print(i)

    def letters_path(self, path, name):
        if True:
            import firebase_admin
            firebase_admin._apps.clear()
            from firebase_admin import credentials, initialize_app, db
            if not firebase_admin._apps:
                cred = credentials.Certificate("credential/farmzon-abdcb-c4c57249e43b.json")
                initialize_app(cred, {'databaseURL': 'https://farmzon-abdcb.firebaseio.com/'})
                ref = db.reference('Shoppy').child("Letters").child(name)
                print("New Start")
                ref.set(
                    {
                        "url": path
                    }
                )

    def id_generator(self):
        not_allowed = ".-:"
        date1 = datetime.datetime.now()
        date, time = id = str(date1).split(" ")
        self.admin_product_id = date + time
        product_id = ""
        for i in range(len(self.admin_product_id)):
            if self.admin_product_id[i] not in not_allowed:
                product_id = self.admin_product_id[i] + product_id
        id = self.admin_product_id = product_id
        print(id)
        return self.admin_product_id

    print("Thanks!!!!")


# Upload_Data.letters(Upload_Data())


#bio = 'Nauza saa mbalimbali za kijanja'
#followers = '4'
#following = '0'
#logo = '/home/alpha/Documents/Letters/A.png'
#stock = '10'
#bought = '3'
#image_path = ['/home/alpha/Downloads/products/watch.jpg',
#              '/home/alpha/Downloads/products/watch1.jpg',
#              '/home/alpha/Downloads/products/watch3.jpg',
#              '/home/alpha/Downloads/products/watch2.jpg']
#
#Upload_Data.upload_product_image(Upload_Data(), "customer", "Market",
#                                 image_path, "0715700411", "0758758440", "Aqulline", "300", "Saa kali", "9060",
#                                 Upload_Data.id_generator(
#                                     Upload_Data()),
#                                 "Pata saa kali za ki gentelman!",
#                                 bio, followers, following, logo, stock, bought)

# Upload_Data.register_admin(Upload_Data(), "0788204327", "machungwa", "120", "nyanya", "juice.png", "906070")
