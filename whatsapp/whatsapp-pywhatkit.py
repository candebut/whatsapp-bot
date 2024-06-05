import time
import pywhatkit;
# import pyautogui
from tkinter import *
from datetime import datetime
import PyPDF2
import os

# win = Tk() # Some Tkinter stuff
# screen_width = win.winfo_screenwidth() # Gets the resolution (width) of your monitor
# screen_height= win.winfo_screenheight() # Gets the resolution (height) of your monitor

# print(screen_width, screen_height) # prints your monitor's resolution

#Contact

# phone_number = input("Enter phone number: ")
# parameters: intber: str, message: str, hour: int, minutes: int, wait_time: int, close after sending: bool, close_time: int
# pywhatkit.sendwhatmsg(phone_number, "Este es un mensaje mandado por Python!", 9, 57, 20, True, 3)

#Group

# group_id = "DVfP3iQCvUy4yCFh7125x9"

# pywhatkit.sendwhatmsg_to_group("DVfP3iQCvUy4yCFh7125x9", 'TEST', 9, 53)

# datetime.now().hour
# datetime.now().minute + 1

# phone_numer =  input("Enter phone number: ")
# group_id =  input("Enter group id: ")
# message =   input("Write your message here: ")
# time_hour =  datetime.now().hour
# time_minute = datetime.now().minute + 1
# waiting_time_to_send = 15
# close_tab = True
# waiting_time_to_close = 2
# mode = 'contact'

# if mode == "contact":
#     pywhatkit.sendwhatmsg(phone_numer, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
# elif mode == "group":
#     pywhatkit.sendwhatmsg_to_group(group_id, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
# else:
#     print("Error code: 97654")
#     print("Error Message: Please select a mode to send your message.")

# pywhatkit.sendwhatmsg("+34644642305", "Enter Message", 14, 31) # Sends the message
# pyautogui.moveTo(screen_width * 0.694, screen_height* 0.964) # Moves the cursor the the message bar in Whatsapp
# pyautogui.click() # Clicks the bar
# pyautogui.press('enter') # Sends the message

def read_lines_from_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return [line.strip() for line in lines if line.strip()]  # remove empty lines

def send_messages_from_text_file(file_path, phone_number):
    lines = read_lines_from_text_file(file_path)
    
    for line in lines:
        message = line
        current_time = datetime.now()
        time_hour = current_time.hour
        time_minute = current_time.minute + 1
        
        # Handle overflow of minutes
        if time_minute >= 60:
            time_minute -= 60
            time_hour += 1
            if time_hour >= 24:
                time_hour -= 24
        
        waiting_time_to_send = 15
        close_tab = True
        waiting_time_to_close = 2

        try:
                pywhatkit.sendwhatmsg(phone_number, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)

        except Exception as e:
            print(f"Failed to send message: {e}")
        
        # Wait before sending the next message
        time.sleep(10)  # wait for a minute before sending the next message

# User inputs
file_name = input("Enter the text file name (if in the same folder as this script): ")
script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the script
file_path = os.path.join(script_dir, file_name)

phone_number = input("Enter phone number (with country code, e.g., +123456789): ")


# Send messages
send_messages_from_text_file(file_path, phone_number)

