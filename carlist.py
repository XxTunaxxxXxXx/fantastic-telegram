import json

def screen_clear(): # clear terminal screen 
    import sys
    from os import system, name
    if name == 'nt':# for windows
        _ = system('cls')
    else:
        _ = system('clear')# for mac and linux

file_name = "carlist.json" #json file to parse through
car_list = [] 
i = 0 

with open(file_name, 'r') as json_file:
    car_list = json.load(json_file) 
    backup = input ('Enter backup json file name: ')
    backup += '.json'
    open_file = open(backup, "w")
    json.dump(car_list, open_file) 
    open_file.close()
    for a, b, c, d in car_list:
        if car_list[i][a] == "wtfbbq":
            print ('       Year: ', car_list[i][b])
            print ('       Make: ', car_list[i][c])
            print ('      Model: ', car_list[i][d],'\n')
            print ('Leave blank to skip, enter \'save\' to save json list to file and exit')
            newOrdinal = input ('Enter Car Ordinal: ')
            if newOrdinal.upper() == "SAVE":
                screen_clear()
                open_file = open(file_name, "w")
                json.dump(car_list, open_file)
                file_name.close()
                print ('Dictionary has been saved to ', file_name)
                break
            elif newOrdinal.isnumeric():
                car_list[i][a] = int(newOrdinal)
                input ('Updated, press enter to continue')
                screen_clear()
                i += 1
            elif newOrdinal == "":
                input ('Car skipped')
                screen_clear()
                i += 1
            else:
                input ('Invalid input, press enter to continue')
                screen_clear()
        else:
            i += 1
input('\nDone, press enter')
