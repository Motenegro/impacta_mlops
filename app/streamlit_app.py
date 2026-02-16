import joblib
import pickle
import pandas as pd
import streamlit as st
import mlflow
import mlflow.pyfunc

#import os
#mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI", "http://localhost:5000"))


@st.cache_resource
def load_model():
    model_uri = "models:/diamonds_price_model@champion"
    model = mlflow.pyfunc.load_model(model_uri)
    return model

@st.cache_resource
def load_model_local():
    model_path = "models/model.pkl"
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

def main():
    st.title("Previsão de preço de diamantes")

    st.write("Modelo treinado com o dataset `diamonds` do seaborn.")

    model = load_model_local()

    st.subheader("Informe as características do diamante")

    # campos básicos do dataset diamonds
    carat = st.number_input("carat", min_value=0.0, max_value=5.0, value=0.5, step=0.01)
    depth = st.number_input("depth", min_value=40.0, max_value=80.0, value=61.5, step=0.1)
    table = st.number_input("table", min_value=40.0, max_value=80.0, value=57.0, step=0.1)
    x = st.number_input("x (comprimento)", min_value=0.0, max_value=15.0, value=5.0, step=0.1)
    y = st.number_input("y (largura)", min_value=0.0, max_value=15.0, value=5.0, step=0.1)
    z = st.number_input("z (altura)", min_value=0.0, max_value=15.0, value=3.0, step=0.1)

    cut = st.selectbox("cut", ["Fair", "Good", "Very Good", "Premium", "Ideal"])
    color = st.selectbox("color", ["D", "E", "F", "G", "H", "I", "J"])
    clarity = st.selectbox(
        "clarity",
        ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"],
    )

    if st.button("Prever preço"):
        data = pd.DataFrame(
            {
                "carat": [float(carat)],
                "depth": [float(depth)],
                "table": [float(table)],
                "x": [float(x)],
                "y": [float(y)],
                "z": [float(z)],
                "cut": [str(cut)],
                "color": [str(color)],
                "clarity": [str(clarity)],
            }
        )


        num_cols = ["carat", "depth", "table", "x", "y", "z"]
        data[num_cols] = data[num_cols].astype(float)

        cat_cols = ["cut", "color", "clarity"]
        data[cat_cols] = data[cat_cols].astype(str)

        EXPECTED_COLUMNS = [
            "carat",
            "depth",
            "table",
            "x",
            "y",
            "z",
            "cut",
            "color",
            "clarity",
        ]

        data = data[EXPECTED_COLUMNS]

        prediction = model.predict(data)[0]

        st.subheader("Resultado")
        st.write(f"Preço estimado: **${prediction:,.2f}**")

if __name__ == "__main__":
    main()
