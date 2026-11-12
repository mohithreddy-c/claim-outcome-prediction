"""TODO: reusable feature engineering for training and inference."""
from sklearn.base import BaseEstimator, TransformerMixin

class ClaimFeatureEngineer(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        # TODO: fit training-only statistics here if target-derived features are used.
        return self

    def transform(self, X):
        # TODO: return a copy with at least two engineered features.
        # Never use test labels or future information.
        raise NotImplementedError("Complete feature engineering.")
