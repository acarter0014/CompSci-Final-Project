#Car sales application
import sys
isContinued = True
checkCar = True
checkEng = True
checkRun = True

veh = [20000, 25000]
eng = [10000, 20000]



print("Hello, please insert your vehicle specifications from the options below:")



priceList = []
vehList = []

class Car:
    def __init__(self, veh, engine):
        self.veh = veh
        self.engine = engine

while isContinued == True:

    while checkCar == True:

        carType = input("Vehicle type(Coupe, Truck): ")

        if carType == "Coupe":
            checkCar == False
            vehPrice = veh[0]
            break

        elif carType == "Truck":
            checkCar == False
            vehPrice = veh[1]
            break
        else:
            checkCar == True
            print("Incorrect vehicle type: check capitalization")
            
    while checkEng == True:

        engSize = input("Engine size(V6, V8): ")

        if engSize == "V6":
            checkEng == False
            engPrice = eng[0]
            break
        
        elif engSize == "V8":
            checkEng == False
            engPrice = eng[1]
            break
        else:
            checkEng == True
            print("Incorrect engine size: check capitalization")

    def addPrice(vehPrice, engPrice):
        totalPrice = vehPrice + engPrice
        return totalPrice

    finalPrice = addPrice(vehPrice, engPrice)


    if finalPrice == 30000:
        v1 = Car("Coupe", "V6")
        vehList.append("V6 Coupe")
        priceList.append(30000)
    elif finalPrice == 40000:
        v1 = Car("Coupe", "V8")
        vehList.append("V8 Coupe")
        priceList.append(40000)
    elif finalPrice == 35000:
        v1 = Car("Truck", "V6")
        vehList.append("V6 Truck")
        priceList.append(35000)
    else:
        vehList.append("V8 Truck")
        v1 = Car("Truck", "V8")
        priceList.append(45000)



    print("Vehicle added to cart for: $" +str(finalPrice))
    print("Listed below are your current vehicles with their corresponding prices underneath:")
    print(vehList)
    print(priceList)

    overallCost = sum(priceList)
    receiptText = "Thank you for shopping, your total is: $" + str(overallCost)

    print("Your current total price is: $" + str(overallCost))

    while checkRun == True:

        keepRunning = input("Would you like to purchase another vehicle?(Yes or No): ")

        if keepRunning == "Yes":
            isContinued == True
            checkCar == True
            checkRun == False
            break
        elif keepRunning == "No":
            printReceipt = open('receipt1.txt', 'w')
            printReceipt.write(receiptText)
            printReceipt.close()
            print(receiptText)
            isContinued == False
            checkRun == False
            sys.exit()
        else:
            isContinued == False
            checkRun == True
            print("Please answer Yes or No, check capitalization.")
           


