import pandas as pd
from os import path

def read_csv(file):
    dataSet = pd.read_csv(file)
    text = "Todas as linhas da tabela:"
    for index, line in dataSet.iterrows():  
       text += f'\n{line["Coluna1"]} {line["Coluna2"]} {line["Coluna3"]}'
    writeFile(text)

def create_file():
    new_file = "../assets/dados.txt"
    if not path.exists(new_file):
        file = open(new_file,"x")
        file.close()

def writeFile(text):
    new_file = "../assets/dados.txt"
    file = open(new_file,'w')
    file.write(text)
    file.close()


if __name__ == "__main__":
    file_name = "../assets/arquivo.csv"
    create_file()
    read_csv(file_name)