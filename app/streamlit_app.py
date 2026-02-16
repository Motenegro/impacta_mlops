import joblib
import pickle
import pandas as pd
import streamlit as st
import mlflow
import mlflow.pyfunc

# --- CONFIGURAÇÃO DA PÁGINA (Deve ser a primeira linha de comando Streamlit) ---
st.set_page_config(
    page_title="Diamond Predictor | José Montenegro Brandão Filho",
    page_icon="💎",
    layout="centered"
)

# --- ESTILIZAÇÃO CUSTOMIZADA (CSS) ---
# Aqui você muda cores de fundo, fontes e estilos de botões
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007BFF;
        color: white;
    }
    .sidebar .sidebar-content {
        background-image: linear-gradient(#2e7bcf,#2e7bcf);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

@st.cache_resource
def load_model_local():
    model_path = "models/model.pkl"
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

def main():
    # --- BARRA LATERAL (ASSINATURA E LOGO) ---
    with st.sidebar:
        # st.image("caminho/para/seu_logo.png", width=150) # Descomente para usar um logo local
        st.title("💡 Diamond Insights")
        st.markdown("---")
        st.write("### Desenvolvido por: José Montenegro Brandão Filho")
        st.info("** José Montenegro Brandão Filho **") # Substitua pelo seu nome
        st.write("Projeto de Previsão de Preços utilizando Machine Learning.")
        
    # --- CORPO PRINCIPAL ---
    st.title("💎 Previsão de Preço de Diamantes")
    st.markdown("Este aplicativo utiliza IA para estimar o valor de mercado de diamantes.")
    
    # Banner ou Imagem de Destaque
    # st.image("https://images.unsplash.com/photo-1551028150-64b9f398f678?w=800", use_column_width=True)

    model = load_model_local()

    st.subheader("📋 Informe as características")
    
    # Organizando em colunas para um visual mais limpo
    col1, col2 = st.columns(2)
    
    with col1:
        carat = st.number_input("Carat (Quilates)", min_value=0.0, max_value=5.0, value=0.5, step=0.01)
        depth = st.number_input("Depth %", min_value=40.0, max_value=80.0, value=61.5, step=0.1)
        table = st.number_input("Table %", min_value=40.0, max_value=80.0, value=57.0, step=0.1)
        cut = st.selectbox("Corte (Cut)", ["Ideal", "Premium", "Very Good", "Good", "Fair"])

    with col2:
        x = st.number_input("Comprimento (x)", min_value=0.0, max_value=15.0, value=5.0, step=0.1)
        y = st.number_input("Largura (y)", min_value=0.0, max_value=15.0, value=5.0, step=0.1)
        z = st.number_input("Altura (z)", min_value=0.0, max_value=15.0, value=3.0, step=0.1)
        color = st.selectbox("Cor (Color)", ["D", "E", "F", "G", "H", "I", "J"])

    clarity = st.selectbox("Clareza (Clarity)", ["IF", "VVS1", "VVS2", "VS1", "VS2", "SI1", "SI2", "I1"])

    if st.button("Calcular Preço Estimado"):
        data = pd.DataFrame({
            "carat": [float(carat)], "depth": [float(depth)], "table": [float(table)],
            "x": [float(x)], "y": [float(y)], "z": [float(z)],
            "cut": [str(cut)], "color": [str(color)], "clarity": [str(clarity)],
        })

        # Predição
        prediction = model.predict(data)[0]

        # Resultado com destaque visual
        st.markdown("---")
        st.balloons() # Efeito visual de comemoração
        st.success(f"### Preço estimado: **US$ {prediction:,.2f}**")

if __name__ == "__main__":
    main()