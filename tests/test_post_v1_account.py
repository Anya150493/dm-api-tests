from services.dm_api_account import Facade

import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_post_v1_account():
    api = Facade(host='http://localhost:5051')

    login = "login_42",
    email = "login_42@mail.ru",
    password = "login_42"

    response = api.account.register_new_user(
        login=login,
        email=email,
        password=password
    )

    # api.account.activate_registered_user()
    #
    # api.login.login_user(
    #     login=login,
    #     password=password
    # )
