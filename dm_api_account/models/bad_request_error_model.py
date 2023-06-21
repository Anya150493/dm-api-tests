from pydantic import BaseModel, StrictStr


class BadRequestErrorModel(BaseModel):
    message: StrictStr
    invalid_properties: StrictStr
