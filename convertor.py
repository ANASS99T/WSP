import json
import pandas as pd
from Extract_Filtre import *



def to_table(new_data):
    for i in range(len(new_data)):
        df = pd.DataFrame(data=new_data[i], index=[i])
        df = (df.T)
        print(df)


def generate_data(new_data, file):
    f = open(file, "w+")

    for i in range(len(new_data)):
        df = pd.DataFrame(data=new_data[i], index=[i])
        df = (df.T)
        f.write(df.to_string(header=False, index=False))
        f.write("\n\n\n")
    f.close()
