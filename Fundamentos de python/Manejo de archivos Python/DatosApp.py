from Datos import *
import csv

dat = []

with open("C:\\Users\\SENA\\Downloads\\Saber_11__2019-2.csv") as cvsDatafile:
    csvReader = csv.reader(cvsDatafile)
    

    for row in csvReader:
        objecto = (row[1], row[2], row[3], row[4])

    print(objecto.verDatos())
    Icfes.append(objecto)   

    for Ic in Icfes:
        print(Ic.getDocumento())
        print(Ic.getGenero())
        print(Ic.getCorreo())
        print(Ic.getTelefono())


