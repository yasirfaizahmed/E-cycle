
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.core.text import LabelBase
from kivy import clock
from kivy.properties import DictProperty



LabelBase.register(fn_regular='Orbitron-VariableFont_wght.ttf', name='myfont')

Window.clearcolor = (1, 1, 1, 1)
Window.size = (800, 480)




class FloatLayout(FloatLayout):    #root widget, main logic class


    def __init__(self, **kwargs):
        super().__init__(**kwargs)





class dashboardApp(App):
    variables = DictProperty({"speed": 25, "kms_ran": 1500, "mileage": 56, "battery_percentage": 49, "btry_crg_sts": False, "battery_temp": 32})


    def update(self, interval):
        # call kms_ran calculating function here, and update the dict keys
        self.variables["kms_ran"] += 1
        print(self.variables["kms_ran"])

        # call mileage calculating function here, and update the dict keys
        self.variables["mileage"] -= 1
        print(self.variables["mileage"])

        # call battery_percentage calculating function here, update the dict keys
        self.variables["battery_percentage"] -= 1

        # call battery_temp calculating function here, update the dict keys
        self.variables["battery_temp"] = 33


    charging = True    #changes when charger is pluged in
    battery_charge_time = 0
    str_batt_char = ''
    if charging == True:
        battery_charge_time = 2
        str_batt_char = str(battery_charge_time)

    def headlight_callback(self,  switchObject, switchValue):
        if(switchValue):
            #turn on the light
            print("headlght_on")
        else:
            #turn off the lights
            print("headlight_off")

    def cruise_mode_callback(self, switchObject, switchValue):
        if(switchValue):
            print("cruise mode on")
            #cruise mode on


    def build(self):
        clock.Clock.schedule_interval(self.update, 1)

        return FloatLayout()



if __name__ == "__main__": 
    dashboardApp().run()

