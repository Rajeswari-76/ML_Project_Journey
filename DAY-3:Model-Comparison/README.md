
# Day 3 - Model Comparison and Selection

## Project Title:
Vitamin Deficiency Detection using Machine Learning

---

## 1. Objective

The goal of Day-3 was to improve the model by training multiple machine learning algorithms and comparing their performance to select the best one.

---

## 2. Data Preparation

- Used the preprocessed dataset from Day-2
- Features (X): Symptoms in binary format
- Target (y): Disease labels
- Data was split into training and testing sets

---

## 3. Models Used

### 3.1 Random Forest
- Ensemble learning method using multiple decision trees
- Works well with high-dimensional data
- Does not require feature scaling

---

### 3.2 Support Vector Machine (SVM)
- Classification algorithm that separates data using decision boundaries
- Works well for structured data
- Requires feature scaling for better performance

---

## 4. Feature Scaling

- Applied StandardScaler to normalize the feature values
- Scaling was applied only for SVM model

---

## 5. Model Training

- Trained both Random Forest and SVM models on training data
- Each model learned the relationship between symptoms and diseases

---

## 6. Model Evaluation

- Predictions were made on test data
- Accuracy was calculated for both models

---

## 7. Model Comparison

- Compared accuracy scores of both models
- Identified the better-performing model

---

## 8. Final Model Selection

- Selected the model with higher accuracy
- Saved the final model using pickle as `final\_model.pkl`

---

## 9. Outcome

- Successfully trained and compared two machine learning models
- Selected the best model for disease prediction
- Prepared the model for integration into a web application

---

## 10. Learning Outcomes

- Understanding differences between machine learning algorithms
- Importance of feature scaling
- Model evaluation and comparison techniques

---

## 11. Next Step

- Integrate prediction with disease description and precautions
- Begin backend development for web application
