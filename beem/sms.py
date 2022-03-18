import json
import requests


def phone_repr(phone):
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


def send_sms(phone, location, phone_company, product, quantity):
    URL = 'https://apisms.beem.africa/v1/send'
    content_type = 'application/json'
    source_addr = 'INFO'
    secrete_key = "ZGVmNWVkMzYxZmRhNWQ3MjM3NDhkMThmMWFkYzg4ZTM0ZGUwMjZmMGZjYTkzNWNkODRkMzFiMWJkZmM0M2JmYw=="
    api_key = '8ccab9418dedde47'
    phonee = phone_repr(phone_company)
    apikey_and_apisecret = api_key + ':' + secrete_key

    first_request = requests.post(url=URL, data=json.dumps({
        'source_addr': 'INFO',
        'schedule_time': '',
        'encoding': '0',
        'message': f'SHOPPY You have an order from{phone}, '
                   f'product name {product}, quantity {quantity} '
                   f'customer location {location}',
        'recipients': [
            {
                'recipient_id': 1,
                'dest_addr': phonee,
            }
        ],
    }),

                                  headers={
                                      'Content-Type': content_type,
                                      'Authorization': 'Basic ' + api_key + ':' + secrete_key,
                                  },
                                  auth=(api_key, secrete_key), verify=False)

    print(first_request.status_code)
    print(first_request.json())
    return (first_request.json())

# send_sms('0788204327', 'vimbweta vya uwanjani', '0676133153', 'karanga', '5')
