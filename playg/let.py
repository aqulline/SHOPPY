import datetime


def day_calc():
    today = str(datetime.date.today())
    y, mon, day = today.strip().split("-")

    print(f'{y}-{mon}-{day}')
    time = f'{y}-{mon}-{day}'
    return time


def id_generator():
    date1 = datetime.datetime.now()
    date, time = id = str(date1).split(" ")
    admin_product_id = str(date + time)
    new_id = admin_product_id.replace('-', '')
    new_id = new_id.replace(':', '')
    new_id = new_id.replace('.', '')
    print(new_id)



