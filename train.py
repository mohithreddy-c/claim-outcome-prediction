"""TODO: train, evaluate, and persist the full ML pipeline."""
from pathlib import Path
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from features import ClaimFeatureEngineer

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "claims.csv"
MODEL_PATH = ROOT / "model" / "claim_model.joblib"
CLASS_ORDER = ["Paid", "Partially_Paid", "Denied"]

def main():
    # TODO 1: Load CSV; separate target and features; exclude id.
    # TODO 2: Split with test_size=0.2, fixed random_state, stratify=y.
    # TODO 3: Define numeric/categorical preprocessing.
    # TODO 4: Build a Pipeline: feature engineer -> preprocessor -> classifier.
    # TODO 5: Fit on training data only.
    # TODO 6: Print per-class precision/recall/F1 and confusion matrix.
    # TODO 7: Save the complete fitted pipeline to MODEL_PATH with joblib.
    raise NotImplementedError("Complete model training and evaluation.")

if __name__ == "__main__":
    main()
