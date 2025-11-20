import socket
from ping3 import ping

############################################
#      Verifica se host esta online        #
############################################
def online(alvo):
    if(ping(alvo)):
        return True
    return False

#############################################
#          testa porta do host              #
#############################################
def scan_port(alvo, porta):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    try:
        resposta = sock.connect_ex((alvo, porta))
        sock.close()
        return resposta == 0
    except TimeoutError:
        return False
    except Exception as e:
        print(f"Erro: {e}")

# Lista de portas a verifica
portas = list({22, 23, 53, 80, 1315, 179})
portas.sort()

for octeto1 in range(3, 9, 1):
    for octeto2 in range(3, 9, 1):
        alvo = f"8.8.{octeto1}.{octeto2}"
        print(f"\033[34mProcurando em {alvo}\033[0m")
        if(online(alvo)):
            for porta in portas:
                print(f"\tconexão TCP posta {porta}\t", end='')
                if (scan_port(alvo, porta)):
                    print(f"\033[32m[ OPEN ]\033[0m")
                else:
                    print(f"\033[31m[CLOSED]\033[0m")
        else:
            print(f"\t\t\t\t\033[33m[OFFLIN]\033[0m")
