
clientes= {1:"id", 2:"clientes"},
{"id":1,
            "Nombre":"Carlos",
            "Apellido":"Alberto",
            "Direccion":"Calle 1 #2",
            "Telefono":"315789560",
            "Servicio":"",
            "Categoria":"Cliente Nuevo",
            "Sugerencia":"",
            "Reclamos":"",
            "Consultas":"" },
{"id":2,
            "Nombre":"Sebastian",
            "Apellido":"Gutierrez",
            "Direccion":"Calle 1 #3",
            "Telefono":"310788789",
            "Servicio":"",
            "Categoria":"Cliente Nuevo",
            "Sugerencia":"",
            "Reclamos":"",
            "Consultas":""
        },
{"id":3,
            "Nombre":"Jesus",
            "Apellido":"Perez",
            "Direccion":"Calle 1 #4",
            "Telefono":"311689560",
            "Servicio":"",
            "Categoria":"Cliente Nuevo",
            "Sugerencia":"",
            "Reclamos":"",
            "Consultas":""
        },
{"id":4,
            "Nombre":"Andres",
            "Apellido":"Guerrero",
            "Direccion":"Calle 1 #5",
            "Telefono":"312789560",
            "Servicio":"",
            "Categoria":"Cliente Regular",
            "Sugerencia":"",
            "Reclamos":"",
            "Consultas":""
        },
{"id":5,
            "Nombre":"Miguel",
            "Apellido":"Martiez",
            "Direccion":"Calle 1 #6",
            "Telefono":"313789760",
            "Servicio":"",
            "Categoria":"Cliente Regular",
            "Sugerencia":"",
            "Reclamos":"",
            "Consultas":""
        },
{"id":6,
            "Nombre":"Danna",
            "Apellido":"Guerrero",
            "Direccion":"Calle 1 #7",
            "Telefono":"314758560",
            "Servicio":"",
            "Categoria":"Cliente Regular",
            "Sugerencia":"",
            "Reclamos":"",
            "Consultas":""
        },
{"id":7,
            "Nombre":"Camila",
            "Apellido":"Corzo",
            "Direccion":"Calle 1 #8",
            "Telefono":"319789560",
            "Servicio":"",
            "Categoria":"Cliente leal",
            "Sugerencia":"",
            "Reclamos":"",
            "Consultas":""
        },
{"id":8,
            "Nombre":"Jennifer",
            "Apellido":"Jaimes",
            "Direccion":"Calle 1 #9",
            "Telefono":"317789560",
            "Servicio":"",
            "Categoria":"Cliente leal",
            "Sugerencia":"",
            "Reclamos":"",
            "Consultas":""
        },
{"id":9,
            "Nombre":"Tatiana",
            "Apellido":"Cortez",
            "Direccion":"Calle 1 #10",
            "Telefono":"318789560",
            "Servicio":"",
            "Categoria":"Cliente leal",
            "Sugerencia":"",
            "Reclamos":"",
            "Consultas":""
        }

Consultas=[]
Sugerencias=[]
Reclamos=[]

#Bienvenida al usuario
Name=input("Bienvenido Cual es tu nombre? ")
print(f"Bienvenido a Movistar ",Name)

#Menu de acceso
Boolean=True
while Boolean==True:
    print("===============================================")
    print("                    MENU                       ")
    print("===============================================")
    print(f"Como quieres ingresar ",Name)
    print("""
            1. Tecnico
            2. Cliente
            3. Salir del programa
            """)
    Opcion=input("Ingrese una opcion (1-3): ")

    #Menu que se le mostrara al tecnico
    if Opcion=="1":
        print("Bienvenido Tecnico ",Name)
        print("===========================================")
        print("              MENU DEL TECNICO             ")
        print("===========================================")
        print(""" 
              1. Revisar clientes
              2. Revisar Servicio del cliente
              3. Revisar Clientes Leales
              4. Revisar reportes
              5. Revisar el tiempo de cada usuario
              """)
        OpcionTecnico=input("Que desea hacer? (1-4)\n ")
        
        if OpcionTecnico=="1":
            print("Estos son los clientes que se encuentran con el servicio")
            print({'id'})

        if OpcionTecnico=="2":
            print("que deseas revisar? ")
            print("===========================================")
            print("""
                1. Sugerencias
                2. Consultas
                3. Reclamos
                """)
            print("===========================================")

    #Menu que se le mostrara al usuario
    if Opcion=="2":
        print("Bienvenido ", Name)
        print("============================================")
        print("              MENU DEL USUARIO              ")
        print("============================================")
        print("""
            1. Realizar una sugerencia
            2. Realizar un reclamo
            3. Realizar una consulta a algun tecnico disponible
            4. Salir del programa
            5. Comprar plan de Movistar
            """)
        OpcionCliente=input("Que deseas hacer? (1-3)")

        try: OpcionCliente

        except: OpcionCliente=="4"
        print("Hasta la proxima ",Name)
        Boolean=False

        if OpcionCliente=="1":
            input("Realizar tu sugerencia a un tecnico\n ") 
            input({'Sugerencias'})

        if OpcionCliente=="2":
            print("Realizar tu reclamo a un tecnico\n ")
            input({'Reclamos'})

        if OpcionCliente=="3":
            print("Realizar consulta a un tecnico\n ") 
            input({'consultas'})
        
        if OpcionCliente=="5":
            print("===================================================")
            print("               PLANES DE MOVISTAR                  ")
            print("===================================================")
            print("""
                  1. Internet de Fibra Optica
                  2. Planes Pospago
                  3. Planes Prepago
                """)
            Planes=input("que plan vas a comprar?(1-3)\n")
            
            if Planes==1:
                print("""
                =========================================
                    PLANES DE INTERNET DE FIBRA OPTICA
                =========================================
                    1. Planes Mensuales
                    2. Planes Anuales
                    3. Planes de Por vida
                    """)
                Planes2=input("Que plan quieres comprar? ")

                if Planes2=="1":
                    print("===================================================")
                    print("                  PLANES MENSUALES                 ")
                    print("===================================================")
                    print("""
                        # | DESCRICION   | Capacidad | Precio (COP)
                        1.  Plan de 25   |    GB     |   $  40.000
                        2.  Plan de 50   |    GB     |   $  80.000
                        3.  Plan de 100  |    GB     |   $ 160.000
                        4.  Plan de 150  |    GB     |   $ 240.000
                        5.  Plan de 200  |    GB     |   $ 300.000
                        6.  Plan de 300  |    GB     |   $ 400.000
                        7.  Plan de 400  |    GB     |   $ 500.000
                        8.  Plan de 500  |    GB     |   $ 600.000
                        9.  Plan de 1000 |    GB     |   $ 700.000
                    """)
                    TipoPlanMensual=input("Que plan prefieres? \n")
                    if TipoPlanMensual=="":
                        print("plan comprado exitosamente ")
                    
                if Planes2=="1":
                    print("===================================================")
                    print("                  PLANES ANUALES                   ")
                    print("===================================================")
                    print("""
                        # | DESCRICION   | Capacidad | Precio (COP)
                        1.  Plan de 25   |    GB     |   $  40.000
                        2.  Plan de 50   |    GB     |   $  80.000
                        3.  Plan de 100  |    GB     |   $ 160.000
                        4.  Plan de 150  |    GB     |   $ 240.000
                        5.  Plan de 200  |    GB     |   $ 300.000
                        6.  Plan de 300  |    GB     |   $ 400.000
                        7.  Plan de 400  |    GB     |   $ 500.000
                        8.  Plan de 500  |    GB     |   $ 600.000
                        9.  Plan de 1000 |    GB     |   $ 700.000
                    """)

    if Opcion=="3":
        print("Hasta la proxima, ", Name)
        print("Espero haber podido ayudarte :D ")
        Boolean=False

