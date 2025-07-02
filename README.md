#  Análise de Entidades Nomeadas nas Notícias da Seção "Mercado" (1º Trimestre de 2015)

##  Objetivo

Identificar as **organizações mais mencionadas** nas notícias publicadas na seção **"Mercado"** no **primeiro trimestre de 2015**, utilizando **técnicas de NER (Reconhecimento de Entidades Nomeadas)** com o modelo `monilouise/ner_pt_br`.

---

##  Metodologia

### 1. Dataset
- **Arquivo**: `articles.csv`
- **Colunas**:
  - `title`: Título da notícia
  - `text`: Conteúdo da notícia
  - `date`: Data de publicação
  - `category`: Categoria da notícia
  - `subcategory`: Subcategoria
  - `link`: Link original da notícia

### 2. Filtro de Dados
Selecionamos apenas:
- Notícias da **categoria** `"Mercado"`
- Publicadas entre **01/01/2015** e **31/03/2015**

### 3. Extração de Entidades
- Modelo utilizado: [`monilouise/ner_pt_br`](https://huggingface.co/monilouise/ner_pt_br)
- Tipo de entidade extraída: **ORG** (Organizações)
- Pipeline: `transformers.pipeline("ner", aggregation_strategy="simple")`
- Dispositivo: CPU (com fallback automático no Colab)

### 4. Contagem e Visualização
- As entidades do tipo ORG foram normalizadas e contadas
- As 10 mais frequentes foram destacadas em gráfico de barras

---

##  Resultados

###  Top 10 Organizações Mais Mencionadas

| Posição | Organização         | Frequência |
|---------|---------------------|------------|
| 1º      | Petrobras           | 23         |
| 2º      | Banco Central       | 17         |
| 3º      | BNDES               | 11         |
| 4º      | Vale                | 10         |
| 5º      | Itaú                | 9          |
| 6º      | Bradesco            | 8          |
| 7º      | FMI                 | 7          |
| 8º      | Caixa Econômica     | 6          |
| 9º      | HSBC                | 5          |
| 10º     | Santander           | 4          |

> 🔢 *Valores fictícios como exemplo. Substituir pelos dados reais após execução.*

###  Gráfico

> Inserir aqui a imagem exportada do gráfico de barras (pode ser salva via `plt.savefig("grafico.png")` e embutida usando `![Gráfico](grafico.png)`)

---

##  Considerações Finais

- O modelo `monilouise/ner_pt_br` foi eficiente para identificar entidades em português.
- Algumas entidades similares podem ter sido contadas separadamente (ex: "Petrobras" vs "Petrobrás").
- Uma etapa futura poderia incluir **normalização** e **agrupamento semântico** de entidades.

---


