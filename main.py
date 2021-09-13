import time
from kivy.clock import Clock

from kivy.properties import NumericProperty, StringProperty
from kivy.uix.image import AsyncImage
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivy import utils
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel

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

    # dialog's
    dialog_spin = None

    # business
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

    def on_start(self):
        self.backgrounds_colors()

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

    ''''
                DOWN HERE STAYS ONLY TESTING FUNCTIONS
    
    '''

    def desc(self):
        rt = self.root
        rt.current = 'description'

    def first(self):
        self.spin_dialog()
        Clock.schedule_once(lambda x: self.test(), 4)

    def test(self):
        for i in range(9):
            card = Foods(on_release=lambda x: self.desc())
            scroll = self.root.ids.front_shop
            self.product_name = f'product{i}'
            self.product_price = f'price{i}/tsh'
            self.company_name = i * 'aa'
            card.add_widget(AsyncImage(source='images/test.png'))
            card.add_widget(Labels(text=self.product_name, halign='center'))
            card.add_widget(Labels(text=self.product_price, halign='center'))
            scroll.add_widget(card)
        self.spin_dismiss()

    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightGreen"
        self.theme_cls.accent = "Brown"
        self.size_x, self.size_y = Window.size
        self.title = "SHOPPY"


MainApp().run()
