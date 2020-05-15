cmd = ""
started = False
while True:
    cmd = input('>').upper()
    if cmd == 'START':
        if started:
            print("What are you doing the car has already started!!!")
        else:
            print("Car started...Ready to go!")
            started = True
    elif cmd == 'STOP':
        if not started:
            print("What the hell are you doing the car has already stopped!!!")
        else:
            print("Car has stopped!")
            started = False
    elif cmd == 'HELP':
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif cmd == 'QUIT':
        break
    else:
        print("Hey!..I don't understand that")
