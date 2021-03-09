#GUI application that uses the airnow api to monitor the aircondiditon i a selected city
from tkinter import *
import PIL
import requests
import json

#Builds window
root = Tk()
root.title('Weather App')
root.geometry('400x400')

#Api link
#http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=75214&distance=15&API_KEY=XXXXXXXXXXXXXXXXXXXXXX

try:
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=75214&distance=25&API_KEY=XXXXXXXXXXXXXXXXXXX")
    api = json.loads(api_request.content)
except Exception as e:
    api = "Error..."

myLabel = Label(root, text=api[0])
myLabel.pack()


root.mainloop()
