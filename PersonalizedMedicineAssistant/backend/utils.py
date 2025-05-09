import pandas as pd
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)


def load_dataset(file_path, expected_columns=None):
    """
    Load a dataset and handle missing values with validation for expected columns.
    """
    if os.path.exists(file_path):
        try:
            data = pd.read_csv(file_path)
            if data.empty:
                logging.warning(f"Dataset at {file_path} is empty.")
            # Handle missing values
            data.fillna('Unknown', inplace=True)

            # Validate expected columns
            if expected_columns:
                missing_columns = set(expected_columns) - set(data.columns)
                if missing_columns:
                    logging.warning(f"Missing columns in {file_path}: {missing_columns}")

            logging.info(f"Loaded dataset: {file_path}")
            return data
        except Exception as e:
            logging.error(f"Error loading {file_path}: {e}")
            return pd.DataFrame()  # Return an empty DataFrame instead of None
    else:
        logging.warning(f"Warning: {file_path} not found.")
        return pd.DataFrame()


def load_general_disease_data(base_path):
    """
    Load general disease datasets from the given base path with validation.
    """
    general_data_files = {
        "description.csv": ["Disease", "Description"],  # Expected columns
        "diets.csv": ["Disease", "Diet"],
        "medications.csv": ["Disease", "Medication"],
        "precautions_df.csv": ["Disease", "Precaution"],
        "symptoms_df.csv": ["Disease", "Symptom"],
        "workout_df.csv": ["Disease", "Workout"],
        "Training.csv": ["prognosis"]  # Main training dataset
    }

    data = {}
    for file, expected_columns in general_data_files.items():
        file_path = os.path.join(base_path, "general", file)  # Path to general folder
        dataset = load_dataset(file_path, expected_columns)
        if not dataset.empty:
            data[file.split('.')[0]] = dataset

    return data


def load_cancer_data(base_path):
    """
    Load cancer-related datasets from the given base path with validation.
    """
    cancer_data_files = {
        "Symptom-severity.csv": ["Symptom", "Severity"],
        "Final_Augmented_dataset_Diseases_and_Symptoms.csv": ["Disease", "Symptoms"],
        "symptom_Description.csv": ["Symptom", "Description"],
        "symptom_precaution.csv": ["Symptom", "Precaution"]
    }

    data = {}
    for file, expected_columns in cancer_data_files.items():
        file_path = os.path.join(base_path, "cancer", file)
        dataset = load_dataset(file_path, expected_columns)
        if not dataset.empty:
            data[file.split('.')[0]] = dataset

    return data


def clean_user_input(user_input):
    """
    Clean user input by removing extra spaces and making all words lowercase.
    """
    symptoms = [symptom.strip().lower() for symptom in user_input.split(',') if symptom.strip()]
    return symptoms


if __name__ == "__main__":
    # Base path where your datasets are stored
    base_path = "backend/Data Sets"

    # Load general disease data
    general_disease_data = load_general_disease_data(base_path)

    # Print the columns of the general disease training dataset as a check
    if general_disease_data and 'Training' in general_disease_data:
        logging.info(f"Dataset columns: {general_disease_data['Training'].columns}")
    else:
        logging.error("General disease dataset 'Training' is missing or could not be loaded.")

    # Load cancer-related data
    cancer_data = load_cancer_data(base_path)

    # If cancer data is loaded successfully, log the dataset columns
    if cancer_data:
        for cancer_file, dataset in cancer_data.items():
            logging.info(f"Loaded cancer dataset: {cancer_file}")
            logging.info(f"Columns: {dataset.columns}")
    else:
        logging.error("Cancer datasets could not be loaded.")

    # Ask the user for symptoms input
    user_input = input("Enter your symptoms separated by commas: ").strip()
    if user_input:
        symptoms = clean_user_input(user_input)
        if symptoms:
            logging.info(f"User symptoms: {symptoms}")
        else:
            logging.warning("No valid symptoms were entered.")
    else:
        logging.warning("Empty input received from the user.")
