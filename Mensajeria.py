#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json
import io
import os

PATH = ''

if os.path.exists("cuentas.json"):
    with open("cuentas.json") as file:
        data = json.load(file)
else:
    with io.open(os.path.join(PATH, 'cuentas.json'), 'w') as db_file:
        db_file.write(json.dumps({"cuentas": []}))
#Verifica la exitencia del archivo JSON,
#si éste no existe, lo crea.


def menu_one():
    """
    Muesta al usuario las opciones al iniciarse el programa.

    """
    print("Bienvenido :) ")
    print("c - Crear cuenta")
    print("i - Ingresar a una cuenta")
    print("s - Salir")
    pass


def menu_two():
    """
    Muestra al usuario las opciones al ingresar a su cuenta.

    """
    print("A que opcion deseas acceder")
    print("p - Perfil")
    print("v - Ver mensajes")
    print("en - Enviar mensajes")
    print("el - Eliminar mensajes")
    print("s - Salir de la cuenta")
    pass


def menu_admin():
    print("Menu del administrador")
    print("perfil - Perfil del usuario")
    print("ver - Ver mensajes del usuario")
    print("salir - Salir de la cuenta del admin")
    pass


def crear_cuenta(usernam, nombr, apellid, clav, mensaj, cuentas_):
    """
    Crea las cuentas del usuario y las almacena en el archivo "cuentas.json".

    :param usernam: Nombre de usuario de la persona.
    :param nombr: Nombre de la persona.
    :param apellid: Apellido de la persona.
    :param clav: Clave de la cuenta del usuario.
    :param mensaj: Mensaje inicial de la cuenta.
    :param cuentas_: Diccionario que almance los datos del usario.

    """
    with open("cuentas.json") as file:
        data = json.load(file)
    cuentas_["Username"] = usernam
    cuentas_["Nombre"] = nombr.capitalize()
    cuentas_["Apellido"] = apellid.capitalize()
    cuentas_["Clave"] = clav
    cuentas_["Mensajes"] = mensaj
    data["cuentas"].append(cuentas_)
    with open("cuentas.json", "w") as file:
        json.dump(data, file, indent=4)
    pass


def enviar_mensaje(des, mensa, data, userx):
    """
    Permite enviar mensajes al usuario seleccionado y
    los almacena en el archivo "cuentas.json".

    :param des: Destinatario del mensaje que se enviará.
    :param mensa: Mensaje que se enviará.
    :param data: Variable que contiene los datos del archivo "cuentas.json".
    :param userx: Variable que almacena la posición del usario
     que recibe el mensaje.

    """
    for j in data["cuentas"]:
        if des == j["Username"]:
            userx = j
            break
    mens = (user["Username"] + ": " + mensa)
    userx["Mensajes"].append(mens)
    with open("cuentas.json", "w") as file:
        json.dump(data, file, indent=4)
    pass


def eliminar_mensaje(mensaje_a_eliminar, user, data):
    """
    Permite eliminar un mensaje elegido por el usario.

    :param mensaje_a_eliminar: Varible que almacena la posición del
     mensaje a eliminar.
    :param user: Varible que almacena la posición del usuario que
     envia el mensaje.
    :param data: Variable que contiene los datos del archivo "cuentas.json".

    """
    del user["Mensajes"][mensaje_a_eliminar]
    with open("cuentas.json", "w") as file:
        json.dump(data, file, indent=4)
    pass

userx = 0
cuentas_t = {}
mensaje = []
mens = 0
mensaje_a_eliminar = 0
men = 'Admin: Bienvenido a la plataforma'
mensaje.append(men)
boo = True
while boo:
    menu_one()
    x = input("Ingrese su opcion: ")
    if x == 'c':
        with open("cuentas.json") as file:
            data = json.load(file)
        print("Se procedera a pedir sus datos de usuario")
        nombre_usuario = input("Username: ")
        for elemento in data["cuentas"]:
            if nombre_usuario == elemento["Username"]:
                print("El nombre de usuario que ingreso ya existe")
                nombre_usuario = input("Username: ")
        # Valida si el usuario existe
        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        clave = input("Clave: ")
        crear_cuenta(nombre_usuario, nombre,
                     apellido, clave, mensaje,
                     cuentas_t)
        print("Creación de cuenta exitosa")
        print("")
    elif x == 'i':
        bu = True
        with open("cuentas.json") as file:
            data = json.load(file)
        t = input("Ingrese su nombre de usuario: ")
        c = input("Ingrese su contraseña: ")
        if t == "Admin" and c == "Admin":
            bi = True
            print("Sesión iniciada exitosamente")
            while bi:
                cuenta_ing = input(print("A que cuenta desea ingresar: "))
                for elemen in data["cuentas"]:
                    # Recorre las cuentas
                    if cuenta_ing == elemen["Username"]:
                        menu_admin()
                        opcion = input(print("Ingrese su opcion: "))
                        if opcion == "perfil":
                            print("Datos del perfil: ")
                            print("Username: " + elemen["Username"])
                            print("Nombre: " + elemen["Nombre"])
                            print("Apellido: " + elemen["Apellido"])
                            print("Clave: " + elemen["Clave"])
                            print("")
                        elif opcion == "ver":
                            print("Mensajes recibidos: ")
                            for i in elemen["Mensajes"]:
                                print(i)
                            # Imprime los mensajes del usuario
                            print("")
                        elif opcion == 's':
                            bi = False
        else:
            while bu:
                for i in data["cuentas"]:
                    # Recorre las cuentas
                    if t == i["Username"] and c == i["Clave"]:
                        print("Inicio de sesión exitoso")
                        user = i
                        menu_two()
                        resp = input("Ingrese la opcion deseada: ")
                        if resp == 'p':
                            print("Datos del perfil: ")
                            print("Username: " + user["Username"])
                            print("Nombre: " + user["Nombre"])
                            print("Apellido: " + user["Apellido"])
                            print("Clave: " + user["Clave"])
                            print("")
                            break
                        elif resp == 'v':
                            print("Mensajes recibidos: ")
                            for i in user["Mensajes"]:
                                print(i)
                            # Imprime los mensajes del usuario
                            print("")
                            break
                        elif resp == "en":
                            with open("cuentas.json") as file:
                                data = json.load(file)
                            for i in data["cuentas"]:
                                print(i["Username"])
                            # Imprime la lista de usuarios
                            dest = input("Ingrese nombre del destinatario: ")
                            mensa = input("Escriba su mensaje: ")
                            enviar_mensaje(dest, mensa, data, userx)
                            print("Mensaje enviado exitosamente")
                            print("")
                            break
                        elif resp == "el":
                            posiciones = len(user["Mensajes"])
                            print("que mensaje desea eliminar: ")
                            print(user["Mensajes"])
                            mensaje_a_eliminar = int(input(
                                "Ingrese la posicion(parte desde el 0) del"
                                " mensaje que desea eliminar: "))
                            while mensaje_a_eliminar < 0 or mensaje_a_eliminar > (posiciones-1):
                                print("posicion fuera de rango")
                                mensaje_a_eliminar = int(input(
                                    "Ingrese la posicion(parte desde el 0) del"
                                    " mensaje que desea eliminar: "))
                            eliminar_mensaje(mensaje_a_eliminar, user, data)
                            print("Mensaje elimiando exitosamente")
                            print("")
                            break
                        elif resp == 's':
                            bu = False
    elif x == 's':
        boo = False

