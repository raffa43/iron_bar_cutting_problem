import json
import os

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

MEMO_FILE = "iron_bar/memo_bottom_up.json"

# Verifica se o arquivo de memo existe e carrega os dados
if os.path.exists(MEMO_FILE):
    try:
        with open(MEMO_FILE, 'r') as f:
            memo = json.load(f)
    except json.JSONDecodeError:
        memo = {}
else:
    memo = {}

def corte_barra_bottom_up(bar_size: int, prices: dict[int, int]):
    bar_size_str = str(bar_size)

    # Verifica se já existe no memo
    if bar_size_str in memo:
        print("\n🔁 Resultado recuperado do memo!\n")
        resultado = memo[bar_size_str]
        return resultado["lucro"], resultado["cortes"], resultado["iteracoes"]

    dp = [0] * (bar_size + 1)
    solution = [[] for _ in range(bar_size + 1)]
    iterations = 0

    for j in range(1, bar_size + 1):
        max_val = float('-inf')
        for i in range(1, j + 1):
            iterations += 1
            if i in prices and dp[j - i] + prices[i] > max_val:
                max_val = dp[j - i] + prices[i]
                solution[j] = solution[j - i] + [i]
                
        dp[j] = max_val
        print(solution)
        

    # Resultado a ser armazenado
    resultado = {
        "lucro": dp[bar_size],
        "cortes": solution[bar_size],
        "iteracoes": iterations
    }

    # Salva no memo
    memo[bar_size_str] = resultado
    with open(MEMO_FILE, 'w') as f:
        json.dump(memo, f, indent=2)

    return dp[bar_size], solution[bar_size], iterations
