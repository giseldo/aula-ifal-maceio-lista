# Tarefa 1  crie uma lista parcial (recurso slice) com somente 3 meses, a partir do mes de agosto, 
# ou seja agosto, setembro e outubro
# imprima o valor na saída principal 

# meses_ano = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", 
#              "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

# for mes in meses_ano[7:10]:
#      print(mes)

# Tarefa 2
# Leia 4 notas e salve em uma lista (dica: list [] input)
# Verifique se ele quer alterar (print while input)
# Depois salve em uma tupla ( tuple () )
# Calcule a média da tupla e imprima na saída padrão (operações básicas + / 4)
# Tente alterar um valor da tupla e capture a exeção com uma mensagem padrão (try except ValueError)

notas = []
for i in range(4):
    notas.append(int(input("Digite a nota: ")))
    
deseja_alterar = 1
while (deseja_alterar == 1):
    deseja_alterar = int(input("Vc desejar alterar alguma nota? (0 - Nao ; 1 - Sim): "))
    if (deseja_alterar == 1):
        indice_nota = input("Digite o bimestre (1, 2, 3 ou 4): ")
        valor_alterado_nota = input("Informe a nova nota: ")
        notas[int(indice_nota) - 1] = valor_alterado_nota
tupla_notas = tuple(notas) # converte lista em tuplas
print("Média: ", (tupla_notas[0] + tupla_notas[1] + tupla_notas[2] + tupla_notas[3])/4) # imprime a média

try:
    tupla_notas[0] = 10
except TypeError as e:
    print("não é possivel alterar a  nota depois do fim do bimestre")

    








