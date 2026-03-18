from pydantic import BaseModel, ConfigDict


class PackageCreate(BaseModel):
    name: str
    description: str
    image_url: str


class PackageUpdate(BaseModel):
    name: str
    description: str
    image_url: str


class PackageResponse(BaseModel):
    id: int
    name: str
    description: str
    image_url: str

    model_config = ConfigDict(from_attributes=True)
