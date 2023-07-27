from services.dm_api_account import Facade

import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_get_v1_account():
    api = Facade(host='http://localhost:5051')
    token = api.login.get_auth_token(login='login_59', password='login_59')
    api.account.set_headers(headers=token)
    api.login.set_headers(headers=token)
    api.account.get_current_user_info()
    # api.login.logout_user()
    api.login.logout_user_from_all_devices()
