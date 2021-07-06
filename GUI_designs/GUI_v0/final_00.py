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
import random
from kivy.properties import DictProperty
from kivy.uix.button import Button


import RPi.GPIO as gpio
import time as time
import math

import os
import sys
import max30100
######## max30100 object
mx30 = max30100.MAX30100()

#import gps

import serial            
import webbrowser
ser = serial.Serial ("/dev/ttyS0" ,baudrate=9600, timeout=1)



LabelBase.register(fn_regular='Orbitron-VariableFont_wght.ttf', name='myfont')

Window.clearcolor = (1, 1, 1, 1)
Window.size = (920, 480)
Window.fullscreen = True


def open_map():
    x = str(ser.read(1200)) #read NMEA string received
    
    pos1 = x.find("$GPRMC")
    pos2 = x.find("\n", pos1)
    loc  = x[pos1:pos2]
    data = loc.split(',')
    
    lati = 0
    long = 0
    
    lat_d = 0
    long_d = 0
    if False:
        print ('No location found')
    else:
        lat = data[3]
        long = data[5]
        
        lat_DD = int(float(lat)/100)
        lat_SS = float(lat) - lat_DD * 100
        lat_d = lat_DD + lat_SS

        
        long_DD = int(float(long)/100) 
        long_SS = float(long) - long_DD * 100
        long_d = long_DD + long_SS
        long_d /= 10
        
        lat_d = 12.933880
        long_d = 77.691836
        
        print ("NMEA Latitude:", lat_d,"NMEA Longitude:", long_d,'\n')
        map_link = 'http://maps.google.com/?q=' + str(lat_d) + ',' + str(long_d)
        #map_link2 = 'https://maps.google.com?saddr=' + str(lat_d) + ',' + str(long_d) + '&daddr'
        webbrowser.open(map_link)


###### RTI methods

hallpin = 17
ledpin = 27

dist_meas = 0.00
km_per_hour = 0
rpm = 0
elapse = 0
pulse = 0
start_timer = time.time()

speed_kmph = 0

elapse_data = []
rpm_data = []
speed_data = []
dist_data = []
def get_pulse(number):
    global pulse, start_timer, elapse, speed_kmph
    pulse+=1   # increase pulse by 1 whenever interrupt occurred
    elapse = time.time() - start_timer # elapse for every 1 complete rotation made!
    start_timer = time.time()


    global rpm,dist_km,dist_meas,km_per_sec,km_per_hour
    if elapse !=0:# to avoid DivisionByZero error
        rpm = 1/elapse * 60
        circ_cm = (2*3.1416)*33.02# calculate wheel circumference in CM
        dist_km = circ_cm/100000 # convert cm to km
        #km_per_sec = dist_km / elapse# calculate KM/sec
        km_per_hour = (dist_km / elapse) * 3600# calculate KM/h
        dist_meas = (dist_km*pulse)*1000# measure distance traverse in meter
        speed_kmph = km_per_hour
        print(km_per_hour)
        print(" ")
        return 1
        

##########RTI
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(hallpin, gpio.IN)
gpio.setup(ledpin, gpio.OUT)
gpio.output(ledpin, False)
gpio.add_event_detect(hallpin, gpio.RISING, callback=get_pulse, bouncetime=100)
#print(time.time())

#heart_data = []
#oxygen_data = []
def get_heart_data():
    
    #mx30.reinit()
    #mx30.set_mode(max30100.MODE_HR)
    #mx30.read_sensor()
    #print("Console : ")
    #print(mx30.read_sensor())
    #print("Hrate sensor")
    #heart_rate = mx30.ir
    #print(heart_rate)
    
    #mx30.set_mode(max30100.MODE_SPO2)
    #mx30.read_sensor()
    #print("oxygen sensor")
    #oxygen = mx30.red
    #print(oxygen)
    
    mx30.enable_spo2()
    mx30.read_sensor()
    hb = int(mx30.ir / 100)
    spo2 = int(mx30.red / 100)  
   # print("HB : ", hb-10, end="\n")
    #print("SPO2 : ", spo2-50)
    
    #data_arr = [75.2, 75.4, 75.9, 76.1, 76.4, 76.8, 76.9, 77.2, 77.3, 77.8, 77.5, 78.0, 78.2, 78.3, 78.6, 78.8, 79.1, 79.3, 79.5, 79.8, 79.9, 80.0]
    #return (random.choice(data_arr))
    
    #print("body temp:")
    #print(mx30.get_temperature())

    #mx30.reset()
    #return heart_rate
    return hb
### main App

class dashboardApp(App):
    variables = DictProperty(
        {"speed": 0, "kms_ran": 69, "mileage": 56, "battery_percentage": 49, "btry_crg_sts": False,
         "battery_temp": 32, "heart_rate": 72, "oxygen": 69})

    def update(self, interval):
        # call kms_ran calculating function here, and update the dict keys
        self.variables["kms_ran"] = 0.4 
        #print(self.variables["kms_ran"])

        # call mileage calculating function here, and update the dict keys
        self.variables["mileage"] = 15
        #print(self.variables["mileage"])

        # call battery_percentage calculating function here, update the dict keys
        self.variables["battery_percentage"] = 19

        # call battery_temp calculating function here, update the dict keys
        self.variables["battery_temp"] = 33

        # call eart_rate calculating function here, update the dict keys
        self.variables["heart_rate"] = get_heart_data()
        #heart_data.append(self.variables["heart_rate"])
        list = [96.2, 95.8, 97.6, 97.7, 97.8, 97.9, 98.0, 98.1, 98.2, 98.3, 98.4, 98.5, 98.6, 98.9]
        if(self.variables["heart_rate"] > 0.00):
            self.variables["oxygen"] = random.choice(list)
        else:
            self.variables["oxygen"] = 0
        #oxygen_data.append(self.variables["oxygen"])
        #print(heart_data)
        #print(oxygen_data)
        
        #speed update here
        self.variables["speed"] = int(speed_kmph)
        

    charging = True  # changes when charger is pluged in
    battery_charge_time = 0
    str_batt_char = ''
    if charging == True:
        battery_charge_time = 2
        str_batt_char = str(battery_charge_time)

    def headlight_callback(self, switchObject, switchValue):
        if (switchValue):
            # turn on the light
            print("headlght_on")
        else:
            # turn off the lights
            print("headlight_off")

    def cruise_mode_callback(self, switchObject, switchValue):
        if (switchValue):
            print("cruise mode on")
            # cruise mode on
    
    def map_callback(self, switchObject, switchValue):
        if(switchValue):
            open_map()
    
    
    ##### calls the update every 1sec to get the real-time data
    def build(self):
        clock.Clock.schedule_interval(self.update, 1)

        return FloatLayout()


###  Credential GUI
class pinApp(App):
    pin = "6969"
    pin_length = 4
    pin_index = 0
    input_text = "6969"

    def build(self):
        layout = FloatLayout()

        b0 = Button(pos_hint={'x': .5, 'center_y': .2}, size_hint=(.2, .2), text='0')
        b1 = Button(pos_hint={'x': .3, 'center_y': .8}, size_hint=(.2, .2), text='1')
        b2 = Button(pos_hint={'x': .5, 'center_y': .8}, size_hint=(.2, .2), text='2')
        b3 = Button(pos_hint={'x': .7, 'center_y': .8}, size_hint=(.2, .2), text='3')
        b4 = Button(pos_hint={'x': .3, 'center_y': .6}, size_hint=(.2, .2), text='4')
        b5 = Button(pos_hint={'x': .5, 'center_y': .6}, size_hint=(.2, .2), text='5')
        b6 = Button(pos_hint={'x': .7, 'center_y': .6}, size_hint=(.2, .2), text='6')
        b7 = Button(pos_hint={'x': .3, 'center_y': .4}, size_hint=(.2, .2), text='7')
        b8 = Button(pos_hint={'x': .5, 'center_y': .4}, size_hint=(.2, .2), text='8')
        b9 = Button(pos_hint={'x': .7, 'center_y': .4}, size_hint=(.2, .2), text='9')
        b_clear = Button(pos_hint={'x': .7, 'center_y': .2}, size_hint=(.2, .2), text='clear')
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

        b0.bind(on_press=self.callback_0)
        b1.bind(on_press=self.callback_1)
        b2.bind(on_press=self.callback_2)
        b3.bind(on_press=self.callback_3)
        b4.bind(on_press=self.callback_4)
        b5.bind(on_press=self.callback_5)
        b6.bind(on_press=self.callback_6)
        b7.bind(on_press=self.callback_7)
        b8.bind(on_press=self.callback_8)
        b9.bind(on_press=self.callback_9)
        b_clear.bind(on_press=self.callback_clear)

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

dashboardApp().run()
root = pinApp()
root.run()


class FloatLayout(FloatLayout):  # root widget, main logic class

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


if __name__ == "__main__":
    
    
    
    dashboardApp().run()
    
    
    
    
    
    


#file = open('geek.txt', 'w+')
#for line in file:
#distance_ran_km = line

