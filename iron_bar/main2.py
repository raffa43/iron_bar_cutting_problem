import datetime
from bottom_up import corte_barra_bottom_up, MEMO_FILE
import json


PRICE_DATA = {  
                1: 1,
                2: 2,
                3: 8,
                4: 11,
                5: 14,
                6: 15,
                7: 16,
                8: 18,
                9: 19,
                10: 19,
                11: 20,
                12: 21,
            }

# Teste inicial
bar_size = int(input("Digite o tamanho da barra: ")) 
start_time = datetime.datetime.now()
resultado = corte_barra_bottom_up(bar_size, PRICE_DATA)
print("\nResultado:", resultado)
print("Duração:", datetime.datetime.now() - start_time)

## Teste secundario para comparação da velocidade
print("\n")
bar_size = int(input("Digite o tamanho da barra: ")) 
start_time = datetime.datetime.now()

resultado = corte_barra_bottom_up(bar_size, PRICE_DATA)
print("Resultado:", resultado)
print(json.load(open(MEMO_FILE, 'r')))

print("Duração:", datetime.datetime.now() - start_time)