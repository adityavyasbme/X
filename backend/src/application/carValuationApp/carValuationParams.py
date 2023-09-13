from pydantic import (BaseModel, ValidationError,
                      field_validator, model_validator)
from enum import Enum, IntEnum


class SellerType(IntEnum):
    Individual = 1
    Dealer = 0
    Other = -1


class TransmisionType(IntEnum):
    Manual = 1
    Automatic = 0


class FuelType(IntEnum):
    Diesel = 0
    Petrol = 1
    Other = -1


class OwnerType(IntEnum):
    First = 0
    Second = 1
    Third = 2
    FourthAndAbove = 3


class carValuationParams(BaseModel):
    Year: int
    Driven: float
    Fuel: FuelType
    SellerType: SellerType
    Transmission: TransmisionType
    Seats: int
    Torque_RPM: int
    Mileage_KMPL: float
    Engine_CC: float
    Power: float
    Owner: OwnerType

    @field_validator('Year')
    @classmethod
    def properYear(cls, v: int) -> int:
        assert v > 1950, "Considering cars manufactured after 1950"
        return v

    @field_validator('Seats')
    @classmethod
    def properSeats(cls, v: int) -> int:
        assert 9 > v > 1, "Seats Range 2-8"
        return v

    @model_validator(mode='after')
    def UpdateWhole(cls, values):
        values.Driven = round(values.Driven, 2)
        values.Mileage_KMPL = round(values.Mileage_KMPL, 2)
        values.Engine_CC = round(values.Engine_CC, 2)
        values.Power = round(values.Power, 2)
        return values


def decodeJson(object: carValuationParams) -> dict:
    """Ideally, I can modify pydantic model json to get the output I needed.
    To make it easier for me, I'll use this function for conversion
    """
    return {'year': int(object.Year),
            'km_driven': float(object.Driven),
            'fuel': int(object.Fuel),
            'seller_type': int(object.SellerType),
            'transmission': int(object.Transmission),
            'seats': int(object.Seats),
            'torque_rpm': int(object.Torque_RPM),
            'mil_kmpl': float(object.Mileage_KMPL),
            'engine_cc': float(object.Engine_CC),
            'max_power_new': float(object.Power),
            'First Owner': True if int(object.Owner) == 0 else False,
            'Fourth & Above Owner': True if int(object.Owner) == 3 else False,
            'Second Owner': True if int(object.Owner) == 1 else False,
            'Test Drive Car': False,
            'Third Owner': True if int(object.Owner) == 2 else False
            }
