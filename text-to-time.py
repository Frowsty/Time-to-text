import datetime
import time
import os
import keyboard
special_times = ["", "ten", "twenty", "thirty", "fourty", "fifty"]
times = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
        "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

def translate_time(user_input):
        hour_milestone = ""
        timeof_day = ""
        minutes_past = ""
        user_input = str(user_input)
        time_data = user_input.split(':')
        
        if len(time_data[0]) > 2 or len(time_data[1]) > 2 or int(time_data[0]) > 23 or int(time_data[1]) > 59:
                print("Stay within the 24h clock, don't go past it or this won't work")
                return #refrain from throwing an error at the user by prompting them to input correct data
        
        hour = int(time_data[0])
        minutes = int(time_data[1])

        #check the "milestones" in each hour
        if minutes == 30:
                hour_milestone = "half past"
        elif minutes == 15:
                hour_milestone = "quarter past"
        elif minutes == 45:
                hour_milestone = "quarter to"
                hour += 1
        else:
                hour_milestone = ""

        #check if we're inbetween the "milestones" in each hour
        if minutes < 20 and minutes != 15:
                minutes_past = f"{times[minutes]} past"
        elif minutes > 20 and minutes < 30:
                minutes = list(str(minutes))
                minutes_past = f"{special_times[int(minutes[0])]}-{times[int(minutes[1])]} past"
        elif minutes > 30 and minutes != 45:
                minutes_to_hour = 60 - minutes
                minutes = list(str(minutes_to_hour))
                hour += 1
                if len(minutes) == 1:
                        minutes_past = f"{times[int(minutes[0])]} to"
                elif minutes_to_hour < 20:
                        minutes_past = f"{times[minutes_to_hour]} to"
                else:
                        minutes_past = f"{special_times[int(minutes[0])]}-{times[int(minutes[1])]} to"

        if hour > 12:
                hour -= 12
                if hour < 5:
                        timeof_day = "in the afternoon"
                else:
                        timeof_day = "in the evening" 
        else:
                if hour > 0 and hour < 5:
                        timeof_day = "at night"
                else:
                        timeof_day = "in the morning"

        #print time in a fancy way :D
        return print(f"""
         -------------------------------------------------------
        |                                                       |
            The time is {hour_milestone}{minutes_past} {times[hour]} {timeof_day}
        |                                                       |
         -------------------------------------------------------""")

user_choice = str(input("Use current time or input your own? (Cur/Own): "))
if user_choice.lower() == 'cur':
        run_loop = str(input("Would you like to run this app in a loop? (Y/N): "))
        repeat_time = int(input("How long do you want the loop time to be? (Seconds): "))
        print("To quit the program during the loop hold Q for more than 1 second!")

#infinite loop to run the program until user chose to quit
while True:
        try:
                if user_choice.lower() == 'cur':
                        if run_loop.upper() == 'Y':
                                translate_time(datetime.datetime.now().time())
                                for i in range(0, repeat_time):
                                        print(f"Waiting time left: {repeat_time - i}")
                                        time.sleep(1)
                                        if keyboard.is_pressed('Q'):
                                                quit()
                                os.system('cls')
                        else:
                                translate_time(datetime.datetime.now().time())
                                user_input = str(input("Type anything to continue, leave blank to exit."))
                                if not user_input:
                                        quit()
                                else:
                                        continue
                elif user_choice.lower() == 'own':
                        user_input = input("Input time in format xx:xx (leave empty to quit): ")
                        if not user_input:
                                quit()
                        translate_time(user_input)
                else:
                        user_choice = str(input("Use current time or input your own? (Cur/Own): "))
                        if user_choice.lower() == 'cur':
                                run_loop = str(input("Would you like to run this app in a loop every minute? (Y/N): "))
        except ValueError:
                print("Something went horribly wrong! Please restart the program.")