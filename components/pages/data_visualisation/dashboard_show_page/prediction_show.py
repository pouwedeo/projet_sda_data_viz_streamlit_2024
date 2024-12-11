import pandas as pd
import  plotly.express as px
import numpy as np
import  streamlit as st
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier
from sklearn.model_selection import  train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression

# Exemple de dataset
def prdiction(data):
    data["success"] = np.where(data["state"] == "successful", 1, 0)

    # Encodage One-Hot
    encoder = OneHotEncoder(sparse_output=False)
    encoded_features = encoder.fit_transform(data[['category', 'country']])
    encoded_columns = encoder.get_feature_names_out(['category', 'country'])
    encoded_df = pd.DataFrame(encoded_features, columns=encoded_columns)

    # Combiner avec les données numériques
    processed_data = pd.concat([data[['goal', 'duration', 'success']], encoded_df], axis=1)
    print(processed_data)

    # Remplacer les valeurs manquantes par la moyenne
    processed_data['goal'] = processed_data['goal'].fillna(processed_data['goal'].mean())

    # Gestion des anomalies - couper à 3 écart-types
    processed_data['goal'] = processed_data['goal'].clip(lower=processed_data['goal'].mean() - 3 * processed_data['goal'].std(),
                                                             upper=processed_data['goal'].mean() + 3 * processed_data['goal'].std())
    scaler = StandardScaler()
    processed_data[['goal', 'duration']] = scaler.fit_transform(processed_data[['goal', 'duration']])
    print(processed_data)

    scaler = StandardScaler()
    processed_data[['goal', 'duration']] = scaler.fit_transform(processed_data[['goal', 'duration']])
    print(processed_data)

    #2
    X = processed_data.drop('success', axis=1)
    y = processed_data['success']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    xgb_model = XGBClassifier(eval_metric='logloss', use_label_encoder=False, random_state=42)
    xgb_model.fit(X_train, y_train)
    param_grid = {
        'n_estimators': [50, 100, 150],
        'max_depth': [3, 5, 7],
        'learning_rate': [0.01, 0.1, 0.2]
    }

    grid_search = GridSearchCV(xgb_model, param_grid, cv=2, scoring='roc_auc', n_jobs=-1)
    grid_search.fit(X_train, y_train)

    print("Best Parameters:", grid_search.best_params_)

    xgb_best = grid_search.best_estimator_
    xgb_preds = xgb_best.predict_proba(X_test)[:, 1]
    if len(y_test.unique()) > 1:
        auc_roc = roc_auc_score(y_test, xgb_preds)
        print("XGBoost AUC-ROC:", auc_roc)
    else:
        print("Impossible de calculer l'AUC-ROC : y_test contient une seule classe.")

    print(classification_report(y_test, (xgb_preds > 0.5).astype(int)))



    #3

    important_features = xgb_best.feature_importances_.argsort()[-5:]  # Top 5 features
    X_train_reduced = X_train.iloc[:, important_features]
    X_test_reduced = X_test.iloc[:, important_features]

    log_reg = LogisticRegression()
    log_reg.fit(X_train_reduced, y_train)

    log_preds = log_reg.predict_proba(X_test_reduced)[:, 1]
    if len(y_test.unique()) > 1:
        auc_roc = roc_auc_score(y_test, log_preds)
        print("Logistic Regression AUC-ROC:", auc_roc)
    else:
        print("Impossible de calculer l'AUC-ROC : y_test contient une seule classe.")


    print("Coefficients:", log_reg.coef_)

    #4

    xgb_scores = cross_val_score(xgb_best, X, y, cv=2, scoring='roc_auc')
    log_scores = cross_val_score(log_reg, X.iloc[:, important_features], y, cv=2, scoring='roc_auc')

    print("XGBoost Cross-Validation AUC:", xgb_scores.mean())
    print("Logistic Regression Cross-Validation AUC:", log_scores.mean())

    #5

    # Combinaison des prédictions avec une pondération
    final_preds = 0.7 * xgb_preds + 0.3 * log_preds
    if len(y_test.unique()) > 1:
        hybrid_auc = roc_auc_score(y_test, final_preds)
        print("Hybrid Model AUC-ROC:", hybrid_auc)
    else:
        print("Impossible de calculer l'AUC-ROC : y_test contient une seule classe.")

    #6





    important_features = np.argsort(xgb_best.feature_importances_)[::-1]  # Indices triés par importance
    feature_names = X.columns[important_features]  # Obtenir les noms des colonnes
    feature_importances = xgb_best.feature_importances_[important_features]  # Importances correspondantes

    # Convertir les données en DataFrame pour Plotly


    importance_df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": feature_importances
    })

    # Créer un graphique avec Plotly
    fig = px.bar(
        importance_df,
        x="Importance",
        y="Feature",
        orientation="h",
        title="XGBoost Feature Importance",
        color="Importance",
        color_continuous_scale="Blues"
    )

    fig.update_layout(
        yaxis=dict(categoryorder="total ascending"),  # Tri des caractéristiques par importance
        xaxis_title="Feature Importance",
        yaxis_title="Features",
        title_x=0.5,  # Centrer le titre
    )

    # Afficher le graphique dans Streamlit
    st.plotly_chart(fig)