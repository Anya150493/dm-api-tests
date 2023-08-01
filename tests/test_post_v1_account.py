import time
from generic.helpers.dm_db import DmDatabase
from services.dm_api_account import Facade
from generic.helpers.orm_db import OrmDatabase
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    api = Facade(host='http://localhost:5051')

    login = "login_69"
    email = "login_69@mail.ru"
    password_user = "login_69"

    user = 'postgres'
    password = 'admin'
    host = 'localhost'
    database = 'dm3.5'

    orm = OrmDatabase(user=user, password=password, host=host, database=database)
    orm.delete_user_by_login(login="login_69")

    # db = DmDatabase(user='postgres', password='admin', host='localhost', database='dm3.5')
    # db.delete_user_by_login(login=login)
    dataset = orm.get_user_by_login(login="login_69")
    assert len(dataset) == 0

    api.mailhog.delete_all_messages()

    response = api.account.register_new_user(
        login=login,
        email=email,
        password=password_user
    )

    dataset = orm.get_user_by_login(login="login_69")
    for row in dataset:
        assert row.Login == login, f'User {login} not registered'
        assert row.Activated is False, f'User {login} was activated'

    api.account.activate_registered_user(login=login)

    time.sleep(2)
    dataset = orm.get_user_by_login(login="login_69")
    for row in dataset:
        assert row.Activated is True, f'User {login} not activated'
    api.login.login_user(
        login=login,
        password=password_user
    )

    orm.db.close_connection()
