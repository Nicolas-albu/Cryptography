from math import tan, sin, cos, ceil
import base64

# criptografia: base64, MD5, SHA-1, ASCII, sistema hexadecimal, Rejindael, sistema octal, RSA. (metadata, camadas de rede)

"""
num = int(input("Numero: "))

octal = oct(num)
binario = bin(num)
hexadecimal = hex(num)
"""

msg = input("Msg: ")
num = int(input("Número primo: "))

def __base_codif__(): #base64 - criptografia

    a = msg.encode("utf-8")

    global base64_bytes
    global base85_bytes
    global base32_bytes
    global base16_bytes

    base64_bytes = base64.b64encode(a)
    base64_bytes_cont = base64_bytes.decode("utf-8")

    base32_bytes = base64.b32encode(base64_bytes)
    base32_bytes_cont = base32_bytes.decode("utf-8")

    base16_bytes = base64.b16encode(base32_bytes)
    base16_bytes_cont = base16_bytes.decode("utf-8")

    base85_bytes = (base64.b85encode(base16_bytes)).decode("utf-8")
    base85_bytes_cont = base85_bytes

    print("\nCriptografia em base -> 85: {}, 64: {}, 32: {}, 16: {}".format(base85_bytes_cont, base64_bytes_cont, base32_bytes_cont, base16_bytes_cont))

def __numeric_base_codif__():
    
    global oct_num
    global hex_num
    global bin_num

    oct_num = oct(num)
    #oct_num_complication = int(str(oct_num)[2:])
    oct_num_cont = str(oct_num)[2:]

    hex_num = hex(num)
    #hex_num_complication = int(str(hex_num[2:]))
    hex_num_cont = str(hex_num)[2:]

    bin_num = bin(num)
    bin_num_cont = str(bin_num)[2:]

    print("Criptografia com base númerica -> octal: {}, hexadecimal: {}, binário: {}".format(oct_num_cont, hex_num_cont, bin_num_cont))

def __trignometric_codif__():

    global tan_codif
    global sin_codif
    global cos_codif

    tan_codif = tan(num)
    tan_codif_cont = str(tan_codif)[3:]
    
    sin_codif = sin(tan_codif)
    sin_codif_cont = str(tan_codif)[3:]

    cos_codif = cos(sin_codif)
    cos_codif_cont = str(sin_codif)[3:]

    print("Criptografia com trigonometria -> tangente: {}, seno: {}, cosseno: {}\n".format(tan_codif_cont, sin_codif_cont, cos_codif_cont))

#------------------------------------------------------------ Decriptofia ----------------------------------------------------------

def __base_decodif__(): #base64 - decriptografia

    base64_bytes_decoded = base64.decodebytes(base64_bytes)
    base64_bytes_decoded_deco = base64_bytes_decoded.decode("utf-8")

    base32_bytes_decoded = base64.b32decode(base32_bytes)
    base32_bytes_decoded_cont = base64.decodebytes(base32_bytes_decoded)
    base32_bytes_decoded_deco = base32_bytes_decoded_cont.decode("utf-8")

    base16_bytes_decoded = base64.b16decode(base16_bytes)
    base16_bytes_decoded_cont = base64.b32decode(base16_bytes_decoded)
    base16_bytes_decoded_cript = base64.decodebytes(base16_bytes_decoded_cont)
    base16_bytes_decoded_deco = base16_bytes_decoded_cript.decode("utf-8")

    b85 = base85_bytes.encode("utf-8")
    base85_bytes_decoded = base64.b85decode(b85)
    base85_bytes_decoded = base64.b16decode(base85_bytes_decoded)
    base85_bytes_decoded_cont = base64.b32decode(base85_bytes_decoded)
    base85_bytes_decoded_cript = base64.decodebytes(base85_bytes_decoded_cont)
    base85_bytes_decoded_deco = base85_bytes_decoded_cript.decode("utf-8")

    print("Decriptografia em base -> 85: {}, 64: {}, 32: {}, 16: {}".format(base85_bytes_decoded_deco, base64_bytes_decoded_deco, base32_bytes_decoded_deco, base16_bytes_decoded_deco))

    #def __numeric_base_decodif__():
    """
    def __trignometric_decodif__():

        t
    """
#Executadores de funções criptograficas
#Executores criptograficos
__base_codif__()
__numeric_base_codif__()
__trignometric_codif__()

#Executores decriptograficos
__base_decodif__()
#__numeric_base_decodif__()