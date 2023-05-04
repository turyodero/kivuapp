from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock



class SplashScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Builder.load_file('screens/splashscreen/splashscreen.kv')
        

    def on_enter(self):
        Clock.schedule_once(self.switch_screen, 3) # delay for 4 seconds

    def switch_screen(self, dt):
        print('Switching screens...')
        print('Current screen:', self.manager.current)
        self.manager.current = 'slider'
        print('New screen:', self.manager.current)
