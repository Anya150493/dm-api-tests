from pydantic import BaseModel, StrictBool, StrictStr


class LoginCredentialsModel(BaseModel):
    login: StrictStr
    password: StrictStr
    remember_me: StrictBool
