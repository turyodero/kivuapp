from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock



class SliderScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Builder.load_file('screens/sliderscreen/sliderscreen.kv')
        # Set the SliderScreen instance attribute of the Carousel widget

    def current_slide(self, index):
        pass

    

             

    def next(self):
        self.ids.carousel.load_next(mode="next")


   