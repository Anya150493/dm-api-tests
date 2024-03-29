import structlog

from generic.helpers.dm_db import DmDatabase
from services.dm_api_account import Facade
from dm_api_account.models.user_envelope_model import UserRole
import json
from hamcrest import assert_that, has_properties

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_token():
    api = Facade(host='http://localhost:5051')

    login = "login_70"
    email = "login_70@mail.ru"
    password = "login_70"

    db = DmDatabase(user='postgres', password='admin', host='localhost', database='dm3.5')
    db.delete_user_by_login(login=login)
    dataset = db.get_user_by_login(login=login)
    assert len(dataset) == 0

    api.mailhog.delete_all_messages()

    response = api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    dataset = db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Login'] == login, f'User {login} not registered'
        assert row['Activated'] is False, f'User {login} was not activated'

    db.activate_user_by_db(login=login)
    dataset = db.get_user_by_login(login=login)
    for row in dataset:
        assert row['Activated'] is True, f'User {login} was activated'



