from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model
model = pickle.load(open("model/model.pkl", "rb"))
le = pickle.load(open("model/label_encoder.pkl", "rb"))

# Load datasets for description & precautions
desc_df = pd.read_csv("data/symptom_Description.csv")
prec_df = pd.read_csv("data/symptom_precaution.csv")

# Clean columns
desc_df.columns = desc_df.columns.str.strip()
prec_df.columns = prec_df.columns.str.strip()

# Create dictionaries
disease_desc = dict(zip(desc_df["Disease"], desc_df["Description"]))

disease_prec = {}
for i in range(len(prec_df)):
    disease = prec_df.iloc[i]["Disease"]
    precautions = prec_df.iloc[i][1:].dropna().values.tolist()
    disease_prec[disease] = precautions


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        symptoms = request.form.getlist("symptoms")

        input_data = np.array(symptoms, dtype=int).reshape(1, -1)

        prediction = model.predict(input_data)
        disease = le.inverse_transform(prediction)[0]

        description = disease_desc.get(disease, "No description available")
        precautions = disease_prec.get(disease, ["No precautions available"])

        return render_template(
            "index.html",
            disease=disease,
            description=description,
            precautions=precautions
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)