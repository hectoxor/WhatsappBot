import pywhatkit
import os
def send_message():
   mobile = os.getenv('mobile')
   message = input('msg')
   hour = int(input('h'))
   minutes = int(input('m'))
   #pywhatkit.sendwhatmsg(phone_no = mobile, message = message,time_hour = hour, time_min = minutes)
   pywhatkit.sendwhatmsg_to_group("group_id", message, hour, minutes)

def main():
   send_message()

if __name__ == '__main__':
   main()
