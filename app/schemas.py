from pydantic import BaseModel
from typing import List


class Plane(BaseModel):
    flightid: int
    reg: str


class PlanesIn(BaseModel):
    planes: List[Plane]
