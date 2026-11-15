
## Imports 
import os 
import joblib
from dotenv import load_dotenv

## Find the main directory path 
BASE_PATH = os.path.dirname(os.path.dirname(__file__))

## Loading the env file variables 
load_dotenv(os.path.join(BASE_PATH, ".env"))

## Initiate the variables
APP_NAME = os.getenv("APP_NAME")
APP_VERSION = os.getenv("APP_VERSION")
SECRET_KEY = os.getenv("SECRET_KEY")

## Load models and processors 
processors = joblib.load(os.path.join(BASE_PATH, "..", "artifacts", "processors.pkl"))
forest_model = joblib.load(os.path.join(BASE_PATH, "..", "artifacts", "Random_forest_grid_model.pkl"))