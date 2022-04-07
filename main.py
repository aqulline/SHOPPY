import os
import re
import threading
from os.path import join

from kivy.clock import Clock

from kivy.properties import NumericProperty, StringProperty
from kivy.uix.image import AsyncImage
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.toast import toast
from kivymd.uix.bottomsheet import MDListBottomSheet
from kivy.base import EventLoop
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivy import utils
import phonenumbers
from kivymd.uix.list import OneLineIconListItem, ILeftBody
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField

from db_transf import Transfer as TR
from db_fetch import Fetch as FE

Window.keyboard_anim_args = {"d": .2, "t": "linear"}
Window.softinput_mode = "below_target"

if utils.platform != 'android':
    Window.size = (412, 732)


class ImagelftWidgt(ILeftBody, AsyncImage):
    pass


class CustomOneLineIconListItem(OneLineIconListItem, AsyncImage):
    icon = StringProperty()
    phone = StringProperty


class Spin(MDBoxLayout):
    pass


class Order(MDBoxLayout):
    pass


class Alert(MDBoxLayout):
    pass


class Foods(MDCard):
    pass


class Labels(MDLabel):
    pass


class NumberOnlyField(MDTextField):
    pat = re.compile('[^0-9]')

    def insert_text(self, substring, from_undo=False):

        pat = self.pat

        if "." in self.text:
            s = re.sub(pat, "", substring)

        else:
            s = ".".join([re.sub(pat, "", s) for s in substring.split(".", 1)])

        return super(NumberOnlyField, self).insert_text(s, from_undo=from_undo)


class MainApp(MDApp):
    # APP
    size_x = NumericProperty(0)
    size_y = NumericProperty(0)
    screens = ['entrance']
    screens_size = NumericProperty(len(screens) - 1)
    current = StringProperty(screens[len(screens) - 1])

    # dialog's
    dialog_spin = None
    alert_dialog = None
    order_dialog = None

    # business
    quantity = StringProperty('1')
    location = StringProperty("Choose location")
    amount = StringProperty("")
    company_name = StringProperty('')
    company_bio = StringProperty('')
    company_followers = StringProperty('')
    company_following = StringProperty('')
    company_products = []
    company_logo = StringProperty('')
    company_phone = StringProperty('')
    company_details = []

    # product
    product_name = StringProperty('')
    product_price = StringProperty('')
    Product_title = StringProperty('')
    product_stock = StringProperty('')
    product_id = StringProperty('')
    product_description = StringProperty('')
    product_image = StringProperty('')
    product_images = []
    total_images = StringProperty('')
    image_counter = StringProperty('1')

    # for food
    food_product = []
    food_products = []
    market_product = []
    market_products = []
    category = StringProperty('')

    # Temporary
    t_company_products = []
    t_company_product = []
    company_instances = []
    t_product_name = StringProperty('')
    t_product_price = StringProperty('')
    t_Product_title = StringProperty('')
    t_product_stock = StringProperty('')
    t_product_id = StringProperty('')
    t_product_description = StringProperty('')
    t_product_image = StringProperty('')
    t_price_comma = StringProperty('')
    user_date = StringProperty('22.6.2002')

    # ONCE counter's
    food_counter = NumericProperty(0)
    profile_counter = NumericProperty(0)

    # user
    user_name = StringProperty('')
    user_phone = StringProperty('')
    user_location = StringProperty('')
    user_amount = StringProperty('')
    user_following = []
    user_point = StringProperty('0')
    user_orders = []
    user_products = []
    user_details = []
    user_bio = StringProperty('')
    user_logo = StringProperty('')
    user_login = NumericProperty(0)
    user_course = StringProperty('')

    def on_start(self):
        self.backgrounds_colors()
        self.keyboard_hooker()
        thread = threading.Thread(target=self.call_look)
        thread.start()

    def backgrounds_colors(self):
        toolbar = self.root.ids.tool
        toolbar.md_bg_color = 1, 1, 1, 1
        toolbar.specific_text_color = 83 / 225, 186 / 225, 115 / 225, 1

        nav = self.root.ids.bnav
        nav.text_color_active = 83 / 225, 186 / 225, 115 / 225, 1

        button = self.root.ids.buy
        button.md_bg_color = 83 / 225, 186 / 225, 115 / 225, 1

        button1 = self.root.ids.follow
        button1.md_bg_color = 78 / 255, 82 / 255, 84 / 255, 1

        button2 = self.root.ids.b_register
        button2.md_bg_color = 83 / 225, 186 / 225, 115 / 225, 1

        button3 = self.root.ids.bp
        button3.md_bg_color = 78 / 255, 82 / 255, 84 / 255, 1

        spin = self.root.ids.spin
        spin.color = 78 / 255, 82 / 255, 84 / 255, 1

        spine = self.root.ids.spine
        spine.color = 78 / 255, 82 / 255, 84 / 255, 1


    def spin_dialog(self):
        if not self.dialog_spin:
            self.dialog_spin = MDDialog(
                type="custom",
                auto_dismiss=False,
                size_hint=(.43, None),
                content_cls=Spin(),
            )
        self.dialog_spin.open()

    def dialog_alert(self):
        if not self.alert_dialog:
            self.alert_dialog = MDDialog(
                type='custom',
                auto_dismiss=False,
                size_hint=(.4, None),
                content_cls=Alert()
            )
        self.alert_dialog.open()

    def alert_dismiss(self):
        self.alert_dialog.dismiss()

    def spin_dismiss(self):
        self.dialog_spin.dismiss()

    def increment(self, what):
        if what == "minus":
            if int(self.quantity) >= 2:
                self.quantity = str(int(self.quantity) - 1)
        elif what == "plus":
            if self.quantity < self.product_stock:
                self.quantity = str(int(self.quantity) + 1)

    def callback_for_menu_items(self, *args):
        toast(args[0])
        self.location = args[0]

    def location_sheet(self):
        bottom_sheet_menu = MDListBottomSheet()
        vimbweta = [
            "vimbweta vya uwanjani",
            "vimbweta vya stationary",
            "vimbweta vya girls hostel",
            "vimbweta vya boys hostel",
            "vimbweta nyuma ya ndege",
            "vimbweta vya block 16",
            "vimbweta vya adminstration",
            "class one",
            "class two",
            "class three",
            "class four",
            "class five",
            "class six",
            "class seven",
            "Aviation classes"
        ]
        for i in vimbweta:
            bottom_sheet_menu.add_item(
                i,
                lambda x, y=i: self.callback_for_menu_items(y),
                icon="google-maps"
            )
        for i in range(1, 22):
            bottom_sheet_menu.add_item(
                f"Block {i}",
                lambda x, y=i: self.callback_for_menu_items(
                    f"Block {y}"
                ),
                icon='google-maps'
            )
        bottom_sheet_menu.radius_from = 'top'
        bottom_sheet_menu.open()

    def refresh(self):
        self.alert_dismiss()
        self.food_counter = 0
        self.food_caller()

    def hook_keyboard(self, window, key, *largs):
        print(self.screens_size)
        if key == 27 and self.screens_size > 0:
            print(f"your were in {self.current}")
            last_screens = self.current
            self.screens.remove(last_screens)
            print(self.screens)
            self.screens_size = len(self.screens) - 1
            self.current = self.screens[len(self.screens) - 1]
            self.screen_capture(self.current)
            return True
        elif key == 27 and self.screens_size == 0:
            toast('Press Home button!')
            return True

    def screen_capture(self, screen):
        sm = self.root
        sm.current = screen
        if screen in self.screens:
            pass
        else:
            self.screens.append(screen)
        print(self.screens)
        self.screens_size = len(self.screens) - 1
        self.current = self.screens[len(self.screens) - 1]
        print(f'size {self.screens_size}')
        print(f'current screen {screen}')

    def screen_leave(self):
        print(f"your were in {self.current}")
        last_screens = self.current
        self.screens.remove(last_screens)
        print(self.screens)
        self.screens_size = len(self.screens) - 1
        self.current = self.screens[len(self.screens) - 1]
        self.screen_capture(self.current)

    def company_screen(self, instance):
        self.screen_capture('company')
        self.company_instances.append(instance)
        self.clear_company()
        self.spin_dialog()
        Clock.schedule_once(lambda x: self.company(instance), 4)

    def clear_company(self):
        parent = self.root.ids.cproducts
        for child in parent.children:
            parent.remove_widget(child)

    def keyboard_hooker(self):
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)

    ''''
                    DOWN HERE STAYS ONLY Product and COMPANY Association FUNCTIONS

        '''

    def image_slider(self):
        id = self.product_id
        cate = self.category
        slider = self.root.ids.image_slide
        slider.clear_widgets()
        self.product_images = FE.image_stiller(FE(), id, cate)
        self.total_images = str(self.product_images.__len__())
        for i in self.product_images:
            slider.add_widget(AsyncImage(source=i))

    def counter_image(self):
        cr = self.root.ids.image_slide
        self.image_counter = str(1 + int(self.image_counter))
        sa = cr.slides
        se = cr.index
        print(sa, se)

    def desc(self, instance):
        product = instance.id
        self.product_name = self.food_products[product]["product_name"]
        self.product_price = self.food_products[product]['product_price']
        self.product_image = self.food_products[product]['image_url']
        self.company_name = self.food_products[product]['company_name']
        self.company_phone = self.food_products[product]['company_phone']
        self.product_description = self.food_products[product]['product_description']
        self.product_stock = self.food_products[product]['stock']
        self.product_id = product
        self.t_price_comma = '{:,}'.format(int(self.product_price))
        thread = threading.Thread(target=self.image_slider())
        thread.start()

        self.screen_capture('description')

    def company(self, instance):
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
        button1 = self.root.ids.follow
        self.company_details = FE.company_stiller(FE(), instance)
        self.company_name = self.company_details['customer_name']
        self.company_logo = self.company_details['logo']
        self.company_bio = self.company_details['bio']
        self.company_followers, self.company_following = self.company_details['followers'], self.company_details[
            'following']
        self.company_phone = self.company_details['customer_phone']
        self.company_product(instance)
        try:
            if self.user_phone in self.company_details['loyalties']:
                button1.md_bg_color = 1, 1, 1, 1
                button1.text_color = 78 / 255, 82 / 255, 84 / 255, 1
                button1.text = 'devoted'
                button1.disabled = True
            else:
                pass
        except:
            button1.md_bg_color = 78 / 255, 82 / 255, 84 / 255, 1
            button1.text_color = 1, 1, 1, 1
            button1.text = 'loyal'
            button1.disabled = False

    def clear_products(self):
        parent = self.root.ids.front_shop
        counter = 0
        parent.clear_widgets()
        for child in parent.children:
            counter += 1
            print(counter)
            parent.remove_widget(child)

    def food_caller(self):
        if self.food_counter == 0:
            self.spin_dialog()
            self.food_counter = 1
            Clock.schedule_once(lambda x: self.Food(self.category), 4)
        else:
            pass

    def Food(self, cate):
        """
                company_name:
                company_phone:
                image_url:
                images:
                product_description:
                product_name:
                product_price:
                stock:
                """
        self.food_product = FE.Product(FE(), cate)
        if self.food_product == "No Internet!":
            toast('Network problem!')
            self.spin_dismiss()
            self.dialog_alert()
        else:
            self.food_products = self.food_product
            for x, y in self.food_product.items():
                card = Foods(on_release=self.desc)
                scroll = self.root.ids.front_shop
                self.product_name = y["product_name"]
                self.product_price = y["product_price"]
                self.product_image = y["image_url"]
                card.add_widget(AsyncImage(source=self.product_image))
                card.add_widget(Labels(text=self.product_name, halign='center'))
                card.add_widget(Labels(text='{:,}'.format(int(self.product_price)) + '/=Tsh', halign='center'))
                card.id = x
                scroll.add_widget(card)
            self.spin_dismiss()

    def company_product(self, phone):
        self.t_company_product = FE.company_products(FE(), phone)
        if self.t_company_product == "No Internet!":
            toast('Network problem!')
            self.spin_dismiss()
            self.dialog_alert()
        else:
            self.t_company_products = self.t_company_product
            for x, y in self.t_company_product.items():
                card = Foods(on_release=self.desc)
                scroll = self.root.ids.cproducts
                self.product_name = y["product_name"]
                self.product_price = y["product_price"]
                self.product_image = y["image_url"]
                card.add_widget(AsyncImage(source=self.product_image))
                card.add_widget(Labels(text=self.product_name, halign='center'))
                card.add_widget(Labels(text='{:,}'.format(int(self.product_price)) + '/=Tsh', halign='center'))
                card.id = x
                scroll.add_widget(card)
            self.spin_dismiss()

    def loyal_helper(self):
        self.company_followers = TR.add_loyal(TR(), self.company_phone, self.user_phone, self.user_name)

    def loyalty(self):
        button1 = self.root.ids.follow
        button1.md_bg_color = 1, 1, 1, 1
        button1.text_color = 78 / 255, 82 / 255, 84 / 255, 1
        button1.text = 'devoted'
        button1.disabled = True
        thr = threading.Thread(target=self.loyal_helper)
        thr.start()

    ''''
                        UP HERE STAYS ONLY Product Association FUNCTIONS

            '''

    """ 
    DOWN HERE STAYS USER ASSOCIATION FUNCTIONS
    """

    def phone_number_check_admin(self, phone):
        new_number = ""
        if phone != "":
            for i in range(phone.__len__()):
                if i == 0:
                    pass
                else:
                    new_number = new_number + phone[i]
            number = "+255" + new_number
            if not carrier._is_mobile(number_type(phonenumbers.parse(number))):
                toast("Please check your phone number!", 1)
                return False
            else:
                self.public_number = number
                return True
        else:
            toast("enter phone number!")

    def register_caller(self, phone, name):
        from db_transf import Transfer as TR
        try:
            self.spin_dialog()
            TR.register(TR(), phone, name)
            self.remember_me(phone, 'i am emma nyoo...', name)
            self.spin_dismiss()
            sm = self.root
            sm.current = 'entrance'
        except:
            toast('OPPs!, No connection')

    def validate_user(self, phone, name):
        if not self.phone_number_check_admin(phone):
            toast("please enter your phone number correctly")
        elif name == "":
            toast("please enter your name")
        else:
            toast("Please wait!")
            Clock.schedule_once(lambda x: self.register_caller(phone, name), 1)


    def call_look(self):
        self.spin_dialog()
        self.spin_dismiss()
        Clock.schedule_once(lambda x: self.look_up(), 6)

    def look_up(self):
        sm = self.root
        file_size = os.path.getsize("credential/admin.txt")
        if file_size == 0:
            sm.current = "register"
            self.spin_dismiss()
        else:
            self.spin_dialog()
            sm.current = "entrance"
            thread = threading.Thread(target=self.check_user)
            thread.start()
            thread.join()
            self.spin_dismiss()

    def check_user(self):
        print('hi')
        if self.user_login == 0:
            self.user_login = 1 + self.user_login
            file1 = open('credential/admin.txt', 'r')
            file2 = open("credential/admin_info.txt")
            Lines = file1.readlines()
            Lines2 = file2.readlines()
            # Strips the newline character
            self.user_phone = Lines[0].strip()
            dust = Lines[1].strip()
            self.user_name = Lines2[0]
        else:
            sm = self.root
            sm.current = "entrance"

    def remember_me(self, phone, dust, name):
        with open("credential/admin.txt", "w") as fl:
            fl.write(phone + "\n")
            fl.write(dust)
        with open("credential/admin_info.txt", "w") as ui:
            ui.write(name)
        fl.close()
        ui.close()

    user_counter = 0

    def profile_caller(self):
        if self.user_counter == 0:
            self.user_counter = self.user_counter + 1
            self.spin_dialog()
            Clock.schedule_once(lambda x: self.user_profile(), 5)

    def clear_user(self):
        with open("credential/admin.txt", 'r+') as f:
            f.truncate(0)
            f.close()
        with open("credential/admin_info.txt", "r+") as d:
            d.truncate(0)
            d.close()

    def user_profile(self):
        """
                        bio:
                        course:
                        date:
                        logo:
                        phone:
                        user_name:
        """
        file = open('credential/admin.txt', 'r')
        line = file.readlines()
        self.user_phone = line[0].strip()
        try:
            self.user_details = FE.Profile(FE(), self.user_phone)
            self.user_phone = self.user_details['phone']
            self.user_name = self.user_details['user_name']
            self.user_logo = self.user_details['logo']
            self.user_bio = self.user_details['bio']
            point = self.user_details["point"]
            self.user_point = str(point['point'])
            self.spin_dismiss()
        except:
            self.spin_dismiss()
            toast('Opps!, No internet')

    def buying_point(self):
        toast('If you reach 1000/bp contact us!')

    """
     
    UP HERE STAYS USER ASSOCIATION FUNCTIONS
    
    """

    """
    
    ORDER FUNCTIONS STAYS DOWN HERE
    
    """

    def dialog_order(self):
        if not self.order_dialog:
            self.order_dialog = MDDialog(
                title="Invoice Confirmation",
                type="custom",
                auto_dismiss=False,
                content_cls=Order(),
            )
        self.order_dialog.open()

    def order_dismiss(self):
        self.order_dialog.dismiss()

    def call_order(self):
        company = self.company_phone
        product_name = self.product_name
        quantity = self.quantity
        location = self.location
        phone = self.user_phone
        self.amount = str(int(quantity) * int(self.product_price))
        self.amount = str('{:,}'.format(int(self.amount)))
        self.dialog_order()

    def order_caller(self):
        self.order_dismiss()
        toast("please wait..")
        Clock.schedule_once(lambda x: self.order(), .9)

    def order(self):
        from db_transf import Transfer as TF
        company = self.company_phone
        product_name = self.product_name
        quantity = self.quantity
        location = self.location
        phone = self.user_phone
        self.amount = str(int(quantity) * int(self.product_price))
        self.send_sms(phone, location, self.company_phone, product_name, quantity)
        TF.Order(TF(), company, phone, location, quantity, self.amount, product_name, self.category, self.product_id)
        toast("Ordered successfully!")

    """
    ORDER FUNCTIONS STAYS UP HERE
    """

    """
                            DOWN HERE STAYS ONLY SEARCH RELATED FUNCTION
    """

    def set_list_customer_name(self, text="", search=False):

        def add_customer_item(name, image, phone):
            self.root.ids.customers.data.append(
                {
                    "viewclass": "CustomOneLineIconListItem",
                    "icon": image,
                    "phone": phone,
                    "text": name,
                }
            )

        def searching():
            phones = FE.search(FE(), text)
            for x, y in phones.items():
                add_customer_item(y['customer_name'], y['logo'], x)
            spinner.active = False
            name.disabled = False

        temp = []
        self.root.ids.customers.data = []
        spinner = self.root.ids.spin
        name = self.root.ids.searchText
        if search:
            name.disabled = True
            spinner.active = True
            thread = threading.Thread(target=searching)
            thread.start()

    """
                            UP HERE STAYS ONLY SEARCH RELATED FUNCTION
    """

    '''
                DOWN HERE STAYS BEEM FUNCTIONS ONLY
    '''

    def send_sms(self, phone, location, phone_c, product_name, quantity):
        from beem import sms as sm

        sm.send_sms(phone, location, phone_c, product_name, quantity)

    '''
                UP HERE STAYS BEEM FUNCTIONS ONLY
    '''

    '''
        DOWN HERE STAYS 
    '''

    ''''
                DOWN HERE STAYS ONLY TESTING FUNCTIONS

    '''

    def test(self):
        for i in range(9):
            card = Foods(on_release=self.desc)
            scroll = self.root.ids.cproducts
            self.product_name = f'product{i}'
            self.product_price = f'price{i}/tsh'
            self.company_name = i * 'aa'
            card.add_widget(AsyncImage(source='images/test.png'))
            card.add_widget(Labels(text=self.product_name, halign='center'))
            card.add_widget(Labels(text=self.product_price, halign='center'))
            card.id = f'product{i}'
            scroll.add_widget(card)
        self.spin_dismiss()

    ''''
                    UP HERE STAYS ONLY TESTING FUNCTIONS

    '''

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightGreen"
        self.theme_cls.accent = "Brown"
        self.size_x, self.size_y = Window.size
        self.title = "SHOPPY"


MainApp().run()

# info@warifng.org
# +1 809-210-0008
