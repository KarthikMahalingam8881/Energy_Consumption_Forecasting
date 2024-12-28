# Energy Consumption Forecasting

This project provides an in-depth analysis of energy consumption across multiple buildings to identify patterns, optimize usage, and forecast future energy demands. The analysis incorporates data preprocessing, visualization, and machine learning techniques to create actionable insights for energy efficiency and cost savings.

## Project Objectives

1. Analyze energy usage patterns across buildings.
2. Identify correlations between weather conditions and energy usage.
3. Develop predictive models (LSTM and XGBoost) to forecast energy consumption.
4. Suggest actionable recommendations for energy optimization.

## Features and Workflow

### 1. Data Cleaning and Preprocessing
- Integrated datasets: metadata, electricity usage, and weather.
- Handled missing values using techniques like forward-fill and interpolation.
- Normalized energy usage by square footage for fair comparisons across buildings.
- Removed irrelevant columns and outliers to ensure clean data for analysis.

### 2. Exploratory Data Analysis (EDA)
- **Monthly Trends**: Visualized energy consumption trends for different buildings.
- **Energy Efficiency**: Identified least and most energy-efficient buildings.
- **Weather Correlations**: Analyzed relationships between weather conditions (temperature, wind, cloud coverage) and energy usage.
- **Cost Analysis**: Estimated monthly and yearly energy costs.

### 3. Predictive Modeling
- **Models Used**:
  - **LSTM (Long Short-Term Memory)**: For sequence-based time-series forecasting.
  - **XGBoost**: For high-accuracy regression-based predictions.
- **Evaluation**:
  - Root Mean Squared Error (RMSE) to compare model performances.

### 4. Visualization and Insights
- Heatmaps and line charts for energy trends.
- Bubble charts combining energy efficiency, total usage, and projected costs.
- Bar charts comparing actual and predicted energy usage.

### 5. Recommendations
- **Short-Term**:
  - Perform energy audits for inefficient buildings.
  - Optimize HVAC schedules during off-peak hours.
  - Implement weather-responsive systems.
- **Long-Term**:
  - Invest in energy-efficient infrastructure.
  - Adopt smart energy management systems.
  - Explore renewable energy sources.

## Tools and Techniques

- **Programming Language**: Python
- **Libraries**:
  - Data Manipulation: `pandas`, `numpy`
  - Visualization: `matplotlib`, `seaborn`
  - Machine Learning: `scikit-learn`, `xgboost`, `tensorflow.keras`
- **Models**: LSTM, XGBoost
- **Metrics**: RMSE, correlation coefficients

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/KarthikMahalingam8881/energy-consumption-forecasting.git


## Results
- Highlighted inefficient buildings and cost-saving opportunities.
- Identified actionable strategies for energy efficiency.
- Engineered a time-series predictive model using XGBoost and deep learning (LSTM), achieving a 15% improvement in 
accuracy 
- Identified $223,110 in potential annual savings through quantitative analysis of energy inefficiencies across 24 buildings, 
contributing to 30% of energy costs, enhancing decision-making for energy optimization


## Future Work
- Incorporating external factors like economic data to enhance the forecasting model.
- Deploying the model as an API or web application for real-time energy consumption predictions.

## Contributions
Contributions are welcome! Please open an issue or submit a pull request for any bugs, enhancements, or new ideas.
