
## Imports 
import pandas as pd 
import numpy as np
from ..schemas.request_schema import ModelData


## Mapping Functions 
def map_water_front(value: str): 
    ## Healthy Check
    value = str(value).strip().title()
    
    if value == "Yes": 
        return 1
    elif value == "No": 
        return 0
    else: 
        raise ValueError("Invalid value for water_front feature")
    
def map_view_rate(value: str): 
    ## Healthy Check
    value = str(value).strip().title()
    
    if value == "None": 
        return 0
    elif value == "Fair": 
        return 1
    elif value == "Good": 
        return 2
    elif value == "Very Good": 
        return 3    
    elif value == "Excellent": 
        return 4
    else: 
        raise ValueError("Invalid value for view feature")
    
def map_condition_rate(value: str): 
    ## Healthy Check
    value = str(value).strip().title()
    
    if value == "Poor": 
        return 1
    elif value == "Fair": 
        return 2
    elif value == "Average": 
        return 3
    elif value == "Good": 
        return 4
    elif value == "Very Good": 
        return 5
    else: 
        raise ValueError("Invalid value for condition rate feature")
    
    

## build the inference function 
def final_prediction(data: ModelData, 
                     processor, 
                     model): 
    
    ## Dump the data 
    data_dict = data.model_dump()
    
    ## mapping values 
    data_dict["waterfront"] = map_water_front(data_dict["waterfront"])
    data_dict["view"] = map_view_rate(data_dict["view"])
    data_dict["condition"] = map_condition_rate(data_dict["condition"])
    
    ## Convert the dictionary of data into dataframe
    df = pd.DataFrame([data_dict]) ## -> Convert the diction into a dataframe
    
    df["waterfront"] = df["waterfront"].astype(int)
    df["view"] = df["view"].astype(int)
    df["condition"] = df["condition"].astype(int)
    
    ## Preprocessing process 
    processed_df = processor.transform(df)
    
    ## Gain the Final Prediction
    final_prediction = model.predict(processed_df)
    
    ## return the final value 
    result = float(np.expm1(final_prediction)[0]) ## -> Convert the final price back to the real value
    
    return round(result, 2)
