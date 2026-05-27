while True:

    print('--------menu--------')

    print('1 - Login')
    print('2 - Cadastrar')
    print('3 - Sair') 

    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        print('Digite seu email e senha.')
        email = input('Email: ')
        senha = input('Senha: ')
        print('Login realizado com sucesso!')
    elif opcao == 2:
        print('Digite seu email e senha para cadastrar.')
        email = input('Email: ')
        senha = input('Senha: ')
        print('Cadastro realizado com sucesso!')
        
    elif opcao == 3:
        print('Saindo do sistema...')
        break
    else:
        print('Opção inválida. Tente novamente.')

