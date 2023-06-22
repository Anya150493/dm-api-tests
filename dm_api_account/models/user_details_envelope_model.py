from enum import Enum
from typing import List, Optional
from datetime import datetime

from pydantic import BaseModel, StrictStr, Field, ConstrainedDate


class Roles(Enum):
    GUEST = 'Guest'
    PLAYER = 'Player'
    ADMINISTRATOR = 'Administrator'
    NANNY_MODERATOR = 'NannyModerator'
    REGULAR_MODERATOR = 'RegularModerator'
    SENIOR_MODERATOR = 'SeniorModerator'


class Rating(BaseModel):
    enabled: bool
    quality: int
    quantity: int


class ParseMode(Enum):
    COMMON = 'Common'
    INFO = 'Info'
    POST = 'Post'
    CHAT = 'Chat'


class InfoBbText(BaseModel):
    value: str
    parseMode: List[ParseMode]


class PagingSettings(BaseModel):
    posts_per_page: int
    comments_per_page: int
    topics_per_page: int
    messages_per_page: int
    entities_per_page: int


class ColorSchema(Enum):
    MODERN = 'Modern'
    PALE = 'Pale'
    CLASSIC = 'Classic'
    CLASSIC_PALE = 'ClassicPale'
    NIGHT = 'Night'


class Settings(BaseModel):
    color_schema: List[ColorSchema]
    nanny_greetings_message: Optional[StrictStr]
    paging: PagingSettings


class UserDetails(BaseModel):
    login: str
    roles: List[Roles]
    medium_picture_url: Optional[StrictStr] = Field(alias="mediumPictureUrl")
    small_picture_url: Optional[StrictStr] = Field(alias="smallPictureUrl")
    status: Optional[StrictStr]
    rating: Rating
    online: Optional[datetime]
    name: Optional[StrictStr]
    location: Optional[StrictStr]
    registration: Optional[datetime]
    icq: Optional[StrictStr]
    skype: Optional[StrictStr]
    originalPictureUrl: Optional[StrictStr]
    info: InfoBbText
    settings: Settings


class UserDetailsEnvelopeModel(BaseModel):
    resourse: UserDetails
    metodata: Optional[StrictStr]
