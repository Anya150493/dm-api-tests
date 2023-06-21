from pydantic import BaseModel, StrictBool, StrictStr


class LoginCredentialsModel(BaseModel):
    login: StrictStr
    password: StrictStr
    rememberMe: StrictBool
