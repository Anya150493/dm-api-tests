from services.dm_api_account import Facade


def test_post_v1_account_login():
    api = Facade(host='http://localhost:5051')
    api.login.login_user(login="login_46", password="login_46", remember_me=True)
