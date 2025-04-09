import os
import sys
import dill
from sklearn.metrics import silhouette_score
from sklearn.model_selection import GridSearchCV
from src.exception import CustomError

def save_object(file_path, obj):
    """Saves a Python object using dill serialization."""
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomError(e, sys)

def evaluate_unsupervised_models(x_data, models, param_grid):
    """
    Evaluates unsupervised models using GridSearchCV or custom loops.
    Returns a score report based on silhouette score.
    """
    try:
        report = {}

        for model_name, model in models.items():
            grid_search = GridSearchCV(model, param_grid[model_name], cv=[(slice(None), slice(None))], n_jobs=-1, verbose=1)
            grid_search.fit(x_data)

            best_model = grid_search.best_estimator_
            labels = best_model.fit_predict(x_data)

            # Some models may assign -1 to outliers (like DBSCAN), which can affect silhouette score
            if len(set(labels)) > 1 and len(set(labels)) < len(x_data):
                score = silhouette_score(x_data, labels)
            else:
                score = -1  # invalid score

            report[model_name] = score

        return report

    except Exception as e:
        raise CustomError(e, sys)
