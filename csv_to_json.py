#converts input csv file to json
import csv
import json

def csv_to_json(inputpath, outputpath): #input csv file, output json file 
    car_list = []
    csv_file = csv.DictReader(open(inputpath))
    for row in csv_file:
        csv_list.append(row)
        
    print ('CSV has been Imported to Dictionary\n')
    file_out = open(outputpath, "w")
    json.dump(csv_list, file_out)
    f.close()
    print ('Dictionary has been saved to ', file_out)
