from google.colab import files
uploaded = files.upload()

import pandas as pd
from transformers import pipeline, AutoTokenizer, AutoModelForTokenClassification
from collections import Counter
import matplotlib.pyplot as plt
import seaborn as sns

# Ler o CSV
df = pd.read_csv("articles.csv")
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Filtrar
df_filtered = df[
    (df['category'].str.lower() == 'mercado') &
    (df['date'] >= '2015-01-01') &
    (df['date'] <= '2015-03-31')
]

# Modelo NER
model_name = "monilouise/ner_pt_br"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)
ner = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

# Contagem
org_counter = Counter()
for text in df_filtered['text'].dropna():
    ents = ner(text)
    for ent in ents:
        if ent['entity_group'] == 'ORG':
            org_counter[ent['word'].strip()] += 1

# Top organizações
org_df = pd.DataFrame(org_counter.items(), columns=['Organização', 'Frequência'])
org_df = org_df.sort_values(by='Frequência', ascending=False).head(10)

# Visualização
plt.figure(figsize=(10,6))
sns.barplot(data=org_df, x='Frequência', y='Organização', palette='viridis')
plt.title('Top 10 Organizações mais mencionadas - Mercado (1º Trim. 2015)')
plt.tight_layout()
plt.savefig("grafico.png")
plt.show()
