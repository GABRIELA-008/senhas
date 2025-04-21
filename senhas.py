import random
import string

def gerar_senha(tamanho=8):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        return senha

senha_gerada = gerar_senha(8)
print(f"sua senha é {senha_gerada}")
