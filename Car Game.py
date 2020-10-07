
'''
First_Command = input(">: ")

if First_Command == "help":
    print("Simulator begins")
    
    conditions = input("Enter (Start) or (Stop) or (Quit)")
    if conditions == "Start":
        print("Start the Engine")
    elif conditions == "Stop":
        print("Stop the Engine")
    else:
        print("Terminator")

'''

#Second Solution
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started")
        else:
            started = True
            print("Start the Engine")
    elif command == "stop":
        if not started:
            print("Car already stopped")
        else:
            started = False
            print("Stop the Engine")
    elif command == "help":
        print("""
Start - Start the Engine
Stop - Stop the Engine 
Quit - Quit the Engine
        
        """)
    elif command == "quit":
        break
    else:
        print("You made the wrong selection")








