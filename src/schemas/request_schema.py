
## imports
from pydantic import BaseModel, Field
from ..utils.enum_classes import CityEnum, StateZipEnum, WaterFront, ViewRate, ConditionRate

## Build the request schema for the data that will be 
# Entered to the model 

## Build the pydantic model for the entered data 
class ModelData(BaseModel): 
    bedrooms: int = Field(ge=0, le=8)
    bathrooms: float = Field(ge=0.0, le=8.0)
    sqft_living: int = Field(ge=380, le=13540)
    sqft_lot: int = Field(ge=638, le=1074218)
    floors: int = Field(ge=1, le=3)
    waterfront: WaterFront
    view: ViewRate
    condition: ConditionRate
    sqft_above: int = Field(ge=380, le=9410)
    sqft_basement: int = Field(ge=0, le=4820)
    yr_built: int = Field(ge=1900, le=2014)
    yr_renovated: int = Field(ge=0, le=2014)
    city: CityEnum
    statezip: StateZipEnum
    
    class Config:
        use_enum_values = True
    