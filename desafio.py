import random
import string

def gerar_senha_criptografada(tamanho, deslocamento):
    if tamanho == 0:
        return "", "" 
    else:
        caractere = random.choice(string.ascii_letters + string.digits)
        novo_caractere = chr((ord(caractere) + deslocamento - ord('A')) % 26 + ord('A'))
        original, criptografada = gerar_senha_criptografada(tamanho - 1, deslocamento)
        return caractere + original, novo_caractere + criptografada
    
tamanho_senha = 8
deslocamento = 3
original, criptografada = gerar_senha_criptografada(tamanho_senha, deslocamento)
print(f"Senha original: {original}\n \nSenha Criptografada: {criptografada}")