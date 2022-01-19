import socket
import parser
import threading
import sys
import json
from os import system, name

def screen_clear(): # clear terminal screen 
    if name == 'nt':# for windows
        _ = system('cls')
    else:
        _ = system('clear')# for mac and linux


def serverBackground(): 
    while True:
        global newOrdinal
        data, addr = serverSock.recvfrom(323)
        newOrdinal = parser.getCarOrdinal(data)

if __name__ == "__main__":
    port_number = 5300  #port to listen to, can be changed as needed
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    newOrdinal = ""

    print("Local IP address is : " , local_ip)   
    print("\nListening port is : ", port_number)  
    input("Press enter to continue")
    screen_clear()

    serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSock.bind((local_ip, port_number))

    serverThread = threading.Thread(target=serverBackground)
    serverThread.start()

    file_name = "carlist.json" #json file to parse through
    car_list = [] 
    i = 0  #for counter

    with open(file_name, 'r') as json_file:
        car_list = json.load(json_file) 
        backup = input ('Enter backup json file name: ')
        backup += '.json'
        open_file = open(backup, "w")
        json.dump(car_list, open_file) 
        open_file.close()

        for a, b, c, d in car_list:
                if car_list[i][a] == "wtfbbq":
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
                        print ('Dictionary has been saved to ', file_name)
                        break
                    elif menu == '1':
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
    sys.exit(__main__)
    







