import datetime

from db_fetch import Fetch as Fe


class Transfer:
    current_time = str(datetime.datetime.now())
    date, time = current_time.strip().split()
    week_day = ""
    day = ""

    def register(self, phone, username):
        if True:
            import firebase_admin
            firebase_admin._apps.clear()
            from firebase_admin import credentials, initialize_app, db
            if not firebase_admin._apps:
                cred = credentials.Certificate("credential/farmzon-abdcb-c4c57249e43b.json")
                initialize_app(cred, {'databaseURL': 'https://farmzon-abdcb.firebaseio.com/'})
                print("Starting deployment....", int(phone))
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