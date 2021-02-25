import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.core.text import LabelBase
from kivy.uix.image import Image
from kivy.graphics import Rectangle


LabelBase.register(fn_regular='Orbitron-VariableFont_wght.ttf', name='myfont')


Window.clearcolor = (0, 0, 0, 1)
Window.size = (800, 480)



class grid(Widget):     #inheritaing from Widget, this is root widget
    def call(self):
        return FloatLayout()


class FloatLayout(FloatLayout):    #root widget, main logic class
    current_speed = 69
    remaining_kms = 12

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.speed = Label(text='[size=70][font=Fonts/static/Orbitron-Medium.ttf]{}'.format(self.current_speed), markup=True, size_hint=(1.0, 1.0))
        self.speed_unit = Label(text='[size=25][font=Fonts/static/Orbitron-Medium.ttf]KMPH', markup=True,
                                size_hint=(1.0, 1.0), pos_hint={"x": 0.0, "y": -0.1})
        self.remaining_kms = Label(text='[size=70][font=Fonts/static/Orbitron-Medium.ttf]{}'.format(self.remaining_kms), markup=True, size_hint=(1.0,1.0), pos_hint={"x": 0.0, "y": -0.2}, font_size='10sp')
        #self.battery_capacity = Rectangle(pos=(100, 100), size=(100, 100))

        self.add_widget(self.speed)
        self.add_widget(self.speed_unit)
        #self.add_widget(self.battery_capacity)


class dashboardApp(App):
    kms_ran = 1500
    str_kms_ran = str(kms_ran) + 'kms'

    mileage = 56
    str_mileage = str(mileage)

    battery_percentage = 49
    str_batt_per = str(battery_percentage)

    charging = False    #changes when charger is pluged in
    battery_charge_time = 0
    str_batt_char = ''
    if charging == True:
        battery_charge_time = 2
        str_batt_char = str(battery_charge_time) + 'hr'


    def build(self):
        return FloatLayout()




if __name__ == "__main__": 
    dashboardApp().run()


