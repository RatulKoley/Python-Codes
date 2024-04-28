import math
import os
import urllib.request
# print(os.getcwd())
# print(os.listdir('.')) #showing folders in current path
os.makedirs('./newdir',exist_ok=True)
'newdir' in os.listdir('.')

urllib.request.urlretrieve(url=
'https://sample-videos.com/text/Sample-text-file-10kb.txt',
filename='./newdir/textfile2.txt')

#Read Downloaded File
text_file = open('./newdir/textfile.txt',mode='r')
#This Process Is To Read File

#Now This File Is To Print The File Data By Converting it to string type
file_contains = text_file.read()
print(file_contains)

#We have to close the open files otherwise it will store on RAM
text_file.close()

#We can also use "WITH OPEN" to automatically close the file after Read
with open('./newdir/textfile2.txt') as text_file_auto:
    text_file_auto_contains = text_file_auto.read()
    print(text_file_auto_contains)
    
#We can print each line individually by 'readlines()'
with open('./newdir/textfile2.txt') as text_file_auto:
    text_file_lines = text_file_auto.readlines()
    print(text_file_lines)
    
    
#Single Line
print(text_file_lines[0])

#Remove \n or empty character
print(text_file_lines[0].strip())

#Separate Each Value By Comma and Conver to float
text_file_lines[0].strip().split(',')

def parse_values(data_line):
    values = []
    for item in data_line.strip().split(','):
        values.append(float(item))
    return values

parse_values(text_file[1])

#Debugging Empty String Cases / Edge Case
def parse_values(data_line):
    values = []
    for item in data_line.strip().split(','):
        if(item == ''):
            values.append(0.0)
        else:
            values.append(float(item))
    return values


#Now we are going to make a dictionary with those headers and values
def create_dic(headers,values):
    result = {}
    for key,value in zip(headers,values):
        result[key] = value
    return result

 #Write Operation
with open('./newdir/textfile2.txt' , 'w') as f:
    for loan in text_file:
        f.write('{},{},{},{},{}\n'.format(
            loan['amount'],
            loan['duration'],
            loan['rate'],
            loan['down_payment'],
            loan['emi'],
        ))
        
# Join Headers With Comma
(',').join(text_file) + '\n'

