from Connection_Collection import *
from Extract_Filtre import *

def main():
    link = 'https://www.linkedin.com/uas/login'
    browser = connection(link)
    name_div = collection(browser)

    Extracted = Extract(name_div)
    print(len(Extracted)," data are found")
    print("Extracted data are : \n", Extracted)

    Filtered = Filtre(Extracted)
    print(len(Filtered), " data are found")
    print("Filtred data are : \n", Filtered)


    print("\nemails : ")
    email(Filtered)
    
    

if __name__ == "__main__":
    main()
