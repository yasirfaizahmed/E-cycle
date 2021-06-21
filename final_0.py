import serial            
from time import sleep
import sys
import webbrowser

ser = serial.Serial ("/dev/ttyS0")
GNGGA_info = "$GNGGA,"
GNGGA_buffer = 0
NMEA_buff = 0
GNGGA_data_available = ""

def convert_to_degrees(raw_value):
    decimal_value = raw_value/100.00
    degrees = int(decimal_value)
    mm_mmmm = (decimal_value - int(decimal_value))/0.6
    position = degrees + mm_mmmm
    position = "%.4f" %(position)
    return position
 
while True:
    GNGGA_buffer = []        
    received_data = (str)(ser.read(200)) #read NMEA string received
    GNGGA_data_available = received_data.find(GNGGA_info)#check for NMEA GNGGA string
    


    if (GNGGA_data_available):
         
        try:
            GNGGA_buffer = received_data.split("$GNGGA,",1)[1] #store data coming after “$GNGGA,” string
        except IndexError:
            
            continue
        
        NMEA_buff = (GNGGA_buffer.split(','))
        nmea_time = []
        nmea_latitude = []
        nmea_longitude = []
        nmea_time = NMEA_buff[0] #extract time from GNGGA string
        nmea_latitude = NMEA_buff[1] #extract latitude from GNGGA string
        nmea_longitude = NMEA_buff[3]
        print("NMEA Time: ", nmea_time,'\n')
        lat = (float)(nmea_latitude)
        lat = convert_to_degrees(lat)
        longi = (float)(nmea_longitude)
        longi = convert_to_degrees(longi)
        print ("NMEA Latitude:", lat,"NMEA Longitude:", longi,'\n')
        map_link = 'http://maps.google.com/?q=' + lat + ',' + longi
        map_link2 = 'https://maps.google.com?saddr=' + lat + ',' + longi + '&daddr'
        webbrowser.open(map_link)
        webbrowser.open(map_link2)
        
    sys.exit(0)
    break