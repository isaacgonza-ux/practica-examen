import random
import csv

def generar_creditos(creditos_alumnos,alumnos):
    for i in alumnos:
        creditos = random.randint(50,200)
        creditos_alumnos[i] = creditos
    print("Créditos generados correctamente")
    print(creditos_alumnos)

def clasificar(creditos_alumnos):
    menor_100 = {}
    entre_100_150 = {}
    mayor_150 = {}
    if not creditos_alumnos:
        print("Primero debes generar créditos")

    else:
        for alumno,credito in creditos_alumnos.items():
            if credito < 100:
                menor_100[alumno] = credito
            elif credito >= 100 and credito <= 150:
                entre_100_150[alumno] = credito
            else:
                mayor_150[alumno] = credito

                
            print("Créditos menores a 100:",len(menor_100))
            for alumno,credito in menor_100.items():
                print(f"{alumno} $ {credito}")

            print("="*50)
            print("Créditos entre 100 y 150:",len(entre_100_150))
            for alumno,credito in entre_100_150.items():
                print(f"{alumno} ${credito}")

            print("="*50)
            print("Créditos de más de 150:",len(mayor_150))
            for alumno,credito in mayor_150.items():
                print(f"{alumno} $ {credito}")


def estadisticas(creditos_alumnos):
    creditos = list(creditos_alumnos.values())
    if not creditos_alumnos:
        print("Primero genera créditos")
    else:
        credito_max = max(creditos)
        min_credito = min(creditos)
        promedio_credito = sum(creditos) /len(creditos_alumnos)
        print(f"El crédito máximo es : {credito_max}")
        print(f"El crédito minimo es : {min_credito}")
        print(f"El promedio de créditos es : {promedio_credito}")


def reporte(creditos_alumnos):
    if not creditos_alumnos:
        print("Pirmero genere créditos")
    else:
        try:
            with open("Reporte_créditos.csv","w",newline="") as archivo:
                escritor = csv.writer(archivo,delimiter=",")
                escritor.writerow(["Nombre","Crédito"])
                for i in creditos_alumnos:
                    escritor.writerow([i,creditos_alumnos[i]])
                print("Reporte generado correctamente")
        except ExceptionGroup as error:
            print("Error al generar",error)