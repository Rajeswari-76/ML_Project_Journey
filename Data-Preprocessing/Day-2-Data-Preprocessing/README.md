
# Day 2 - Data Preprocessing and Model Building

## Project Title:
Vitamin Deficiency Detection using Machine Learning

---

## 1. Objective

The goal of Day-2 was to work with the dataset, preprocess the data, and build a basic machine learning model for prediction.

---

## 2. Dataset Understanding

The dataset contains:
- Disease (target/output)
- Multiple symptom columns (Symptom_1, Symptom_2, ...)

Each row represents a patient with a set of symptoms and the corresponding disease.

---

## 3. Data Preprocessing

### 3.1 Handling Missing Values
- Missing values (NaN) in symptom columns were replaced with "None"

### 3.2 Feature Transformation
- Symptoms were originally in text format across multiple columns
- Converted into a binary format (0/1)
  - 1 → symptom present
  - 0 → symptom absent

This transformation was necessary to make the data suitable for machine learning models.

---

## 4. Feature and Target Separation

- Features (X): Symptoms in binary format
- Target (y): Disease column

---

## 5. Encoding Target Variable

- Disease labels (text) were converted into numerical values using Label Encoding

---

## 6. Model Building

A classification model was trained using:

- Random Forest Classifier

The model learns the relationship between symptoms and diseases.

---

## 7. Model Evaluation

- Data was split into training and testing sets
- Model performance was evaluated using accuracy

---

## 8. Outcome

- Successfully converted raw symptom data into machine-learning-friendly format
- Trained a model to predict diseases based on symptoms
- Achieved good accuracy on test data

---

## 9. Learning Outcomes

- Understanding real-world dataset structure
- Handling categorical data
- Feature engineering using symptom encoding
- Training a machine learning model

---

## 10. Next Step

- Improve model performance
- Compare multiple algorithms (SVM, Random Forest)
- Integrate model into a web application
