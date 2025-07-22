import re 
import getpass

def verificar_forca(senha):
    pontos = 0
    if len(senha)>= 8:
        pontos += 1
    if re.search(r"[a-z]", senha) and re.search(r"[A-Z]", senha):
        pontos += 1
    if re.search(r"[!@#$%¨&*()-_=+´`~^/:;ç]", senha):
        pontos += 1
    if re.search(r"\d", senha):
        pontos += 1
    if re.search(r"(123456|abcdef|senha|password|qwerty)", senha.lower()):
        pontos -= 1

    if pontos <= 1:
        return "Fraca!"
    elif pontos <=3:
        return "Média!"
    else:
        return "Forte!"
        
    
senha = getpass.getpass("Digite a senha para ser verificada: ")
resultado = verificar_forca(senha)
print(f"A sua senha é: {resultado}")
