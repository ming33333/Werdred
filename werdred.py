#create time 
import json 
import time
import threading
import constants as constants
from playerData import stats




pause_event = threading.Event() 
global endgame
endgame = False

'''
Functions
'''
def coordinationLocation(grid):
    mapCoordinates = {}
    for x,lines in enumerate(grid):
        for y,locations in enumerate(lines):
            if locations:
                mapCoordinates[locations]=[x,y]
    return mapCoordinates
def coordinationDifference(firstLocation,secondLocation):
    return (abs(firstLocation[0]-secondLocation[0])+abs(firstLocation[1]-secondLocation[1]))*10

def statDisplay():
    global stats
    print('Current Stats')
    print(json.dumps(stats,indent=4))

def clock_time(stopTimer=False):
    while not stopTimer:
        if endgame:
            stopTimer = True
        elif pause_event.is_set():
            hours, mins = divmod(stats["time"]*60, 60)
            time_format = 'time is {:02d}:{:02d}'.format(int(hours), int(mins))
            print(time_format, end='\r')  # End with \r to overwrite the line
            time.sleep(1)
            stats["time"] += 1 / 60  # Update stats time, converting seconds to minutes
def updateTime(addTime):
    print("addTime",addTime)
    stats["time"] += addTime
    if stats["time"] >= 24:
        stats["time"] += -24
        stats["dayWeek"] = constants.weekdays[(constants.weekdays.index(stats["dayWeek"]) + 1) % 7]

def standing():
    print("You are standing in",stats["currentPlace"])
    resume()

def work():
    print("Working....")
    if stats["job"] == "Unemployed":
        print("You are unemployed. Please find a job.")
        print("Choose a job from the following options:")

        for i, job in enumerate(constants.jobs, 1):
            print(f"{i}. {job}")
        stats["jobChoice"] = int(input("Enter the number of the job you want: \n"))
        if 1 <= stats["jobChoice"]  <= len(constants.jobs):
            stats["job"] = constants.jobs[stats["jobChoice"]  - 1]
            print(f"You are now employed as a {stats['job']}.")
        else:
            print("Invalid choice. You remain unemployed.")
    else:
        print("You are employed as a",stats["job"])
        print("You earned 100 dollars.")
        stats["money"] += stats["job"][stats["joblevel"]]
    updateTime(8)
    resume()

def travel():
    print("Traveling....")
    destination = input("Enter destination: \n")
    while destination not in constants.districts:
        print("Invalid destination. Please enter a valid district.")
        destination = input("Enter destination: \n")
    current_location = stats["currentPlace"]
    travel_time = coordinationDifference(mapCoordinates[current_location], mapCoordinates[destination])
    updateTime(travel_time/60)
    stats["currentPlace"] = destination
    print(f"Traveled to {destination}. It took {travel_time} minutes.")
    resume()

def endgameOption():
    print("Sad to see you go")
    return True

def options_selector(functions):
    print("Select a options to execute:")
    pause()
    for i, func in enumerate(functions, 1):
        print(f"{i}. {func.__name__}")
    choice = int(input("Enter number: \n"))
    if 1 <= choice <= len(functions):
        quitGame = functions[choice - 1]()
    else:
        print("Invalid choice")
    return quitGame if quitGame is not None else False

def pause():
    pause_event.clear()

def resume():
    pause_event.set()

if __name__ == "__main__":
    global mapCoordinates
    mapCoordinates = coordinationLocation(constants.grid)
    pause_event.set()
    # Start the countdown timer in a separate thread
    timer_thread = threading.Thread(target=clock_time)
    timer_thread.start()
    time.sleep(1)  # Give the timer thread time to start
    print()
    print("Welcome to Werdred")
    while not endgame:
        statDisplay()
        user_input = input("Enter 1 to see the options selector: \n")
        if user_input == "1":
            endgame = options_selector([standing, travel, endgameOption,work])
            print("endgame is set to:", endgame)
    # Ensure the timer thread is stopped before exiting
    timer_thread.join()
    print("game end")

print(coordinationLocation(constants.grid))
print(coordinationDifference(coordinationLocation(constants.grid)["Dewmist"],coordinationLocation(constants.grid)["Semba"]))