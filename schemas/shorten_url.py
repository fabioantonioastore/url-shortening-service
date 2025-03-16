from pydantic import BaseModel, field_validator
import validators
from fastapi import HTTPException, status


class ShortenURL(BaseModel):
    pass


class CreateShortenURL(ShortenURL):
    url: str
    short_code: str

    @field_validator("url")
    @classmethod
    def is_url(cls, url: str) -> str:
        if not (validators.url(url)):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid URL"
            )
        return url

    @field_validator("short_code")
    @classmethod
    def has_space(cls, value: str) -> str:
        if " " in value:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid short code"
            )
        return value


class UpdateShortenURL(CreateShortenURL):
    pass
