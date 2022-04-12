import Persona1
import base64
import desencriptacionProyecto

Message64 = Persona1.MessageSend
Message2byte = Message64.decode("ascii")
MessagByte = base64.b64decode(Message2byte)
String = MessagByte.decode("ascii")

def persona2():
    print(f"Mensaje recibido   :   {Message64}")
    print("Ingresa si para descomprimir mensaje")
    x = input()
    if x == "si" :
        print(f"Mensaje recibido descomprimido :  {String}")
        decrip(String)
    else:
        print("Adiós")

def decrip(String):
    print("Ingresa llave")
    key = input()
    cipherText = "".join(desencriptacionProyecto.decipher(String, key))
    print(cipherText)
