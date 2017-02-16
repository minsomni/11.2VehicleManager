# coding=utf-8

#########################################
#### Homework 11.2: Vehicle Manager ####
#########################################
# Das Programm erstellt eine editierbare Liste
# von Vehicle-Objekten. Die Liste wird beim Beenden
# in eine Textdatei geschrieben, die beim nächsten
# Start wieder eingelesen wird.
#########################################

# globale variable
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

def showList(): #zeigt Objekte der allVehicles-Liste. Einträge können editiert werden (km, service date, löschen)
    print("\n" * 5)
    while True:
        print("\n" * 2)
        print("### LIST OF VEHICLES ###")
        for index, i in enumerate(allVehicles):
            print("(" + str(index) + ") " + i.list_data())

        listSelection = raw_input("\nWhich Vehicle would you like to edit? (press enter to return to main menu)").lower()

        if listSelection == "":
            return None

        try:
            if int(listSelection) < len(allVehicles):
                selected_car = allVehicles[int(listSelection)]
                print selected_car.list_data()
                newKm = raw_input("Enter new km (press enter to skip): ")
                newService = raw_input("Enter next Service date (press enter to skip): ")
                deleteCar = raw_input("Do you want to (d)elete this entry? (press enter to skip): ").lower()
                if newKm:
                    selected_car.edit_km(newKm)
                if newService:
                    selected_car.edit_service(newService)
                if deleteCar == "d":
                    allVehicles.remove(selected_car)

        except ValueError:
            print("Error")

def addCar(): #erzeugt neues Vehicles-Objekt und fügt es der allVehicles-Liste hinzu
    print("\n" * 5)
    print("### ADD NEW CAR ###")
    brand = raw_input("Brand: ")
    model = raw_input("Model: ")
    km = raw_input("Km: ")
    service = raw_input("Next Service: ")
    newCar = Vehicle(brand,model,km,service)
    allVehicles.append(newCar)

if __name__ == '__main__':
    import_data()

    while True:
        print("\n" * 5)
        print("#####################################")
        print("### V E H I C L E   M A N A G E R ###")
        print("#####################################")
        print("(1) Show List")
        print("(2) Add a new car")
        print("\n(E)xit Vehicle Manager\n")

        menuSelection = str(raw_input("Please select: ")).lower()

        if menuSelection == "1":
            showList()
        elif menuSelection == "2":
            addCar()
        elif menuSelection == "e":
            save_data()
            print("Good Bye")
            exit()