import csv
import os
import string
import random

file_name = "../assets/arquivo.csv"

def create_file():
   
    if not os.path.exists(file_name):
        file = open(file_name,"x")
        file.close()

def create_random_text(length,upper):
    if upper:
        letters = string.ascii_uppercase
    else:
        letters = string.ascii_lowercase

    letters = ''.join([letters,'0','1','2','3','4','5','6','7','8','9'])


    text = ''.join(random.choice(letters) for index in range(length))

    return text


def write_csv():
    file = open(file_name,'w',newline='')
    writer = csv.writer(file,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['Coluna1','Coluna2','Coluna3'])
    for i in range(3000):
        row = [create_random_text(3,True),create_random_text(5,True),create_random_text(20,False)]
        writer.writerow(row)
    file.close()



def main():
    create_file()
    write_csv()
    

main()