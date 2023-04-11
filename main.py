ano_atual = int(input("Digite o ano atual: "))
idade = int(input("Digite sua idade atual: "))
novo_ano = int(input("Digite outro ano: "))
nome = str(input("Digite seu nome: "))
ano_nascimento = ano_atual - idade
nova_idade = novo_ano - ano_nascimento
print(nome,"no ano de", novo_ano, "você terá", nova_idade, "anos")