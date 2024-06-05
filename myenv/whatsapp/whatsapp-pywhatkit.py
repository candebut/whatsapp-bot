import pywhatkit;

#Contact

# phone_number = input("Enter phone number: ")
# parameters: intber: str, message: str, hour: int, minutes: int, wait_time: int, close after sending: bool, close_time: int
# pywhatkit.sendwhatmsg(phone_number, "Este es un mensaje mandado por Python!", 9, 57, 20, True, 3)

#Group

# group_id = "DVfP3iQCvUy4yCFh7125x9"

# pywhatkit.sendwhatmsg_to_group("DVfP3iQCvUy4yCFh7125x9", 'TEST', 9, 53)

phone_numer =  input("Enter phone number: ")
group_id =  input("Enter group id: ")
message =   input("Write your message here: ")
time_hour =  10
time_minute = 2
waiting_time_to_send = 20
close_tab = True
waiting_time_to_close = 2
mode = 'contact'

if mode == "contact":
    pywhatkit.sendwhatmsg(phone_numer, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
elif mode == "group":
    pywhatkit.sendwhatmsg_to_group(group_id, message, time_hour, time_minute, waiting_time_to_send, close_tab, waiting_time_to_close)
else:
    print("Error code: 97654")
    print("Error Message: Please select a mode to send your message.")