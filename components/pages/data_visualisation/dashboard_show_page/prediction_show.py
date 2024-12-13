import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns



# Data preprocessing
def preprocess_data(data):
    X = data[['category', 'country', 'goal', 'duration']]
    y = data['success']

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), ['goal', 'duration']),
            ('cat', OneHotEncoder(), ['category', 'country'])
        ])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    return X_train, X_test, y_train, y_test, preprocessor

# Model train
def train_model(X_train, y_train, preprocessor):
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', LogisticRegression())
    ])
    model.fit(X_train, y_train)
    return model

# ROC curve
def plot_roc_curve(y_test, y_prob):
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, label=f'ROC curve (AUC = {roc_auc:.2f})', color='blue')
    plt.plot([0, 1], [0, 1], 'k--', color='gray')
    plt.xlabel('Taux de Faux Positifs')
    plt.ylabel('Taux de Vrai Positive')
    plt.title('Courbe ROC')
    plt.legend(loc='lower right')
    st.pyplot(plt)

# Confusion matrix
def plot_confusion_matrix(y_test, y_pred):
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Failed', 'Success'], yticklabels=['Failed', 'Success'])
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Matrice de confusion')
    st.pyplot(plt)

# Show prediction
def prediction(data):
    data["success"] = np.where(data["state"] == "successful", 1, 0)

    st.title("Kickstarter Success Prediction")
    st.write("Cette application estime la probabilité de succès d’un projet Kickstarter en se basant sur des facteurs tels que la catégorie du projet, la durée de la campagne, l’objectif financier fixé et le pays de lancement..")

    X_train, X_test, y_train, y_test, preprocessor = preprocess_data(data)
    model = train_model(X_train, y_train, preprocessor)

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    st.subheader("Métriques du modèle")
    report = classification_report(y_test, y_pred, output_dict=True)
    st.write(pd.DataFrame(report).transpose())

    st.subheader("Visualisations")
    st.write("### Courbe ROC")
    plot_roc_curve(y_test, y_prob)

    st.write("### Matrice de confusion")
    plot_confusion_matrix(y_test, y_pred)

    st.write("### Importance des caractéristiques")
    coefficients = model.named_steps['classifier'].coef_[0]
    feature_names = model.named_steps['preprocessor'].get_feature_names_out()
    coef_df = pd.DataFrame({'Feature': feature_names, 'Coefficient': coefficients})
    coef_df = coef_df.sort_values(by='Coefficient', ascending=False)
    st.bar_chart(coef_df.set_index('Feature'))


