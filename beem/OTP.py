import requests
import json
from BeemAfrica import Authorize, OTP


# request class

class req:
    pin = ''
    phone = ''

    def otp_req(self, phone):
        URL = 'https://apiotp.beem.africa/v1/request'
        content_type = 'application/json'
        source_addr = 'INFO'
        secrete_key = "ZGVmNWVkMzYxZmRhNWQ3MjM3NDhkMThmMWFkYzg4ZTM0ZGUwMjZmMGZjYTkzNWNkODRkMzFiMWJkZmM0M2JmYw=="
        api_key = '8ccab9418dedde47'
        Authorize(api_key, secrete_key)
        req.phone = self.phone_repr(phone)
        print(phone)
        first_request = requests.post(url=URL, data=json.dumps({
            "appId": 181,
            "msisdn": self.phone_repr(phone)
        }),

                                      headers={
                                          'Content-Type': content_type,
                                          'Authorization': 'Basic ' + api_key + ':' + secrete_key,
                                      },
                                      auth=(api_key, secrete_key), verify=False)

        print(first_request.status_code)
        print(first_request.json())
        data = first_request.json()
        req.pin = pin = data['data']['pinId']
        print(pin)
        ver = data['data']['message']['code']
        if ver == 100:

            return True
        else:
            return False

    def verfy(self, pin):
        print(req.pin)
        data = OTP.verify(pin_id=self.pin, pin=pin)
        print(data)
        valid = data['data']['message']['code']
        if valid == 117:

            return True
        else:
            return False


    def phone_repr(self, phone):
        new_number = ""
        if phone != "":
            for i in range(phone.__len__()):
                if i == 0:
                    pass
                else:
                    new_number = new_number + phone[i]
            number = "255" + new_number
            public_number = number
            return public_number
