import structlog
from services.dm_api_account import DmApiAccount
from dm_api_account.models.user_envelope_model import UserRole
import json
from hamcrest import assert_that, has_properties

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_put_v1_account_token():
    api = DmApiAccount(host='http://localhost:5051')
    response = api.account.put_v1_account_token(token='64ab6f09-4f00-409a-8935-27d5c27fc114', status_code=200)
    assert_that(response.resource, has_properties(
        {
            "login": "login_36",
            "roles": [UserRole.guest, UserRole.player]
        }
    ))

    # expected_json = {'resourse': {
    #     "login": "login36",
    #     "rating": {
    #         "quantity": 0
    #     },
    #     "roles": [
    #         "Guest",
    #         "Player"
    #     ]
    # }}
    # actual_json = json.loads(response.json(by_alias=True, exclude_none=True))
    # assert actual_json==expected_json
    # print(response)
    # print(response.resource)
    # print(response.resource.login)
    # print(response.resource.roles)
