import time
def Countdown(minutes):
    print(minutes, " minutes left.")
    while minutes > 0:
        time.sleep(60)
        minutes = minutes-1
        print(minutes, " minutes left.")
    print("Bang!!")

minutes = input("Set the time!")
minutes = int(minutes)

Countdown(minutes)
