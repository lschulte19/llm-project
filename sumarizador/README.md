# 📰 Sumarizador de Artigos com LLM, LangChain e Streamlit

## 📌 Visão Geral

Este é um aplicativo simples e funcional que permite ao usuário colar o texto de um artigo e obter um **resumo conciso** com auxílio de **modelos de linguagem (LLMs)** via **OpenAI API**.

O projeto utiliza:
- ✅ [Streamlit](https://streamlit.io/) para a interface interativa
- ✅ [LangChain](https://www.langchain.com/) para orquestração do prompt e integração com o LLM
- ✅ [OpenAI API](https://platform.openai.com/) como motor de geração de texto

---

## 🏗️ Arquitetura

Usuário (navegador)
│
Streamlit
│
LangChain
│
OpenAI LLM API (GPT-3.5 Turbo Instruct)
│
Resumo gerado


### 🔧 Componentes

- **Interface Web**: Criada com Streamlit para facilitar entrada e visualização
- **LLMChain**: Usado para combinar prompt com LLM e gerar a resposta
- **PromptTemplate**: Define como o artigo será enviado ao modelo
- **OpenAI LLM**: Modelo utilizado (`gpt-3.5-turbo-instruct`) com baixa temperatura para resumos mais objetivos

---

## 🚀 Como usar

### 1. Clone o projeto

```bash
git clone https://github.com/seu-usuario/sumarizador-artigos.git
cd sumarizador-artigos

2. Instale as dependências

pip install -r requirements.txt

Ou manualmente:

pip install streamlit openai langchain

3. Execute o aplicativo

streamlit run app.py

4. Insira sua API Key da OpenAI

    A chave é solicitada na barra lateral

    Pode ser obtida em: https://platform.openai.com/account/api-keys

5. Cole o texto do artigo e clique em "Gerar Resumo"
📦 Estrutura do Projeto

sumarizador-artigos/
│
├── app.py               # Código principal do app
├── README.md            # Documentação
├── requirements.txt     # Dependências (opcional)
