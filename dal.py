from model import connsession, User

session = connsession()


def save_user(name, email, password):
    user = User(name=name, email=email, password=password)

    session.add(user)
    session.commit()
    session.rollback()

    return 'Usúario salvo com sucesso!'


def list_users():
    users = session.query(User)

    return users
