# aluno = {
#     "nome": "Fulano",
#     "idade": 16,
#     "nota": 9.5
# }

# print(aluno["nome"])
# print(aluno["idade"])
# print(aluno["nota"])

# alunos = [
#     {"nome": "Ana", "notas": (10, 20, 30, 40)},
#     {"nome": "Jose", "notas": (10, 20, 30, 40)}
# ]

# for aluno in alunos:
#     media = (sum(aluno["notas"])/ len(aluno["notas"]))
#     print(aluno["nome"]) 

''''
Faça um dicionario que possui a seguinte estrutura:
nome
cpf
endereco (rua, numero, bairro, cidade, UF)

Adicione ao menos 3 linhas nesse dicionário, preechendo todos os dados.

Imprima os dados de cada pessoa, como:

Pessoa: {nome}
CPF: {cpf}
Endereço: {rua}, {numero}, {bairro}. {cidade} - {UF}.
'''

pessoas = [
    {
     "nome": "giseldo",
     "cpf": "1234567",
     "endereco": {"rua": "Rua A", "bairro": "Universitario", "cidade": "Maceio", "UF": "AL"}
    },

    {
     "nome": "Alex",
     "cpf": "1234",
     "endereco": {"rua": "Rua A", "bairro": "Universitario", "cidade": "Maceio", "UF": "AL"}
    },

    {
     "nome": "Jose",
     "cpf": "1234",
     "endereco": {"rua": "Rua A", "bairro": "Universitario", "cidade": "Maceio", "UF": "AL"}
    },

]

for pessoa in pessoas:
    print(f"""
          Nome: {pessoa["nome"]}, CPF: {pessoa["cpf"]}, 
          Endereço:
          Rua: {pessoa["endereco"]["rua"]}, Bairro: {pessoa["endereco"]["bairro"]}, Bairro: {pessoa["endereco"]["cidade"]}, Bairro: {pessoa["endereco"]["UF"]}
          """)