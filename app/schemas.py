

# class New_Plane(BaseModel):
#     username: str
#     name: str
#     age: int | None
#     country_id: int | None
#
#
# class New_Plane_ID(New_Plane):
#     id: int

from pydantic import BaseModel


class New_Plane(BaseModel):
    fr24_id: str
    flight: str
    callsign: str
    lat: float
    lon: float
    track: int
    alt: int
    gspeed: int
    vspeed: int
    squawk: str
    timestamp: str
    source: str
    hex: str
    type: str
    reg: str


class New_Plane_ID(New_Plane):
    id: int  # ID записи в базе данных