from pydantic import BaseModel


class RootResponse(BaseModel):
    name: str
    status: str
    environment: str


class HealthResponse(BaseModel):
    status: str

