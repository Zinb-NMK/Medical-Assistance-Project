## 📌 Project Title: Disease Prediction and Recommendation System

### 📝 Project Overview:

This project is a Machine Learning-based Disease Prediction System that predicts possible diseases based on symptoms entered by the user. The system uses a **Random Forest Classifier** trained on a medical dataset to suggest the top 5 most likely diseases. It also provides detailed recommendations, including disease descriptions, precautions, medications, workout plans, and dietary suggestions.

---

### 📂 Project Structure:

```
DiseasePrediction/
├── Data Sets/                      # Dataset folder
│   ├── Training.csv                # Training dataset
│   ├── symptoms_df.csv             # Symptom data
│   ├── precautions_df.csv          # Precaution data
│   ├── workout_df.csv              # Workout data
│   ├── description.csv             # Disease descriptions
│   └── medications.csv             # Medication recommendations
├── models/
│   └── svc.pkl                     # Saved Random Forest model
├── main.py                         # Main script for prediction
└── README.md                       # Project documentation
```

---

### 🚀 Installation and Setup:

1. Clone the repository:

   ```bash
   git clone https://github.com/username/DiseasePrediction.git
   cd DiseasePrediction
   ```
2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the prediction script:

   ```bash
   python main.py
   ```

---

### 💡 Features:

1. **Disease Prediction**

   * Enter symptoms separated by commas.
   * The model suggests the top 5 diseases with confidence scores.

2. **Recommendations Provided**:

   * Description
   * Precautions
   * Medications
   * Workout Plans
   * Diet Plans

---

### 📊 Model Training:

* **Algorithm Used:** Random Forest Classifier
* **Accuracy:** Approximately 98%
* **Cross-Validation Accuracy:** Around 97%
* **Model Training Process:**

  * Uses `RandomForestClassifier` with 200 estimators.
  * Data is split into training (70%) and testing (30%) sets.
  * Cross-validated using `StratifiedKFold` with 5 splits.

---

### 🔍 Prediction Logic:

* User symptoms are taken as input.
* The symptoms are mapped to a binary vector representing the input features.
* The model predicts disease probabilities based on the vector.
* Top 5 diseases with the highest confidence are displayed.
* Additional details like medications, diets, and precautions are fetched from respective datasets.

---

### 🗂️ Datasets Used:

1. `Training.csv`: Main dataset for model training.
2. `symptoms_df.csv`: List of symptoms.
3. `precautions_df.csv`: Suggested precautions for diseases.
4. `workout_df.csv`: Workout recommendations for diseases.
5. `description.csv`: Disease descriptions.
6. `medications.csv`: Medication information.

---

### 💾 Model Saving and Loading:

* The trained model is saved using `pickle` for quick inference.
* Model path: `models/svc.pkl`

---

### ✅ Example Usage:

```
Enter your symptoms separated by commas: headache, fever, cough

========= Possible Disease 1: Common Cold (Confidence: 89.45%) =========
========= Description: =========
Common cold is a viral infection affecting the upper respiratory tract.
========= Precautions: =========
1 : Drink plenty of fluids.
2 : Get enough rest.
3 : Use a humidifier.
4 : Avoid close contact with infected individuals.
========= Medications: =========
1 : Paracetamol
2 : Antihistamines
========= Workout: =========
1 : Light stretching
2 : Breathing exercises
========= Diets: =========
1 : Warm soups
2 : Herbal tea
```

---

### 🔄 Future Enhancements:

1. Web-based UI: Integrate a user-friendly web interface using Django or Flask to allow users to interact with the prediction system through a browser.
2. More Datasets: Add more diverse datasets to improve the generalization of the model and include additional diseases for prediction.
3. Interactive Chatbot: Implement a conversational chatbot for a more interactive experience, enabling users to discuss symptoms and receive predictions.
4. Mobile App Integration: Create a mobile application (Android/iOS) to allow users to access the disease prediction system on the go.
5. Multi-Model Integration: Integrate multiple models, such as Support Vector Machines (SVM) or Neural Networks, and use an ensemble approach for improved predictions.
6. Real-time Symptom Input: Enable real-time symptom input through voice or text for a more seamless user experience.
7. Integration with Medical Databases: Fetch real-time medical data, such as the latest medication or treatment methods, using external APIs.
8. Personalized Treatment Plans: Use machine learning to recommend personalized treatment plans, combining medications, workouts, and diets based on the user’s medical history and preferences.
9. Multi-language Support: Add multi-language support to make the system accessible to users worldwide.
10. Disease Risk Prediction: Implement a feature to predict the risk of developing certain diseases based on lifestyle, family history, and other factors.

---

### 👥 Contributors:

* **Nagaram ManojKumar** - Developer and AI/ML Enthusiast

---

### 📧 Contact:

If you have any questions or suggestions, feel free to reach out at \[[nagarammanojkumar3@gmail.com](mailto:your-email@example.com)]
