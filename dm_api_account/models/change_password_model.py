from pydantic import BaseModel, StrictStr


class ChangePasswordModel(BaseModel):
    login: StrictStr
    token: StrictStr
    oldPassword: StrictStr
    newPassword: StrictStr

# change_password_model = {
#     "login": "password1",
#     "token": "84060d01-09e6-096e-2459-1409207d00c7",
#     "oldPassword": "password1",
#     "newPassword": "password2"
# }
