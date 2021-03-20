############################ 1024 * 768 res ###############################
############################ edit config.ini file in .kivy/config.ini to make the touch work ###############

######kivy version v2.1.0.dev0  ############################
######pyton version 3.7.3 ##################################

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.core.text import LabelBase
from kivy import clock
from kivy.properties import DictProperty

from kivy.uix.button import Button 

LabelBase.register(fn_regular='Orbitron-VariableFont_wght.ttf', name='myfont')

Window.clearcolor = (1, 1, 1, 1)
Window.size = (920,480 )
Window.fullscreen = True




### main App

class dashboardApp(App):
    
    
    variables = DictProperty({"speed": 25, "kms_ran": 1500, "mileage": 56, "battery_percentage": 49, "btry_crg_sts": False, "battery_temp": 32, "heart_rate": 72, "oxygen": 69})


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
        
        #call eart_rate calculating function here, update the dict keys
        self.variables["heart_rate"] += 1


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






###  Credential GUI
class pinApp(App):
    pin = "6969"
    pin_length = 4
    pin_index = 0
    input_text = ""
    
    
        
    
    
    def build(self):
      layout = FloatLayout()
      
      b0 = Button(pos_hint={'x': .5, 'center_y': .2}, size_hint=(.2, .2),text= '0')
      b1 = Button(pos_hint={'x': .3, 'center_y': .8}, size_hint=(.2, .2),text= '1')
      b2 = Button(pos_hint={'x': .5, 'center_y': .8}, size_hint=(.2, .2),text= '2')
      b3 = Button(pos_hint={'x': .7, 'center_y': .8}, size_hint=(.2, .2),text= '3')
      b4 = Button(pos_hint={'x': .3, 'center_y': .6}, size_hint=(.2, .2),text= '4')
      b5 = Button(pos_hint={'x': .5, 'center_y': .6}, size_hint=(.2, .2),text= '5')
      b6 = Button(pos_hint={'x': .7, 'center_y': .6}, size_hint=(.2, .2),text= '6')
      b7 = Button(pos_hint={'x': .3, 'center_y': .4}, size_hint=(.2, .2),text= '7')
      b8 = Button(pos_hint={'x': .5, 'center_y': .4}, size_hint=(.2, .2),text= '8')
      b9 = Button(pos_hint={'x': .7, 'center_y': .4}, size_hint=(.2, .2),text= '9')
      b_clear = Button(pos_hint={'x': .7, 'center_y': .2}, size_hint=(.2, .2),text= 'clear')
      layout.add_widget(b0)
      layout.add_widget(b1)
      layout.add_widget(b2)
      layout.add_widget(b3)
      layout.add_widget(b4)
      layout.add_widget(b5)
      layout.add_widget(b6)
      layout.add_widget(b7)
      layout.add_widget(b8)
      layout.add_widget(b9)
      layout.add_widget(b_clear)
      
      
      b0.bind(on_press = self.callback_0)
      b1.bind(on_press = self.callback_1)
      b2.bind(on_press = self.callback_2)
      b3.bind(on_press = self.callback_3)
      b4.bind(on_press = self.callback_4)
      b5.bind(on_press = self.callback_5)
      b6.bind(on_press = self.callback_6)
      b7.bind(on_press = self.callback_7)
      b8.bind(on_press = self.callback_8)
      b9.bind(on_press = self.callback_9)
      b_clear.bind(on_press = self.callback_clear)
      
      return layout
      
    def callback_0(self, event): 
        self.input_text += '0'
        self.pin_index += 1
        if self.pin_index == self.pin_length:
            if self.input_text == self.pin:
                App.get_running_app().stop()
                dashboardApp().run()
    def callback_1(self, event): 
        self.input_text += '1'
        self.pin_index += 1
        if self.pin_index == self.pin_length:
            if self.input_text == self.pin:
                App.get_running_app().stop()
                dashboardApp().run()
    def callback_2(self, event): 
        self.input_text += '2'
        self.pin_index += 1
        if self.pin_index == self.pin_length:
            if self.input_text == self.pin:
                App.get_running_app().stop()
                dashboardApp().run()
    def callback_3(self, event): 
        self.input_text += '3'
        self.pin_index += 1
        if self.pin_index == self.pin_length:
            if self.input_text == self.pin:
                App.get_running_app().stop()
                dashboardApp().run()
    def callback_4(self, event): 
        self.input_text += '4'
        self.pin_index += 1
        if self.pin_index == self.pin_length:
            if self.input_text == self.pin:
                App.get_running_app().stop()
                dashboardApp().run()
    def callback_5(self, event): 
        self.input_text += '5'
        self.pin_index += 1
        if self.pin_index == self.pin_length:
            if self.input_text == self.pin:
                App.get_running_app().stop()
                dashboardApp().run()
    def callback_6(self, event): 
        self.input_text += '6'
        self.pin_index += 1
        if self.pin_index == self.pin_length:
            if self.input_text == self.pin:
                App.get_running_app().stop()
                dashboardApp().run()
    def callback_7(self, event): 
        self.input_text += '7'
        self.pin_index += 1
        if self.pin_index == self.pin_length:
            if self.input_text == self.pin:
                App.get_running_app().stop()
                dashboardApp().run()
    def callback_8(self, event): 
        self.input_text += '8'
        self.pin_index += 1
        if self.pin_index == self.pin_length:
            if self.input_text == self.pin:
                App.get_running_app().stop()
                dashboardApp().run()
    def callback_9(self, event): 
        self.input_text += '9'
        self.pin_index += 1
        if self.pin_index == self.pin_length:
            if self.input_text == self.pin:
                App.get_running_app().stop()
                dashboardApp().run()
    def callback_clear(self, event): 
        self.input_text = ""
        self.pin_index = 0
      
    

     

root = pinApp() 
  
# run function runs the whole program 
# i.e run() method which calls the target 
# function passed to the constructor. 
root.run() 






class FloatLayout(FloatLayout):    #root widget, main logic class


    def __init__(self, **kwargs):
        super().__init__(**kwargs)





if __name__ == "__main__": 
    dashboardApp().run()


