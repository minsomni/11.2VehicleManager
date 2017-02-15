# coding=utf-8

#########################################
### Homework 11.2: Vehicle Management ###
#########################################
# Das Programm erstellt eine editierbare Liste
# von Vehicle-Objekten. Die Liste wird beim Beenden
# in eine Textdatei geschrieben, die beim nächsten
# Start wieder eingelesen wird.
#########################################

### global variables
allVehicles = [] # holds all Vehicle-Objects

class Vehicle(object):
    def __init__(self,brand,model,km,service):
        self.brand = brand
        self.model = model
        self.km = km
        self.service = service

    def edit_km(self,km):
        self.km = km

    def edit_service(self,service):
        self.service = service

    def list_data(self):
        a = self.brand + " " + self.model + " (" + self.km + " km), Next Service: " + self.service
        return a

def import_data(): #liest Daten aus Textdatei, falls vorhanden
    try:
        with open("vehicles.txt", "r") as f:
            input = f.readlines()

            for i in input:
                data = i.split("//")
                for lines in data:
                    cardata = lines.split("::")
                    brand = cardata[0]
                    model = cardata[1]
                    km = cardata[2]
                    service = cardata[3]
                    newCar = Vehicle(brand, model, km, service)
                    allVehicles.append(newCar)

    except IOError:
        print("io error")
    except IndexError:
        print("index error")

def save_data(): #schreibt alle Objekte von allVehicles-Liste in eine Datei
    with open("vehicles.txt","w") as file:
        for i,j in enumerate(allVehicles):
            brand = allVehicles[i].brand
            model = allVehicles[i].model
            km = allVehicles[i].km
            service = allVehicles[i].service

            file.write(brand + "::" + model + "::" + km + "::" + service + "//")

def addCar():
    print("\n" * 5)
    print("### Add a car ###")
    brand = raw_input("Brand: ")
    model = raw_input("Model: ")
    km = raw_input("Km: ")
    service = raw_input("Next Service: ")
    newCar = Vehicle(brand,model,km,service)
    allVehicles.append(newCar)

def showList():
    print("\n" * 5)
    while True:
        print("\n" * 2)
        print("### List of Vehicles ###")
        for index, i in enumerate(allVehicles):
            print("(" + str(index) + ") " + i.list_data())
        print("(B)ack to main menu")

        listSelection = raw_input("Which Vehicle would you like to edit? ").lower()

        if listSelection == "b":
            return None

        try:
            if int(listSelection) < len(allVehicles):
                selected_car = allVehicles[int(listSelection)]
                print selected_car.list_data()
                newKm = raw_input("Enter new km (or leave empty to skip): ")
                newService = raw_input("Enter next Service date (or leave empty to skip): ")
                deleteCar = raw_input("Do you want to delete this entry (y)es, leave empty to skip): ").lower()
                if newKm:
                    selected_car.edit_km(newKm)
                if newService:
                    selected_car.edit_service(newService)
                if deleteCar == "y":
                    allVehicles.remove(selected_car)

        except ValueError:
            print("Error")

def main():
    import_data()

    while True:
        print("\n" * 5)
        print("### V E H I C L E   M A N A G E R ###")
        print("(1) Add a new car")
        print("(2) Show List")
        print("(3) Exit")

        menuSelection = str(raw_input("Please select: ")).lower()

        if menuSelection == "1":
            addCar()
        elif menuSelection == "2":
            showList()
        elif menuSelection == "3":
            save_data()
            print("Good Bye")
            exit()

if __name__ == '__main__': main()


