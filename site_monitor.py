#This is a simple command line tool used to monitor the status of a website
#Input as many URL's in the 'host' list
#Must use the full URL
import subprocess as sp
import requests
import time
import colorama
from colorama import Fore, Style

#TODO: write funciton that corrects URL's typed in wrong fromat to correct format
#List of sites to monitor URLS's must follow https://www.website.com
hosts = ['https://www._______.com/','https://www._______.com', 'https://www._______.com','https://www._______.com/']

starttime=time.time()

red = (Fore.RED + ("\u25CF"))
green = (Fore.GREEN + ("\u25CF"))

'''
Function that pings wbesite for response
Red = no connection to site found
Green = connection found 
'''
def pinger():
    for i in hosts:
        try:
            check = requests.get(i)
            print(i,' ' +  green, Style.RESET_ALL)
        except requests.exceptions.MissingSchema:
            print(i,' ' + red , Style.RESET_ALL)
        except requests.exceptions.ConnectionError:
            print( i,' ' + red , Style.RESET_ALL)
            
#Main function tht calls the pinger and prints results to command line every 10 seconds and clears previous line            
def main():
    while True:
        pinger()
        time.sleep(10.0 - ((time.time() - starttime) % 10.0))
        sp.call('cls',shell=True)
        

main()
