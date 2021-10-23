import time
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
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel

Window.keyboard_anim_args = {"d": .2, "t": "linear"}
Window.softinput_mode = "below_target"

if utils.platform != 'android':
    Window.size = (360, 640)


class Spin(MDBoxLayout):
    pass


class Foods(MDCard):
    pass


class Labels(MDLabel):
    pass


class MainApp(MDApp):
    # APP
    size_x = NumericProperty(0)
    size_y = NumericProperty(0)
    screens = ['entrance']
    screens_size = NumericProperty(len(screens) - 1)
    current = StringProperty(screens[len(screens) - 1])

    # dialog's
    dialog_spin = None

    # business
    quantity = StringProperty('0')
    location = StringProperty("Choose location")
    company_name = StringProperty('')
    company_bio = StringProperty('')
    company_followers = StringProperty('')
    company_products = []
    company_logo = StringProperty('')
    company_phone = StringProperty('')

    # product
    product_name = StringProperty('')
    product_price = StringProperty('')
    Product_title = StringProperty('')
    product_stock = StringProperty('')
    product_description = StringProperty('')
    product_image = StringProperty('')
    product_images = []

    # user
    user_name = StringProperty('')
    user_phone = StringProperty('')
    user_location = StringProperty('')
    user_amount = StringProperty('')
    user_following = []
    user_orders = []
    user_products = []
    user_bio = StringProperty('')
    user_logo = StringProperty('')

    def on_start(self):
        self.backgrounds_colors()
        self.keyboard_hooker()

    def backgrounds_colors(self):
        toolbar = self.root.ids.tool
        toolbar.md_bg_color = 1, 1, 1, 1
        toolbar.specific_text_color = 83 / 225, 186 / 225, 115 / 225, 1

        nav = self.root.ids.bnav
        nav.text_color_active = 83 / 225, 186 / 225, 115 / 225, 1

    def spin_dialog(self):
        if not self.dialog_spin:
            self.dialog_spin = MDDialog(
                type="custom",
                size_hint=(.43, None),
                content_cls=Spin(),
            )
        self.dialog_spin.open()

    def spin_dismiss(self):
        self.dialog_spin.dismiss()

    def increment(self, what):
        if what == "minus":
            if int(self.quantity) >= 1:
                self.quantity = str(int(self.quantity) - 1)
        elif what == "plus":
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
        bottom_sheet_menu.open()

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
            toast('fucker')
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

    def company_screen(self):
        pass

    def keyboard_hooker(self):
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)

    ''''
                DOWN HERE STAYS ONLY TESTING FUNCTIONS
    
    '''

    def desc(self, instance):
        self.product_name = instance.id
        self.screen_capture('description')

    def first(self):
        self.spin_dialog()
        Clock.schedule_once(lambda x: self.test(), 4)

    def test(self):
        for i in range(9):
            card = Foods(on_release=self.desc)
            scroll = self.root.ids.front_shop
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
