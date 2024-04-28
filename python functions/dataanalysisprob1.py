import urllib.request
import os

os.makedirs('./Data Analysis Problems',exist_ok=True)

with open('./Data Analysis Problems/DigiDB_digimonlist.csv') as digimon_db:
    digimon_details = digimon_db.readlines()
    print(digimon_details[1].strip().split(','))
    
    
def parse_values(dataset):
    value = []
    for item in dataset.split(','):
        try:
            value.append(float(item))
        except ValueError:
            value.append(item)
    return value

digimon_dataset = parse_values(digimon_details)
print(digimon_dataset)
            
            
    


