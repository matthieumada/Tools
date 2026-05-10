import serial
import time

# Remplacez 'COM4' par le port de votre ESP32
# La vitesse (baudrate) doit être identique au code C++
port = "COM4" 
baudrate = 115200

try:
    ser = serial.Serial(port, baudrate, timeout=1)
    time.sleep(2) # Pause pour laisser l'ESP32 redémarrer après la connexion

    while True:
        commande = input("Entrez une commande (ON/OFF/EXIT) : ")
        
        if commande == "EXIT":
            break
            
        # Envoi du message avec un caractère de fin de ligne '\n'
        # .encode() transforme la chaîne en octets (bytes)
        ser.write((commande + '\n').encode())
        
        # Lecture de la réponse de l'ESP32
        reponse = ser.readline().decode().strip()
        if reponse:
            print(f"Réponse : {reponse}")

    ser.close()
except Exception as e:
    print(f"Erreur : {e}")