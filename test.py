nome = "breno"
idade = 10


def teste(nome: str, idade: int):
    
    print(f"Nome: {nome}, Idade: {idade}")
    
teste(nome, idade)


def soma(a: int, b: int) -> int:
    return a + b

test = 4+3
valor = soma(20, 30)
print(f"Soma: {test}, Valor: {valor}")

def teste2(valor: int, valor2:int, valor3:int) -> int:
    return valor + valor2 + valor3 / valor2


soma = teste2(10, 20, 30)
print(f"Soma 2: {soma}")
    