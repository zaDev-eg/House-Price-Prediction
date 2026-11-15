
## Imports 
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from typing import Annotated
from ..schemas.request_schema import ModelData
from ..utils.inference import final_prediction
from ..utils.config import processors, forest_model, SECRET_KEY


## initialize the app 
random_forest_router = APIRouter()

## build the apikey_header
api_key_header = APIKeyHeader(name="X_API_Key")

## check if the Secret key is correct
async def varify_api_key(api_key: str=Depends(api_key_header)):
    if api_key != SECRET_KEY:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Wrong Secret Key ❌")
         

## EndPoints 
@random_forest_router.post("/forest_prediction")
async def forest_prediction(data: Annotated[ModelData, Depends()],
                            _: Annotated[str, Depends(varify_api_key)]): 
    ## pass the data to the inference method 
    result = final_prediction(data, processors, forest_model)
    
    ## display the final result 
    return {
        "prediction_state": "model prediction is ended successfully ✅",
        "final_prediction": float(result),
    } 