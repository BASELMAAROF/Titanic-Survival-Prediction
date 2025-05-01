![Banner](static/titanic_banner.png)

# Titanic Survival Prediction 🚢

A machine learning project that predicts survival on the Titanic using demographic and passenger features from the Kaggle dataset.

---

## 📂 Project Structure

Titanic-Survival-Prediction/ ├── data/ # Dataset files (train.csv, test.csv, gender_submission.csv) ├── static/ # Banner or image files ├── templates/ # HTML templates for web display (if Flask used) ├── titanic_model/ # Python scripts (model, test, app) │ ├── titanic_analysis.py │ ├── test.py │ └── app.py ├── README.md # Project README (this file) └── requirements.txt # Python dependencies



---

## 📊 Dataset

This project uses the [Kaggle Titanic Dataset](https://www.kaggle.com/c/titanic/data), which includes:

- `train.csv`: Training data with features and survival labels  
- `test.csv`: Test data for model prediction  
- `gender_submission.csv`: Sample submission format

---

## ⚙️ Technologies Used

- **Python** (Pandas, NumPy, Scikit-learn)  
- **Jupyter Notebook**  
- **Matplotlib / Seaborn** (for visualization)  
- **Flask** (if web interface used)

---

## 🔍 Key Features

- Data cleaning and preprocessing  
- Exploratory Data Analysis (EDA)  
- Feature engineering (e.g., encoding, missing values)  
- Model building: Logistic Regression, Random Forest, XGBoost  
- Model evaluation and accuracy comparison  
- Optional: Web deployment with Flask

---

## 📈 Model Results

- Best model: `Logistic Regression` (update with your real results!)
- Validation accuracy: `~X%`  
- Insight: Females and 1st-class passengers had higher survival rates

---

## 🚀 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/BASELMAAROF/Titanic-Survival-Prediction.git
cd Titanic-Survival-Prediction

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run analysis
python titanic_model/titanic_analysis.py
