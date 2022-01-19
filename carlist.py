import socket
import sys
import json
from forzatelemetry import Telemetry, ForzaListen
from os import system, name

file_name = "carlist.json"               #json file to parse through
port_number = 5300                       #port to listen to, can be changed as needed
car_list = []                            #for json array

# clear terminal screen
def screen_clear(): 
    if name == 'nt':# for windows
        _ = system('cls')
    else:
        _ = system('clear')# for mac and linux

def debug():
    print (newOrdinal)

#loads json file to dictionary, then runs though list finding carOrdinals that aren't set 
def main():
    with open(file_name, 'r') as json_file:
        car_list = json.load(json_file) 
        backup = input ('Enter backup json file name: ')
        backup += '.json'
        open_file = open(backup, "w")
        json.dump(car_list, open_file) 
        open_file.close()
        
        #quick option to skip the start of the list if you had a stopping point
        print ('Enter start index, leave blank to start on 0')
        print ('Invalid input will default to 0')
        i = input ('Index :')         
        if i.isnumeric():
            i = int(i)
            if i >= 0 and i <= len(car_list):
                pass
            else:
                i = 0
        else:
            i = 0

        for a, b, c, d in car_list: #a= Year b=Make c=Model d=carOrdinal
                if car_list[i][a] == "wtfbbq":   #wtfbbq is the placeholder in the json for carOrdinal's that are not set 
                    print (f'{car_list[i][b]} {car_list[i][c]} {car_list[i][d]}') #Year Make Model
                    print ('\n1: Save Current Car Ordinal')
                    print ('\n2: Skip Current Car')
                    print ('\n3: Save New Json Updates To File And Exit')
                    menu = input('\nEnter 1, 2, or 3: ')
                    if menu == '3':
                        screen_clear()
                        open_file = open(file_name, "w")
                        json.dump(car_list, open_file)
                        open_file.close()
                        print (f'Dictionary has been saved to {file_name}')
                        print (f'\n Last used index was {i}')
                        break
                    elif menu == '1':
                        forzaData.dataRefresh(server.recieve())
                        if newOrdinal == 0:
                            input('Car Ordinal currently 0, only save in free roam')
                            screen_clear()
                        else:
                            car_list[i][a] = int(newOrdinal)
                            i += 1
                            screen_clear()
                    elif menu == '2':
                        i += 1
                        screen_clear()
                    else:
                        input('Invalid Choice, press enter to continue')
                        screen_clear()
                else:
                    i += 1
        input('\nDone, press enter')

if __name__ == "__main__":
    server = ForzaListen(port_number)     #initialize server with set port
    print(f"Local IP address is : {server.local_ip}")   
    print(f"\nListening port is : {server.port}")  
    input("Press enter to continue")
    screen_clear()

    server.start()      #start listening to for incoming data

    forzaData = Telemetry(server.recieve())
    newOrdinal = forzaData.getCarOrdinal() #set variable to return current carOrdinal
    #debug()
    main()








