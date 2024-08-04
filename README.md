# PortfolioProject

## Problem Statement
Insurance companies need accurate health insurance cost predictions to set premiums appropriately. Traditional methods often use broad actuarial tables and historical averages, which may not account for individual differences. Leveraging machine learning can lead to more competitive pricing and better risk management.

## Project Need
Accurate predictions can:
- Enhance precision in pricing
- Increase competitiveness
- Improve customer satisfaction
- Enable personalized offerings
- Refine risk assessment
- Inform policy development
- Aid strategic decision-making
- Boost customer engagement

## Data Description
The dataset comprises 11 attributes:
- Age: 18-66 years
- Diabetes, BloodPressureProblems, AnyTransplants, AnyChronicDiseases, KnownAllergies, HistoryOfCancerInFamily: Binary (0 or 1)
- Height: 145-188 cm
- Weight: 51-132 kg
- NumberOfMajorSurgeries: 0-3
- PremiumPrice: 15,000-40,000

## Tableau Visualization
### Goal
- Visualize key data points
- Predict insurance costs
- Generate strategic insights

### Interactive Features
- Filters, sliders, drill-down capabilities, tooltips
- Insights gathering: Predictive insights, risk profiles, policy recommendations

## EDA and Hypothesis Testing
### Goals
- Visualize distributions, identify outliers, explore correlations
- Test hypotheses on premium costs based on health conditions and demographics

### Methods
- Distribution analysis
- Correlation analysis
- Outlier detection
- Hypothesis testing: T-tests, ANOVA, Chi-square tests, regression analysis

## ML Modeling
### Data Preprocessing
- Handle missing values, feature engineering, scaling, and encoding

### Model Selection
- Linear regression, tree-based models, neural networks

### Evaluation
- Cross-validation, performance metrics (RMSE, MAE, R²), confidence intervals

### Interpretability
- Feature importance, model insights

## Deployment
### Objectives
- Accessibility, real-time estimations, user-friendly interface

### Process
- Flask API: Backend handling requests and predictions
- Streamlit Application: User input forms and real-time predictions

## Files
1. `EDA & Hypothesis Testing.ipynb`
2. `ML Modeling.ipynb`
3. `app.py`
4. `optimized_rf_model.pkl`

## Links
- [Dataset](https://drive.google.com/file/d/1NBk1TFkK4NeKdodR2DxIdBp2Mk1mh4AS/view?usp=drive_link)
- [Tableau Public](https://public.tableau.com/app/profile/praneeth.kumar.maddula/viz/InsuranceCostPrediction/Dashboard1)
- [GitHub repository](https://github.com/Pranee-007/PortfolioProject)
- [Technical Blog](https://medium.com/@praneethkumar_88970/insurance-cost-prediction-using-machine-learning-0b7b27b0c21c)
- [Demo Video](https://www.loom.com/looms/videos)
