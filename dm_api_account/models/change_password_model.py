from __future__ import annotations
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, StrictStr, Extra, Field


class ChangePassword(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr] = Field(None, description='User login')
    token: Optional[UUID] = Field(None, description='Password reset token')
    old_password: Optional[StrictStr] = Field(
        None, alias='oldPassword', description='Old password'
    )
    new_password: Optional[StrictStr] = Field(
        None, alias='newPassword', description='New password'
    )

# change_password_model = {
#     "Login": "password1",
#     "token": "84060d01-09e6-096e-2459-1409207d00c7",
#     "old_password": "password1",
#     "new_password": "password2"
# }
# print(ChangePasswordModel(**change_password_model).json())
