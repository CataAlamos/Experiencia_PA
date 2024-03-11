import random
import time
import os 
import platform

def cachipun():
    """
    Esta función representa el juego de cachipun.
    Debes pedir al usuario que elija piedra, papel o tijera, y luego comparar su elección con la de la computadora.
    La computadora debe elegir una opción al azar.
    """

    outcomes = {
        "piedra": {"tijera": "Ganaste!", "papel": "Perdiste.", "piedra": "¡Es un empate!"},
        "papel": {"piedra": "Ganaste!", "tijera": "Perdiste.", "papel": "¡Es un empate!"},
        "tijera": {"papel": "Ganaste!", "piedra": "Perdiste.", "tijera": "¡Es un empate!"}
    }

    valid_options = ["piedra", "papel", "tijera"]

    user_choice = input("Selecciona: piedra, papel o tijera \n").lower()

    if user_choice not in valid_options:
        print(f"Opción invalida: %s" % user_choice)
        cachipun()

    computer_choice = random.choice(valid_options)

    print(f"Tú elegiste: {user_choice}")
    print(f"La computadora eligió: {computer_choice}")

    print(outcomes[user_choice][computer_choice])


def adivinar_numero():
    """
    Esta función representa el juego de adivinar un número.
    Debes generar un número al azar entre 1 y 10, y luego pedir al usuario que adivine el número.
    Se debe mostrar un mensaje si el usuario adivina correctamente o no.
    """
    random_number = random.randint(1, 10)
    user_choice = int(input("Selecciona un numero entre 1 y 10\n"))

    if user_choice < 1 and user_choice > 10:
        adivinar_numero()

    if user_choice == random_number:
        print(f"Felicidades elegiste correctamente")
    else:
        print(f"Intenta nuevamente")
 

def reaccion_rapida():
    """
    Esta función representa el juego de reacción rápida.
    Debes pedir al usuario que presione Enter lo más rápido posible después de que vea "GO!".
    Debes medir el tiempo que tarda el usuario en reaccionar y mostrarlo al final del juego.
    """

    input("Presiona Enter para comenzar...")
    start_time = time.time()
    input("GO!")
    end_time = time.time()

    reaction_time = end_time - start_time
    print(f"Tardaste {reaction_time:.2f} segundos en reaccionar.")



def suma_rapida():
    """
    Esta función representa el juego de suma rápida.
    Debes generar dos números al azar y pedir al usuario que los sume lo más rápido posible.
    Debes medir el tiempo que tarda el usuario en responder y mostrarlo al final del juego.
    """
    random_number_1 = random.randint(1, 100)
    random_number_2 = random.randint(1, 100)

    print(f"Suma los siguientes números lo más rápido posible: {random_number_1} + {random_number_2}")

    start_time = time.time()
    user_answer = int(input("Ingrese la suma: "))
    end_time = time.time()

    if user_answer == random_number_1 + random_number_2:
        print("Respuesta correcta.")
    else:
        print("Respuesta incorrecta.")

    response_time = end_time - start_time
    print(f"Tardaste {response_time:.2f} segundos en responder.")



def clear_terminal():
    """
    Clear the terminal screen based on the platform.
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def memoria():
    """
    Esta función representa el juego de memoria.
    Debes generar una secuencia de números al azar y mostrarla al usuario.
    Luego, debes pedir al usuario que repita la secuencia.
    Se debe mostrar un mensaje si el usuario acierta o no.
    """
    longitude_sequence = random.randint(3, 10)
    random_sequence = [random.randint(0, 9) for _ in range(longitude_sequence)]

    print("Memoriza la siguiente secuencia:")
    print(" ".join(map(str, random_sequence)))
    print("Tienes 5 segundos")

    time.sleep(5)

    clear_terminal()

    user_input = input("Repite la secuencia (separando los números por espacios): ")
    user_sequence = list(map(int, user_input.split())) 

    if user_sequence == random_sequence:
        print("Respuesta correcta.")
    else:
        print("Respuesta incorrecta.")
