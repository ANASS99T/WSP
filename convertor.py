import pandas as pd
from Extract_Filtre import *



def to_table(new_data):
    for i in range(len(new_data)):
        df = pd.DataFrame(data=new_data[i], index=[i])
        df = (df.T)
        print(df)


def generate_data(new_data, file):

    for i in range(len(new_data)):
        df = pd.DataFrame(new_data, columns=['name','work','image','description','label'])
        print(df)

    #df.to_csv(file)

