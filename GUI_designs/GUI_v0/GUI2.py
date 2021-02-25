import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.core.text import LabelBase
from kivy import clock
from kivy.properties import DictProperty



LabelBase.register(fn_regular='Orbitron-VariableFont_wght.ttf', name='myfont')


Window.clearcolor = (0, 0, 0, 1)
Window.size = (800, 480)






class FloatLayout(FloatLayout):    #root widget, main logic class
    current_speed = 69

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.speed = Label(text='[size=70][font=Fonts/static/Orbitron-Medium.ttf]{}'.format(self.current_speed), markup=True, size_hint=(1.0, 1.0))
        self.speed_unit = Label(text='[size=25][font=Fonts/static/Orbitron-Medium.ttf]KMPH', markup=True,
                                size_hint=(1.0, 1.0), pos_hint={"x": 0.0, "y": -0.1})


        self.add_widget(self.speed)
        self.add_widget(self.speed_unit)






class dashboardApp(App):
    variables = DictProperty({"kms_ran": 1500})


    kms_ran = 1500

    def update(self, interval):
        self.variables["kms_ran"] += 1
        print(self.str_kms_ran)




    str_kms_ran = str(kms_ran) + 'kms'

    mileage = 56
    str_mileage = str(mileage)

    battery_percentage = 49
    str_batt_per = str(battery_percentage)

    charging = True    #changes when charger is pluged in
    battery_charge_time = 0
    str_batt_char = ''
    if charging == True:
        battery_charge_time = 2
        str_batt_char = str(battery_charge_time) + 'hr'

    def headlight_callback(self,  switchObject, switchValue):
        if(switchValue):
            print("headlght_on")
        else:
            print("headlight_off")




    def build(self):
        clock.Clock.schedule_interval(self.update, 1)

        return FloatLayout()



if __name__ == "__main__": 
    dashboardApp().run()

