contatos = {}

nome = input('Insira o nome do contato: ')
contatos['nome'] = nome
telefone = input('Insira o telefone do contato: ')
contatos['telefone'] = telefone
email = input('Insira o email do contato: ')
contatos['email'] = email

for chave, valor in contatos.items():
    print(f"{chave.capitalize()}: {valor}")
