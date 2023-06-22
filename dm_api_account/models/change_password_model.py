from pydantic import BaseModel, StrictStr, Field


class ChangePasswordModel(BaseModel):
    login: StrictStr = Field(alias='Login', title='login')
    token: StrictStr = Field(alias='token')
    old_password: StrictStr = Field(alias='old_password')
    new_password: StrictStr = Field(alias='new_password')


# change_password_model = {
#     "Login": "password1",
#     "token": "84060d01-09e6-096e-2459-1409207d00c7",
#     "old_password": "password1",
#     "new_password": "password2"
# }
# print(ChangePasswordModel(**change_password_model).json())
