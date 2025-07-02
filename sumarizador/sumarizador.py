import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

# --- Configurar chave da OpenAI ---
openai_api_key = st.sidebar.text_input("Sua OpenAI API Key", type="password")

# --- Título do app ---
st.title("Sumarizador de Artigos com LLM")

# --- Campo para inserir o artigo ---
article = st.text_area("Cole aqui o texto do artigo que deseja resumir:", height=300)

# --- Processamento ---
if st.button("Gerar Resumo") and article and openai_api_key:
    os.environ["OPENAI_API_KEY"] = openai_api_key

    # Prompt + LangChain
    prompt = PromptTemplate(
        input_variables=["article"],
        template="Resuma o seguinte artigo de forma concisa e clara:\n\n{article}"
    )
    llm = OpenAI(temperature=0.3, model_name="gpt-3.5-turbo-instruct")
    chain = LLMChain(llm=llm, prompt=prompt)

    with st.spinner("Gerando resumo..."):
        summary = chain.run(article)

    st.subheader("Resumo Gerado:")
    st.success(summary)

elif st.button("Gerar Resumo", key="generate_summary") and not openai_api_key:
    st.warning("⚠️ Por favor, insira sua chave da OpenAI na barra lateral.")
