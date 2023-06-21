from pydantic import BaseModel, StrictStr


class GeneralErrorModel(BaseModel):
    message: StrictStr
