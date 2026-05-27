tentativa_login = 0

usuarios = []

while True:

    print('\n-------- MENU --------')
    print('1 - Cadastrar')
    print('2 - Login')
    print('3 - Listar usuários')
    print('4 - Sair')

    try:
        opcao = int(input('Escolha uma opção: '))

    except ValueError:
        print('Digite apenas números!')
        continue

    # ---------------- CADASTRO ----------------

    if opcao == 1:

        print('\n--- Cadastro ---')

        email = input('Email: ')
        senha = input('Senha: ')

        email_existe = False

        # verifica se já existe usuário com esse email
        for usuario in usuarios:

            if usuario["email"] == email:
                email_existe = True
                break

        if email_existe:

            print('Esse email já está cadastrado!')

        else:

            novo_usuario = {
                "email": email,
                "senha": senha
            }

            usuarios.append(novo_usuario)

            print('Cadastro realizado com sucesso!')

    # ---------------- LOGIN ----------------

    elif opcao == 2:

        print('\n--- Login ---')

        email = input('Email: ')
        senha = input('Senha: ')

        login_realizado = False

        for usuario in usuarios:

            if usuario["email"] == email and usuario["senha"] == senha:

                login_realizado = True
                break

        if login_realizado:

            print('Login realizado com sucesso!')

            # reseta tentativas após login correto
            tentativa_login = 0

        else:

            tentativa_login += 1

            print('Email ou senha incorretos.')

            print(f'Tentativas restantes: {3 - tentativa_login}')

            if tentativa_login >= 3:

                print('Número máximo de tentativas atingido.')
                print('Sistema encerrado.')

                break

    # ---------------- LISTAR USUÁRIOS ----------------

    elif opcao == 3:

        print('\n--- Usuários cadastrados ---')

        if len(usuarios) == 0:

            print('Nenhum usuário cadastrado.')

        else:

            for usuario in usuarios:

                print(usuario["email"])

    # ---------------- SAIR ----------------

    elif opcao == 4:

        print('Saindo do sistema...')
        break

    # ---------------- OPÇÃO INVÁLIDA ----------------

    else:

        print('Opção inválida. Tente novamente.')