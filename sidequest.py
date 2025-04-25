import pandas as pd
import matplotlib.pyplot as plt


base_dados = pd.read_csv("Sidequest-Dados\Cópia de Base_despadronizada - Base_Corrigida.csv")

base_dados['sexo'] = base_dados['sexo'].str.strip().str.lower()

map_sexo = {
    'm': 'Masculino', 'masc': 'Masculino', 'masculino': 'Masculino',
    'f': 'Feminino', 'fem': 'Feminino', 'feminino': 'Feminino'
}

base_dados['sexo'] = base_dados['sexo'].map(map_sexo)


base_dados['nota_matematica'] = base_dados['nota_matematica'].astype(str).str.replace(',', '.').astype(float)
base_dados['nota_portugues'] = base_dados['nota_portugues'].astype(str).str.replace(',', '.').astype(float)
base_dados['frequencia'] = base_dados['frequencia'].astype(str).str.replace(',', '.').astype(float)
base_dados['media'] = (base_dados['nota_matematica'] + base_dados['nota_portugues'] + (base_dados['frequencia'] / 10)) / 3



def verificar_aprovacao(media):
    if media >= 7:
        return 'Sim'
    else:
        return 'Não'
    
base_dados['aprovado'] = base_dados['media'].apply(verificar_aprovacao)


aprov_counts = base_dados['aprovado'].value_counts()
aprov_perc = base_dados['aprovado'].value_counts(normalize=True) * 100

print("Distribuição de Aprovação:")
print(aprov_counts.to_string(index=True, header=False))
print(aprov_perc.round(1).to_string(index=True, header=False))

plt.figure(figsize=(6,6))
plt.pie(aprov_counts, labels=aprov_counts.index, autopct='%1.1f%%', colors=['green', 'red'])
plt.title('Distribuição de Aprovação')
plt.savefig('grafico_aprovacao_pizza.png')
plt.show()

sexo_counts = base_dados['sexo'].value_counts()

print("\nDistribuição por Sexo:")
print(sexo_counts.to_string(index=True, header=False))


plt.figure(figsize=(4,4))
plt.bar(sexo_counts.index, sexo_counts.values, color=['blue', 'pink'])
plt.title('Distribuição por Sexo')
plt.xlabel('Sexo')
plt.ylabel('Quantidade')
plt.savefig('grafico_sexo.png')
plt.show()

top5_medias = base_dados[['nome', 'media']].sort_values(by='media', ascending=False).head(5)

print("\nTop 5 Melhores Médias:")
print(top5_medias)


plt.figure(figsize=(8,3))
plt.barh(top5_medias['nome'], top5_medias['media'], color='orange')
plt.xlabel('Média')
plt.title('Top 5 Melhores Médias')
plt.gca().invert_yaxis()
plt.savefig('grafico_top5_medias.png')
plt.show()


top5_freq = base_dados[['nome', 'frequencia']].sort_values(by='frequencia', ascending=False).head(5)

print("\nTop 5 Frequência:")
print(top5_freq)

plt.figure(figsize=(8,3))
plt.barh(top5_freq['nome'], top5_freq['frequencia'], color='purple')
plt.xlabel('Frequência')
plt.title('Top 5 Frequência')
plt.gca().invert_yaxis()
plt.savefig('grafico_top5_frequencia.png')
plt.show()




base_dados['nota_matematica'] = base_dados['nota_matematica'].astype(str).str.replace('.', ',')
base_dados['nota_portugues'] = base_dados['nota_portugues'].astype(str).str.replace('.', ',')
base_dados['media'] = base_dados['media'].astype(str).str.replace('.', ',')
base_dados['frequencia'] = base_dados['frequencia'].astype(str).str.replace('.', ',')


print(base_dados)