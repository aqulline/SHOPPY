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
                             description, bio, followers, following, logo, stock):
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
                                    following, image, stock, description)

    def register_admin(self, phone, phone_other, name, price, product_name, password, product_id, cate, catee, bio,
                       followers,
                       following, logo, stock, description):
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
                            "company_name": name,
                            "stock":stock
                        }
                    )
                    for i in Upload_Data.url:
                        ref_image = db.reference("Shoppy").child("Products").child(catee).child(product_id).child("images").child(
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


bio = 'fata mambo yako'
followers = '0'
following = '0'
logo = 'C:/Users/DELL/Downloads/beast.jpg'
stock = '7'
image_path = ['C:/Users/DELL/Downloads/imagess.jpeg', 'C:/Users/DELL/Downloads/imags.jpeg',
              'C:/Users/DELL/Downloads/images.jpeg',
              'C:/Users/DELL/Downloads/imges.jpeg']
Upload_Data.upload_product_image(Upload_Data(), "customer", "Food",
                                 image_path, "0687863886", "0734794026", "Zawadi kamote", "10000", "Perfumes", "1010",
                                 Upload_Data.id_generator(
                                     Upload_Data()),
                                 "Black opium ml50, blue princess ml100, locasit ml100, boss ml100, bei @10k~12/=",
                                 bio, followers, following, logo, stock)
#
# Upload_Data.register_admin(Upload_Data(), "0788204327", "machungwa", "120", "nyanya", "juice.png", "906070")
