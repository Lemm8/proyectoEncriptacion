import base64
import encriptacionProyecto

def Send():
    print("Ingresa mensaje")
    MessageClient1 = input()
    return MessageClient1


def KeyClient():
    print("Inicializa llave")
    keyClient = input()
    return keyClient

def crip264(Criptomensaje):
   Message2byte = Criptomensaje
   Mbyte = Message2byte.encode("ascii")
   Message2B64 = base64.b64encode(Mbyte)
   #print("base 64")
   #print(Message2B64)
   return Message2B64


digramas = encriptacionProyecto.convertPlainTextToDiagraphs(Send())
#print(digramas + '  digrama')
cipherText = "".join(encriptacionProyecto.encrypt(digramas, KeyClient()))
#print(cipherText + '  Cipher txt')
MessageSend= crip264(cipherText)