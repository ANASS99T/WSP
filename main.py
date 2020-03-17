from Connection_Collection import *
from Extract_Filtre import *
from convertor import *

def main():
    
    link = 'https://www.linkedin.com/uas/login'
    browser = connection(link)
    name_div = collection(browser)

    #Extract data
    Extracted = Extract(name_div)
    print(len(Extracted)," data are found")
    print("Extracted data are : \n", Extracted)

    #Filtre data
    Filtered = Filtre(Extracted)
    print(len(Filtered), " data are found")
    print("Filtred data are : \n", Filtered)

    #Get data with email
    NewFiltered = email(Filtered)
    print("\nFiltred data with emails : \n", NewFiltered, "\n", len(NewFiltered), " data are found")
    
    #transfer data to table
    print()
    to_table(NewFiltered)

    #generate csv file
    generate_data(NewFiltered, "data.csv")
    print("data are saved in .\\WSP\\data.csv")



if __name__ == "__main__":
    main()
