from pydantic import BaseModel, UUID4, Field


class CountryBase(BaseModel):
    title: str = Field(..., max_length=255)
    attr: str = Field(None, max_length=255)

    class Config:
        orm_mode = True


class CountryCreate(CountryBase):
    pass
