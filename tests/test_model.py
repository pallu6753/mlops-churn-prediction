import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score


def test_model_f1():

    df = pd.read_csv("data/churn.csv")

    X = df.drop("churn", axis=1)
    y = df["churn"]

    preprocessor = ColumnTransformer(
        [
            (
                "categorical",
                OneHotEncoder(handle_unknown="ignore"),
                ["contract_type", "internet_service", "tech_support"]
            )
        ],
        remainder="passthrough"
    )

    model = Pipeline([
        ("preprocessing", preprocessor),
        ("model", RandomForestClassifier(
            n_estimators=100,
            max_depth=5,
            random_state=42
        ))
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    f1 = f1_score(y_test, predictions, zero_division=0)

    print(f"F1 Score: {f1:.4f}")

    assert f1 >= 0.80