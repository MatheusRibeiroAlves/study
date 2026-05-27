



tentativa_login = 0


while True:

    print('--------menu--------')

    print('1 - Cadastrar')
    print('2 - Login')
    print('3 - Sair') 
    

    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        print('Digite seu email e senha para cadastrar.')
        email_cadastro = input('Email: ')
        senha_cadastro = input('Senha: ')
        print('Cadastro realizado com sucesso!')
        
    elif opcao == 2:
        print('Digite seu email e senha para login.')
        email = input('Email: ')
        senha = input('Senha: ')
        if email == email_cadastro and senha == senha_cadastro:
            print('Login realizado com sucesso!')
        else:
            print('Email ou senha incorretos.')
            tentativa_login += 1
            if tentativa_login == 3:
                print('Número de tentativas excedido. Saindo do sistema...')
                break
        
    elif opcao == 3:
        print('Saindo do sistema...')
        break
    else:
        print('Opção inválida. Tente novamente.')

