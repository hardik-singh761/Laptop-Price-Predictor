# 💻 Laptop Price Predictor

A data science project to predict the price of laptops based on key specifications such as RAM, processor type, storage, screen size, GPU brand, and more. This end-to-end machine learning project includes data cleaning, exploratory data analysis (EDA), feature engineering, model training, evaluation, and deployment.

## 📌 Project Objective

To build a regression model that accurately predicts laptop prices using various laptop configuration features. The goal is to assist buyers and sellers in estimating a fair price for laptops based on specifications.

## 🔗 Project Link

👉 [GitHub Repository](https://github.com/hardik-singh761/Laptop-Price-Predictor)
👉 [Live Link](https://lnkd.in/gWUuDA-A)
![Screenshot (96)](https://github.com/user-attachments/assets/8f2493ad-ea67-4d99-985c-6de6aaf65c05)
---

## 📁 Dataset

The dataset used contains various features such as:

- **Company** – Manufacturer brand (e.g., Dell, HP)
- **TypeName** – Type of laptop (e.g., Ultrabook, Gaming)
- **RAM** – Size in GB
- **Weight** – Weight of the laptop
- **Touchscreen**, **IPS** – Display features
- **Screen Size** and **Resolution**
- **CPU**, **GPU**, **HDD**, **SSD**, **Operating System**
- **Price** – Target variable

> 📌 The dataset was sourced from Kaggle or scraped from online laptop retail sites.

---

## 🧹 Workflow

### 1. Data Cleaning
- Converted string-formatted features (e.g., "8GB", "1TB") to numerical.
- Handled missing values and removed duplicates.

### 2. Exploratory Data Analysis (EDA)
- Price distribution plots
- Correlation heatmaps
- Brand-wise and feature-wise price comparisons

### 3. Feature Engineering
- Extracted CPU and GPU brands
- Parsed resolution to calculate PPI (Pixels Per Inch)
- Derived binary indicators for features like touchscreen and IPS display

### 4. Encoding & Scaling
- Used **OneHotEncoder** and **StandardScaler** to preprocess categorical and numerical features.

### 5. Model Training
- Tested multiple regression algorithms:
  - **Linear Regression**
  - **Ridge/Lasso Regression**
  - **Random Forest Regressor**
  - **XGBoost Regressor**

- Selected the best model based on **R² Score**, **MAE**, and **RMSE**.

### 6. Deployment
- Final model saved using `joblib`
- Optional: Streamlit web app (if implemented)

---

## 🛠️ Technologies Used

- Python
- Jupyter Notebook
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- XGBoost
- Joblib

---

## 📊 Model Performance

| Model                | R² Score | MAE   | RMSE  |
|---------------------|---------:|------:|------:|
| Random Forest        | 0.89     | ~2100 | ~2500 |
| XGBoost              | 0.91     | ~1900 | ~2300 |
| Linear Regression    | 0.75     | ~3500 | ~4000 |

✅ XGBoost Regressor gave the best results and was chosen as the final model.

---

## 📌 Future Work

- Add a Streamlit interface for users to input specs and get price predictions
- Add cross-validation for more robust performance
- Deploy via Flask + Docker or render using HuggingFace Spaces

---

## 🤝 Contributors

- **Hardik Singh**  
  Data Science Intern @ Unified Mentor  
  [GitHub](https://github.com/hardik-singh761)

---

## 📃 License

This project is licensed under the MIT License. Feel free to use and modify the code.

