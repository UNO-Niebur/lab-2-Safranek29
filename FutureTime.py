#FutureTime.py
#Name: Louis Safranek
#Date: 01/28/2026
#Assignment: Lab 2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = now.hour
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  hours=int(input("Give a number of hours"))
  #Ask user for minutes
  minutes=int(input("Give a number of Minutes"))
  #Calculate the time after the user-supplied time has passed.
  extraHour=(currentMinute+int(minutes))//60
  futureHour=currentHour + int(hours)+extraHour
  futureMinute = currentMinute + int(minutes)
  
    #Do not use any if statements in calculating the time.
  print(str(futureHour%24)+":"+ str(futureMinute%60))
  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
