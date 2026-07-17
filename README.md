# Swiggy Delivery Time Prediction

## Project Overview

This project predicts the estimated delivery time (in minutes) for Swiggy food orders using Machine Learning. The model leverages customer, rider, restaurant, weather, traffic, geospatial, and temporal information to provide accurate delivery time predictions before the order is dispatched. The application is deployed using **Streamlit** and can be hosted on **Hugging Face Spaces** for public access.

## Business Problem

Swiggy processes millions of food deliveries across hundreds of cities every month. Providing an accurate Estimated Time of Arrival (ETA) is essential for customer satisfaction and efficient delivery operations.

Inaccurate ETAs can lead to:
- Reduced customer trust and repeat orders
- Increased order cancellations and refund costs
- Higher customer support workload
- Inefficient rider allocation
- Increased operational costs

The objective of this project is to build a production-ready Machine Learning model that predicts delivery time accurately using real-time and historical order information.

## Dataset

**Source:** Swiggy Delivery Time Prediction Dataset

**Target Variable:** 'Time_taken' (Delivery Time in Minutes)

**Dataset Size**
- Records: 45,502
- Features: 26

### Dataset Features

| Feature | Description |
|---------|-------------|
| Rider_id | Unique rider identifier |
| Age | Rider's age |
| Ratings | Rider's average rating |
| Vehicle_condition | Condition of delivery vehicle |
| Type_of_vehicle | Vehicle used for delivery |
| Type_of_order | Food order category |
| Multiple_deliveries | Number of deliveries assigned |
| Pickup_time_minutes | Restaurant preparation time |
| Restaurant Latitude & Longitude | Restaurant location |
| Delivery Latitude & Longitude | Customer location |
| Distance | Distance between restaurant and customer |
| Weather | Weather condition |
| Traffic | Traffic condition |
| Festival | Festival indicator |
| City_type | Urban / Metropolitan |
| City_name | Delivery city |
| Order_date | Order date |
| Order_day | Day of month |
| Order_month | Month |
| Order_day_of_week | Day of week |
| Is_weekend | Weekend indicator |
| Order_time_hour | Order hour |
| Order_time_of_day | Morning / Afternoon / Evening / Night |
| Time_taken | Actual delivery time (Target) |

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Streamlit
- Pickle

## Exploratory Data Analysis (EDA)

The following analyses were performed:

- Missing Value Analysis
- Duplicate Value Check
- Data Type Validation
- Statistical Summary
- Feature Distribution Analysis
- Correlation Analysis
- Outlier Detection
- Categorical Feature Analysis
- Target Variable Analysis

## Data Preprocessing

The dataset was preprocessed using Scikit-learn Pipelines.

Preprocessing steps include:

- Handling Missing Values
- Encoding Categorical Features
- Feature Scaling
- Feature Engineering
- ColumnTransformer
- Pipeline Implementation
- Train-Test Split

## Feature Engineering

Several new features were created to improve model performance.

- Distance
- Pickup Time Minutes
- Order Time Hour
- Order Day
- Order Month
- Order Day of Week
- Weekend Indicator
- Time of Day

## Machine Learning Models

The following regression models were trained and evaluated:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Support Vector Regressor (SVR)
- Gradient Boosting Regressor
- XGBoost Regressor

## Hyperparameter Tuning

Hyperparameter tuning was performed to optimize model performance.

Parameters tuned include:

- n_estimators
- max_depth
- learning_rate
- min_samples_split
- min_samples_leaf
- subsample
- colsample_bytree

The best hyperparameters were selected based on the highest Cross-Validation Score and lowest prediction error.

## Cross Validation

To ensure model robustness and generalization, **5-Fold Cross Validation** was performed for each model.

Cross-validation helps reduce overfitting and provides a reliable estimate of model performance on unseen data.

## Model Evaluation Metrics

Models were evaluated using:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

Training and Testing scores were compared to identify underfitting and overfitting.

## Best Model

After comparing multiple Machine Learning algorithms, **XGBoost Regressor** achieved the best overall performance due to:

- Highest R² Score
- Lowest RMSE
- Strong Cross-Validation Performance
- Better Generalization on Unseen Data

## Deployment

The trained Machine Learning model was deployed using **Streamlit**.

Users can:

- Enter delivery details
- Predict delivery time instantly
- Interact through a simple and intuitive web interface

The application can be hosted publicly using **Hugging Face Spaces**.

## Project Structure
swiggy_delivery_time_prediction/
│
├── app.py
├── requirements.txt
├── swiggy_delivery_time_prediction.pkl
├── README.md
└── images/

## Installation

Clone the repository

git clone https://github.com/harudra5/swiggy_delivery_time_prediction.git

Navigate to the project folder:
cd swiggy_delivery_time_prediction

Install dependencies:
pip install -r requirements.txt

Run the Streamlit application:
streamlit run app.py

## Live Demo:
Coming Soon (Hugging Face Spaces)

## Application Screenshots

### Home Page

<img width="401" height="372" alt="image" src="https://github.com/user-attachments/assets/d5c8e5ff-a045-4c4f-b81c-1669090b8137" />


### Prediction Result

<img width="425" height="399" alt="image" src="https://github.com/user-attachments/assets/1ad2f3f3-357a-4015-943b-69f65b7937ce" />


## Future Improvements

- Real-time Traffic API Integration
- Live Weather API Integration
- Route Optimization
- Deep Learning Models
- ETA Confidence Intervals
- Cloud Deployment
- Docker Containerization
- CI/CD Pipeline

## Author

**Harish Alakuntla**

Machine Learning | Data Science | Python
