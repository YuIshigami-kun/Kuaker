from include import card, internet, bin, bruteForce, dorker, ip, phone
from threading import Thread
from os import name, system
from time import sleep

def cls():
    if name == 'nt':
        system("cls")
    else:
        system("clear")


if __name__ == '__main__':
    __datafile__ = "./save-files/data.txt"

    try:
        f = open(__datafile__, 'r')
        __user__ = f.read().split(',')[0]
        f.close()

    except:
        __user__ = "user"
    
    __command__ = ""
    __conected__ = internet.check()

    while(__command__ != "break"):
        __command__ = str(input(f"<{__user__}> "))

        if(__command__ == "clear"):
            cls()

        elif(__command__[0:7] == "setUser"):
            x = __command__.split()

            __user__ = x[1]

            f = open(__datafile__, 'w')
            f.write(x[1] + ',')
            f.close()

            del x, f

        elif(__command__ == "help" or __command__ == "?"):
            print("Help menu: \n\nclear - Clear console \nhelp|? - Show help menu \nsetUser <username> - Set a new username \nbin <bin> - Check bin info \ngen bin=<bin> month=<month> year=<year> cvv=<cvv> - Gen 10 cards(month, year and cvv are optional) \nbruteforce - Starts the bruteforce tool \ndorker <dork> - Search for a dork in google.com \nip <ip> - Gets information about an IP (can be IPV4 and IPV6) \nphone <phone number> - Gets information about a phone number \nbreak - Exit kuaker")

        elif(__command__[0:3] == "bin"):
            if(__conected__ == False):
                print("You need conection to use this tool!")
            else:
                x = __command__.split()

                r = bin.getInfo(x[1])
                if(r == False):
                    print("Not found!")
                else:
                    print(f"Type: {r['type']} \nPrepaid: {r['prepaid']} \nCountry: {r['country']} \nBank: {r['bank']}")
                
                del x, r
            
        elif(__command__[0:3] == "gen"):
            x = __command__.split()
            bin = ""
            month = "#"
            year = "#"
            cvv = "#"

            for i in x:
                if(i.find("bin=") != -1):
                    bin = i[4:len(i)]

                elif(i.find("month=") != -1):
                    month = i[6:len(i)]

                elif(i.find("year=") != -1):
                    year = i[5:len(i)]

                elif(i.find("cvv=") != -1):
                    cvv = i[4:len(i)]

            if(bin == "" or len(bin) > 15):
                print("Invalid bin!")

            else:
                for i in card.gen(bin, month, year, cvv):
                    print(i)

            del x, bin, month, year, cvv

        elif(__command__[0:10] == "bruteforce"):
            lChars, uChars, nums, sim = "", "", "", ""

            lChars = str(input("Use lowercase chars(y/n): "))
            uChars = str(input("Use uppercase chars(y/n): "))
            nums = str(input("Use numbers(y/n): "))
            sim = str(input("Use special characters(y/n): "))

            n = int(input("Enter the max length of the passwords: "))
            f = str(input("Enter the result file name (default pass.txt): "))

            if(f == ""):
                x = Thread(target = bruteForce.genDict, args = (lChars, uChars, nums, sim, n,))
            else:
                x = Thread(target = bruteForce.genDict, args = (lChars, uChars, nums, sim, n, f,))
            x.start()
            
            while(x.is_alive()):
                try:
                    cls()
                    print("Generating dictionary... \nNumber of passwords made: " + str(bruteForce.getCount()) + "\nPress ctr+c to stop the process")
                    sleep(0.5)
                except KeyboardInterrupt:
                    print("Stopping...")
                    bruteForce.stopProcess()
                    break

            del lChars, uChars, nums, sim, n, f, x

        elif(__command__[0:4] == "dork"):
            x = __command__.split(' ')
            
            for i in dorker.get_urls(x[1]):
                print(i + '\n')

            del x

        elif(__command__[0:2] == "ip"):
            x = __command__.split(' ')

            r = ip.getInfo(x[1])

            if(r["status"] == "success"):
                print(f'IP FOUND! \nLocation: {r["country"]}/{r["city"]} \nCoordinates: lat {r["lat"]}, lon {r["lon"]} \nZip: {r["zip"]} \nISP: {r["isp"]}')
            else:
                print("IP NOT FOUND")

            del x, r

        elif(__command__[0:5] == "phone"):
            x = __command__.split(' ')

            r = phone.getInfo(x[1])
            print(f'Location: {r["city"]} \nCarrier: {r["carrier"]}')

            del x, r
        print("")