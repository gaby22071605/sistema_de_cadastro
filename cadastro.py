
def cadastro_cliente(banco_dados):
    #strip() remove espaços do fim e inicio da string
    nome = input('Nome: ').strip()
    idade = input('Idade: ').strip()
    telefone = input('Telefone: ').strip()
    email = input('Email: ').strip()

    if nome == '' or idade == '' or telefone == '' or email == '':
        print ('ERRO: Todos os campos são obrigatorios.')
        return None
    cliente = {
        'nome': nome,
        'idade': idade,
        'telefone': telefone,
        'email': email
    }
    banco_dados.append(cliente)

