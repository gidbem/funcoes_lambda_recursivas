#Funcão para calcular o reajuste de um produto em 30%
def calcular_reajuste(valor):
    return valor * 1.3

print(f'Preço: {calcular_reajuste(1000)}') 

#Função lambda
reajuste = lambda x : x * 1.3

print(reajuste(1000))

produtos = [1000, 200, 350, 520, 110]
print(list(map(calcular_reajuste, produtos)))
print(list(map(lambda x : x * 1.3, produtos)))
print(list(map(reajuste, produtos)))

#Converte uma string em maiúscula
nome_lambda = lambda nome : nome.upper()
print(nome_lambda('gigi'))

lista = ['ana', 'maria', 'carlos', 'pedro']

print(list(map(lambda nome : nome.upper(), lista)))

#Retornar uma lista apenas com valores pares
numeros = [1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x : x % 2 == 0, numeros))) 
print(list(filter(lambda x : x % 2 == 0, numeros))) 



