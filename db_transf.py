import datetime

from db_fetch import Fetch as Fe


class Transfer:
    current_time = str(datetime.datetime.now())
    date, time = current_time.strip().split()
    week_day = ""
    day = ""
    point = '1'
    orders = '1'
    number = 0
    order_id = '123'

    def register(self, phone, username):
        if True:
            import firebase_admin
            firebase_admin._apps.clear()
            from firebase_admin import credentials, initialize_app, db
            if not firebase_admin._apps:
                cred = credentials.Certificate("credential/farmzon-abdcb-c4c57249e43b.json")
                initialize_app(cred, {'databaseURL': 'https://farmzon-abdcb.firebaseio.com/'})
                print("Starting deployment....", int(phone))

                ref = db.reference('Shoppy').child('Users')
                users = ref.get()
                if phone in users:
                    print('It there')
                else:
                    ref = db.reference('Shoppy').child("Users").child(phone)
                    print("horray!!!")
                    ref.set(
                        {
                            'user_name': username,
                            'phone': phone,
                            'course': 'None',
                            'date': self.date,
                            'bio': 'Change Bio in Setting!',
                            'logo': Fe.Logos(Fe(), username),
                            'following': '0',
                            'birth-date': 'None',

                        })

    def Order(self, company, phone, location, quantity, amount, product_name):
        if True:
            import firebase_admin
            firebase_admin._apps.clear()
            from firebase_admin import credentials, initialize_app, db
            if not firebase_admin._apps:
                cred = credentials.Certificate("credential/farmzon-abdcb-c4c57249e43b.json")
                initialize_app(cred, {'databaseURL': 'https://farmzon-abdcb.firebaseio.com/'})

            self.orders_calc(company, product_name)
            self.current_time = str(datetime.datetime.now())
            self.date, self.time = self.current_time.strip().split()
            self.id_generator()
            ref = db.reference('Shoppy').child('Company').child(company).child("Orders").child(product_name). \
                child(self.order_id)
            ref.set({
                "company_phone": company,
                "Phone number": phone,
                "location": location,
                "quantity": quantity,
                "amount": amount,
                "oder_id": self.order_id,
                "product name": product_name,
                "time": self.time,
                "date": self.date
            })
            self.order_point(phone, amount)
            self.day_calc()
            refe = db.reference('Shoppy').child('Company').child(company).child("statistics"). \
                child(self.day).child(product_name)
            refe.set({
                "orders": self.orders
            })
            refp = db.reference('Shoppy').child("Users").child(phone).child('point')
            refp.set({
                "point": self.point
            })

    def orders_calc(self, company, name):
        if True:
            import firebase_admin
            firebase_admin._apps.clear()
            from firebase_admin import credentials, initialize_app, db
            if not firebase_admin._apps:
                cred = credentials.Certificate("credential/farmzon-abdcb-c4c57249e43b.json")
                initialize_app(cred, {'databaseURL': 'https://farmzon-abdcb.firebaseio.com/'})

            print('now i am fuckn working')
            self.day_calc()
            try:
                print("Another way")
                ref = db.reference('Shoppy').child('Company').child(company).child('statistics').child(self.day).child(
                    name).child('orders')
                self.orders = str(ref.get())
                self.orders = str(int(self.orders) + 1)
                print(self.orders)
            except:
                self.orders = '1'

    def order_point(self, phone, price):
        if True:
            import firebase_admin
            firebase_admin._apps.clear()
            from firebase_admin import credentials, initialize_app, db
            if not firebase_admin._apps:
                cred = credentials.Certificate("credential/farmzon-abdcb-c4c57249e43b.json")
                initialize_app(cred, {'databaseURL': 'https://farmzon-abdcb.firebaseio.com/'})

            print('order fucker')
            try:
                print("fucking points")
                point = int(price) * (1 / 100)
                ref = db.reference('Shoppy').child("Users").child(phone).child('point')
                points = ref.get()
                self.point = int(points['point']) + point
            except:
                self.point = str(int(price) * (1 / 100))

    def day_calc(self):
        today = str(datetime.date.today())
        y, mon, day = today.strip().split("-")

        print(f'{y}-{mon}-{day}')
        time = f'{y}-{mon}-{day}'
        time = time
        self.day = time

    def id_generator(self):
        date1 = datetime.datetime.now()
        date, time = id = str(date1).split(" ")
        admin_product_id = str(date + time)
        new_id = admin_product_id.replace('-', '')
        new_id = new_id.replace(':', '')
        new_id = new_id.replace('.', '')
        self.order_id = new_id


#company, phone, location, quantity, amount, product_name = '0687863886', '0788204327', 'arusha', '5', '200', 'dildo'

#Transfer.Order(Transfer(), company, phone, location, quantity, amount, product_name)
Transfer.register(Transfer(),'0788204327', 'beast')
