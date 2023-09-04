from dal import list_users, save_user
from cryptography.hazmat.primitives import hashes
from sqlalchemy.exc import NoResultFound


def register(name, email, password):
    users = list_users()

    if name.strip():
        if not any(any(chr(x) in name for x in range(i, j)) for i, j in zip([33, 91, 123], [65, 97, 127])):
            if email.strip():
                if all(x != '' for x in email.split('@')) and '@' in email:
                    if not list(users.filter_by(email=email)):
                        if password.strip():
                            password_check = True
                            if not list(filter(lambda x: chr(x) in password, range(65, 91))):
                                print('A senha tem de ter uma letra maiúscula!')
                                password_check = False

                            if not list(filter(lambda x: chr(x) in password, range(97, 123))):
                                print('A senha tem de ter uma letra minúscula!')
                                password_check = False

                            if not list(filter(lambda x: str(x) in password, range(0, 10))):
                                print('A senha tem de ter um número!')
                                password_check = False

                            if not any(any(chr(x) in password for x in range(i, j)) for i, j in
                                       zip([33, 58, 91, 123], [48, 65, 97, 127])):
                                print('A senha tem de ter um caractere especial!')
                                password_check = False

                            if len(password) < 6:
                                print('A senha tem de ter no mínimo 6 caracteres!')
                                password_check = False

                            if password_check:
                                password_ = password[::-1].encode('utf-8')
                                password = password.encode('utf-8')
                                digest = hashes.Hash(hashes.SHA256())
                                digest.update(password)
                                digest.update(password_)
                                password_value = digest.finalize()

                                print(save_user(name, email, password_value))

                                return True

                            else:
                                return False, name, email, ''

                        else:
                            print('O campo senha não pode estar vazio!')

                            return False, name, email, ''

                    else:
                        print('Já existe uma conta com este e-mail!')

                        return False, name, '', ''

                else:
                    print('Insira o e-mail completo!')

                    return False, name, '', ''

            else:
                print('O campo e-mail não pode estar vazio!')

                return False, name, '', ''

        else:
            print('O campo nome não pode conter números ou caracteres especiais!')

            return False, '', email, ''

    else:
        print('O campo nome não pode estar vazio!')

        return False, '', email, ''


def login(email, password):
    try:
        users = list_users()

        user = users.filter_by(email=email).one()

        if user:
            password_ = password[::-1].encode('utf-8')
            password = password.encode('utf-8')
            digest = hashes.Hash(hashes.SHA256())
            digest.update(password)
            digest.update(password_)
            password_value = digest.finalize()

            if user.password == password_value:
                print(f'{user.name} está logado!')

            else:
                print('Senha incorreta!')

    except NoResultFound:
        print('Este usuario não existe!')
