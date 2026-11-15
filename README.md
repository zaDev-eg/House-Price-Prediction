# 🏠 House Price Prediction

A Machine Learning project that predicts house prices based on different property features using a trained **Random Forest Regressor** model. The project also provides a RESTful API built with **FastAPI**, allowing users to submit property information and receive price predictions.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Project Objectives](#-project-objectives)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Machine Learning Workflow](#-machine-learning-workflow)
- [Backend Architecture](#-backend-architecture)
- [Getting Started](#-getting-started)
- [Installation and Setup](#-installation-and-setup)
- [Environment Configuration](#-environment-configuration)
- [Running the Server](#-running-the-server)
- [API Documentation](#-api-documentation)
- [Troubleshooting](#-troubleshooting)

---

## 📖 Project Overview

House Price Prediction is an end-to-end Machine Learning project designed to estimate residential property prices based on several housing characteristics.

The project uses a **Random Forest Regression model** trained on housing data. It includes a complete prediction pipeline that handles incoming data, applies the required preprocessing transformations, and generates the final predicted house price.

To make the trained model accessible, a FastAPI backend was developed to expose the prediction functionality through REST API endpoints.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Explore and analyze housing datasets.
- Perform data preprocessing and feature preparation.
- Train and optimize a Random Forest Regression model.
- Save the trained model and preprocessing components for future use.
- Build a REST API using FastAPI.
- Validate incoming prediction data using Pydantic.
- Secure the prediction endpoint using API Key authentication.
- Provide a simple and reusable prediction service.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data manipulation and analysis |
| NumPy | Numerical computations |
| Scikit-learn | Machine Learning and preprocessing |
| XGBoost | Machine Learning library |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| FastAPI | Backend API development |
| Pydantic | Input validation |
| Joblib | Saving and loading trained models |
| Python-dotenv | Environment variable management |

---

## 📁 Project Structure

```text
House-Price-Prediction/
│
├── artifacts/
│   ├── Random_forest_grid_model.pkl
│   ├── processors.pkl
│   └── __init__.py
│
├── data/
│   └── data.csv
│
├── notebooks/
│   └── notebook.ipynb
│
├── src/
│   ├── routers/
│   │   ├── __init__.py
│   │   └── random_forest_router.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── request_schema.py
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── enum_classes.py
│   │   └── inference.py
│   │
│   ├── main.py
│   └── .env.example
│
├── requirements.txt
└── README.md
```

### Directory Description

**1. artifacts/**

Contains the previously trained Machine Learning components:

- `Random_forest_grid_model.pkl`: The trained Random Forest model.
- `processors.pkl`: The preprocessing components required to transform incoming data before prediction.

**2. data/**

Contains the original housing dataset used during the Machine Learning development process.

**3. notebooks/**

Contains the Jupyter Notebook used for data exploration, analysis, experimentation, and model development.

**4. src/routers/**

Contains the API routes and prediction endpoint implementation.

**5. src/schemas/**

Contains the Pydantic data schema used to validate incoming property information.

**6. src/utils/**

Contains utility modules responsible for:

- Loading environment variables and model artifacts.
- Defining categorical feature values using Python Enums.
- Preprocessing incoming data.
- Generating the final house price prediction.

**7. src/main.py**

The main entry point of the FastAPI application. It initializes the application, registers API routers, and configures CORS middleware.

---

## 🔬 Machine Learning Workflow

The Machine Learning development process is organized into the following stages:

### 1. Data Exploration and Analysis

The housing dataset is explored to understand its structure, features, distributions, and relationships between different property characteristics.

### 2. Data Preprocessing

The dataset is prepared for Machine Learning by handling the required feature transformations and preparing the input features.

### 3. Feature Engineering and Preparation

The property features are prepared in a format suitable for the prediction model, including the handling of categorical and numerical features.

### 4. Model Training and Optimization

A Random Forest Regression model is trained to learn the relationship between housing features and their corresponding prices.

Model optimization is performed using a Grid Search approach.

### 5. Model Persistence

After training, the model and its preprocessing components are saved as serialized `.pkl` files using Joblib.

This allows the backend to load and reuse the trained components without retraining the model every time the server starts.

### 6. Model Deployment

The trained model is integrated into a FastAPI application, allowing external applications to send property information and receive price predictions.

---

## ⚙️ Backend Architecture

The backend follows a modular structure to keep the application organized and maintainable.

### Main Components

**1. FastAPI Application (`main.py`)**

Initializes the FastAPI application and registers the prediction router.

**2. Request Schema (`request_schema.py`)**

Defines the expected property features and validates their values using Pydantic.

The model accepts the following features:

- Bedrooms
- Bathrooms
- Living Area
- Lot Area
- Floors
- Waterfront
- View
- Condition
- Above-Ground Area
- Basement Area
- Year Built
- Year Renovated
- City
- State ZIP Code

**3. Enum Classes (`enum_classes.py`)**

Defines the accepted categorical values for features such as city, state ZIP code, waterfront, view, and condition.

**4. Configuration (`config.py`)**

Loads environment variables and initializes the saved preprocessing components and trained Random Forest model.

**5. Inference (`inference.py`)**

Responsible for the prediction process:

1. Receives validated property information.
2. Converts the input into a dictionary.
3. Maps categorical values into their corresponding numerical representations.
4. Converts the data into a Pandas DataFrame.
5. Applies the saved preprocessing components.
6. Passes the processed data to the trained model.
7. Converts the predicted value back from the logarithmic scale using `np.expm1()`.
8. Returns the final predicted house price.

**6. Prediction Router (`random_forest_router.py`)**

Handles incoming prediction requests and verifies the API Key before executing the prediction process.

---

## 🚀 Getting Started

Follow these steps to download, configure, and run the project locally.

### Prerequisites

Before starting, make sure you have installed:

- Python 3.11 or a compatible Python version.
- Git.
- pip (Python package installer).

---

## 💻 Installation and Setup

### Step 1: Clone the Repository

Open your terminal or command prompt and run:

```bash
git clone https://github.com/zaDev-eg/House-Price-Prediction.git
```

Navigate to the project directory:

```bash
cd House-Price-Prediction
```

### Step 2: Create a Virtual Environment

It is recommended to use a virtual environment to isolate the project dependencies.

```bash
python -m venv .venv
```

Activate the virtual environment.

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**

```cmd
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### Step 3: Upgrade pip

```bash
python -m pip install --upgrade pip
```

### Step 4: Install Project Dependencies

All required Python packages are listed in the `requirements.txt` file.

Install them using:

```bash
pip install -r requirements.txt
```

**Important:** The project uses FastAPI with its standard server dependencies. If you encounter a missing server dependency when trying to run the application, follow the additional installation instructions in the Troubleshooting section below.

---

## 🔐 Environment Configuration

The application requires environment variables to configure the backend.

Navigate to the `src` directory and create a `.env` file based on the provided `.env.example` file.

**Windows:**

```powershell
Copy-Item src/.env.example src/.env
```

**Linux / macOS:**

```bash
cp src/.env.example src/.env
```

Open `src/.env` and configure the variables:

```env
APP_NAME="House Price Prediction"
APP_VERSION="1.0.0"
SECRET_KEY="your_custom_secret_key"
```

**Important Notes:**

- Replace `your_custom_secret_key` with your own secret key.
- The `SECRET_KEY` must match the API Key sent with prediction requests.
- Keep your `.env` file private.
- Never upload your actual secret key to GitHub.

---

## ▶️ Running the Server

After completing the installation and environment configuration, make sure you are inside the main project directory:

```text
House-Price-Prediction/
```

Run the FastAPI application using:

```bash
uvicorn src.main:app --reload
```

If everything is configured correctly, the server will start locally.

You should be able to access the application at:

```text
http://127.0.0.1:8000
```

To check whether the server is running, open:

```text
http://127.0.0.1:8000/
```

Expected response:

```json
"The Server Is Up And Running ✅"
```

---

## 📚 API Documentation

FastAPI automatically generates interactive API documentation.

After starting the server, open:

**Swagger UI:**

```text
http://127.0.0.1:8000/docs
```

**ReDoc:**

```text
http://127.0.0.1:8000/redoc
```

These interfaces allow you to explore the available endpoints, inspect the expected parameters, and test API requests.

### Available Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Checks whether the server is running |
| POST | `/forest_prediction` | Predicts a house price using the trained Random Forest model |

### Prediction Endpoint

**Endpoint:**

```text
POST /forest_prediction
```

**Authentication:**

The prediction endpoint requires an API Key.

Add the following HTTP header to your request:

```text
X_API_Key: your_custom_secret_key
```

The value must match the `SECRET_KEY` configured in your `.env` file.

**Input Parameters:**

The prediction endpoint accepts the property features defined in `ModelData`.

You can inspect all accepted values and validation constraints directly through Swagger UI.

**Successful Response Example:**

```json
{
    "prediction_state": "model prediction is ended successfully ✅",
    "final_prediction": 350000.00
}
```

The returned prediction represents the estimated house price.

*Note: The value above is an illustrative example, not a guaranteed model prediction.*

---

## 🛠️ Troubleshooting

### 1. FastAPI Standard Dependencies Issue

**Problem:**

When running the server for the first time, you may encounter an error indicating that an additional FastAPI server dependency is missing.

This happens because installing the basic `fastapi` package does not necessarily install all the standard optional dependencies required to run the application using Uvicorn.

**Solution:**

Install FastAPI with its standard dependencies:

```bash
pip install "fastapi[standard]==0.162.2"
```

This installs FastAPI along with its standard optional dependencies, including Uvicorn.

After installation, try running the server again:

```bash
uvicorn src.main:app --reload
```

**Important:** The project pins FastAPI to version `0.162.2` in its requirements file, so the installation command above preserves that version.

### 2. ModuleNotFoundError

If you encounter a `ModuleNotFoundError`, make sure:

- Your virtual environment is activated.
- All dependencies have been installed.
- You are running the command from the main project directory.

You can reinstall the dependencies using:

```bash
pip install -r requirements.txt
```

### 3. Environment Variable Errors

If the application cannot load the required environment variables:

- Make sure the `.env` file exists inside the `src` directory.
- Check that the variable names are correct.
- Make sure `SECRET_KEY` has been configured.

### 4. API Key Authentication Error

If you receive a `401 Unauthorized` response, verify that the `X_API_Key` header contains exactly the same value configured in your `.env` file.

---

## 👨‍💻 Author

**zaDev-eg**

GitHub: [https://github.com/zaDev-eg](https://github.com/zaDev-eg)

Project Repository: [House-Price-Prediction](https://github.com/zaDev-eg/House-Price-Prediction)

---

## ⭐ Support

If you find this project useful, consider giving the repository a star on GitHub!