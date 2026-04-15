
# Day 4 - Disease Advice System

## Project Title:
Vitamin Deficiency Detection using Machine Learning

---

## 1. Objective

The objective of Day-4 was to enhance the machine learning model by providing meaningful outputs such as disease descriptions and precautionary measures.

---

## 2. Datasets Used

- dataset.csv (main dataset with symptoms and diseases)
- symptom_Description.csv (contains disease descriptions)
- symptom_precaution.csv (contains precautionary measures)

---

## 3. Approach

### Step 1: Data Loading
Loaded all datasets using pandas.

### Step 2: Data Cleaning
Handled missing values and ensured consistent column formatting.

### Step 3: Mapping Creation
- Created a dictionary for disease → description
- Created a dictionary for disease → precautions

### Step 4: Model Integration
Used the trained machine learning model from previous steps.

### Step 5: Prediction
Predicted disease based on input symptoms.

### Step 6: Output Enhancement
Displayed:
- Predicted disease
- Description
- Precautions

---

## 4. Sample Output
<img width="1616" height="238" alt="image" src="https://github.com/user-attachments/assets/98a45360-4adc-4dda-ae93-f5f53c79d6aa" />

---

## 5. Outcome

- Successfully integrated machine learning predictions with real-world advice
- Improved usability of the system
- Prepared the model for web application development

---

## 6. Next Step

- Build backend using Flask
- Connect model with web interface
