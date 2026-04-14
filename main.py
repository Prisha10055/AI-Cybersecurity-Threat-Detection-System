import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns

print("🚀 PROGRAM STARTED")

# Load dataset
df = pd.read_csv("data/dataset.csv")

print("✅ Dataset Loaded")
print(df.head())

# Encode categorical columns
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].astype('category').cat.codes

print("✅ Data Preprocessed")

# Split data
X = df.drop("label", axis=1)
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print("✅ Data Split Done")

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

print("✅ Model Trained")

# Predict
predictions = model.predict(X_test)

print("✅ Predictions Done")

# Evaluate
print("\n🎯 Accuracy:", accuracy_score(y_test, predictions))
print("\n📊 Report:\n", classification_report(y_test, predictions))

# Confusion matrix
cm = confusion_matrix(y_test, predictions)
sns.heatmap(cm, annot=True)
plt.title("Confusion Matrix")
plt.show()

# ALERT SYSTEM
print("\n🚨 ALERTS:")
for i, pred in enumerate(predictions):
    if pred == 1:
        print(f"⚠️ Threat detected at test index {i}")