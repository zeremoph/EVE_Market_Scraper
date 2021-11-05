
# Készítette Zeremoph


import requests
from datetime import datetime

HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0 :D ) Gecko/20100101 Firefox/93.0', }


def EMS():
    Command_1 = input("EMS> ")
    Command = str(Command_1)
    check = int(0)

    if Command == "help":
        check = 1
    if Command == "h":
        check = 1

    if Command == "Help":
        check = 1

    if Command == "set":
        check = 2

    if Command == "Set":
        check = 2

    if check == 0:
        check = 3



    # ------------------------------------------------------------------------------------------------------------------

    if check == 3: # DEBUG, rossz parancs ellenőrző!
        print("rossz parancs!")

    if check == 1: # Ez a help parancs
        print("Parancsok:" "\n" "set, Set --> főparancs")

    if check == 2: # Fő része a programnak
        Item_Command = input("Adja meg az item ID-t: ")
        Item_id = str(Item_Command)
        print("ItemID= ", Item_id)
        Region_Command = input("EMS set RegionID> ")
        Region_ID = str(Region_Command)
        print("RegionID=", Region_ID)



        url = str('https://api.evemarketer.com/ec/marketstat/json?typeid=' + Item_id + '&regionlimit=' + Region_ID)
        

        x = requests.get(url, headers=HEADERS)

        print("Az eredmény le lett mentve")

        most = datetime.now()
        ido = most.strftime("%d_%m_%Y_%H_%M_%S")
        nev = str(ido)
        file = open(nev + '.json', 'a')
        file.write(x.text)
        file.close()


if __name__ == '__main__':
    EMS()
