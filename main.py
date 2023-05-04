from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import ScreenManager 
from screens.homescreen.homescreen import HomeScreen
from screens.splashscreen.splashscreen import SplashScreen
from screens.sliderscreen.sliderscreen import SliderScreen
from screens.loginscreen.loginscreen import LoginScreen
from screens.signupscreen.signupscreen import SignupScreen


from kivy.core.window import Window
from kivymd.uix.screen import MDScreen


#Window.size=(310,600)




class Kivu(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Builder.load_file('screens/splashscreen/splashscreen.kv')
        
        Builder.load_file('screens/sliderscreen/sliderscreen.kv')
        Builder.load_file('screens/loginscreen/loginscreen.kv')
        Builder.load_file('screens/signupscreen/signupscreen.kv')
        Builder.load_file('screens/homescreen/homescreen.kv')
        
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name='splash'))
        sm.add_widget(SliderScreen(name='slider'))
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(SignupScreen(name='signup'))
        sm.add_widget(HomeScreen(name='home'))



    
        
        
        sm.current = 'splash'
        return sm
    
    def current_slide(self, index):
        for i in range(3):
            if index ==  i:
                self.root.ids[f"slide{index}"].color = "#E87040"
            else:
                self.root.ids[f"slide{i}"].color = "#EEEFEF"

    
    def next(self):
        slider_screen = self.root.get_screen('slider')
        slider_screen.ids.carousel.load_next(mode='next')

    



if __name__=="__main__":
    Kivu().run()