def buscar_datos(*args, **kwargs):
    
    datos_encontrados = []

    if "database" in kwargs:

        database = kwargs["database"]

        for arg in args:

            found = False

            for key, data in database.items(): 
    
                if arg in data.values():

                    datos_encontrados.append(arg)

                    found = True

                    break

            if not found:

                print(f"Palabra '{arg}' no se encuentra en la base de datos.")
    print("Se encuentran datos en la base de datos:", datos_encontrados)

    return datos_encontrados

database = {
    "persona1": {
        "primer_nombre": "Pablo",
        "segundo_nombre": "Diego",
        "primer_apellido": "Ruiz",
        "segundo_apellido": "Picasso"
    },

     "persona2" : {
         "primer_nombre": "Martino",
         "segundo_nombre": "Agustin",
         "primer_apellido": "Vespa",
         "segundo_apellido": "Stacchiola"  
     }
}

buscar_datos("Martino", "Agustin", "Vespa", "Stacchiola", database=database)