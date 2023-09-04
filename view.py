from controller import register, login
import os


def view():
    name, email, password = '', '', ''

    while True:
        print(f'{"=" * 5}MENU{"=" * 5}\n'
              f'1 - Cadastro\n'
              f'2 - Login\n'
              f'3 - Sair\n'
              f'{"="  * 14}')

        option = int(input('Insira a opção: '))

        os.system('clear')

        if option == 1:
            while True:
                print(f'{"=" * 5}CADASTRAR{"=" * 5}')

                name = input('Nome: ') if name == '' else name
                email = input('E-mail: ') if email == '' else email
                password = input('Senha: ') if password == '' else password

                new_register, name, email, password = register(name, email, password)

                if new_register:
                    os.system('clear')

                    break

        if option == 2:
            while True:
                email = input('E-mail: ')
                password = input('Senha: ')

                login_ = login(email, password)

                if login_:
                    input('Pressione enter para deslogar!')

                    break

        if option == 3:
            break

        else:
            print('Opção Inválida!')


if __name__ == '__main__':
    os.environ['TERM'] = 'xterm'
    view()
