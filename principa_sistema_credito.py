import funcion_sistema_credito as fn

alumnos = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez",   
           "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
creditos_alumnos = {}
eleccion = " "
while eleccion != "5":
    print("1.Aignar créditos")
    print("2.Clasificar créditos")
    print("3.Cálculo de estadísticas de créditos ")
    print("4.Generar reporte")
    print("5.Salir")
    eleccion = input("Ingresa una opción: ")

    if eleccion == "1":
        print("="*60)
        fn.generar_creditos(creditos_alumnos,alumnos)

    elif eleccion =="2":
        print("="*60)
        fn.clasificar(creditos_alumnos)

    elif eleccion == "3":
        print("="*60)
        fn.estadisticas(creditos_alumnos)

    elif eleccion == "4":
        print("="*60)
        fn.reporte(creditos_alumnos)

    else:
        print("Opción incorrecta")