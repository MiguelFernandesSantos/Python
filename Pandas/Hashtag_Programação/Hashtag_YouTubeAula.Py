# Importa o pandas:
import pandas as pd 

# Le um arquivo em Excel da mesma pasta:
vendas_df = pd.read_excel("Vendas.xlsx")

# Mostra de forma mais estilizada a tabela:
display(vendas_df)

# Mostra as 10 primeiras linhas:
display(vendas_df.head(10)) 

# Mostra a quantidade de linhas e colunas:
display(vendas_df.shape)

# Recebe uma serie, ou seja uma coluna ou linha, nesse caso colunas:
produtos = vendas_df[['Produto', 'ID Loja']] 

# Loc = linha / coluna

# Mostra da primeira ate a quarta linha:
display(vendas_df.loc[1:4])

# Pegar linhas de uma determinada condição:
display(vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping'])

# Pegar varias linhas e colunas usando o loc:
vendas_norte_df = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping', ['ID Loja', 'Produto', 'Quantidade']]
display(vendas_norte_df)

# Pegar um valor especifico:
display(vendas_df.loc[1, 'Produto'])

# Criar uma coluna a partir de uma coluna que existe:
vendas_df['Comissao'] = vendas_df['Valor Final'] * 0.05
display(vendas_df)

# Criar uma coluna com um valor padrao
vendas_df.loc[: , 'Imposto'] = 0
display(vendas_df)

# Pegar vendas de dezembro
vendas_dezembro_df = pd.read_excel('Vendas - Dez.xlsx')
display(vendas_dezembro_df)

# Coloca o conteudo de uma em outra, entretando se tiver colunas diferentes ele coloca como null:
# Poderia colocar as colunas iguais nas 2 antes de juntar, ou juntar e depois colocar as colunas
vendas_df = vendas_df.append(vendas_dezembro_df)
display(vendas_df)

# 1 é igual coluna e 0 igual coluna
vendas_df = vendas_df.drop('Imposto', axis = 1) 
display(vendas_df)

# Deletar linhas e colunas completamente vazias:
# Exclui valores vazios apenas exclui linhas totalmente vazias, e se passar o eixo 1 exclui colunas
vendas_df = vendas_df.dropna(how = 'all') 
display(vendas_df)

# Deletar linha que possuem pelo menos 1 valor vazio:
# Exclui linhas que possuem pelo menos 1 valor vazio.
vendas_df = vendas_df.dropna() 
display(vendas_df)

# Preencher valores vazios:
# Preencher com a media:
vendas_df['Comissao'] = vendas_df['Comissao'].fillna(vendas_df['Comissao'].mean()) 
display(vendas_df)

# Preencher com o ultimo valor:
# Preencher cada valor vazio com o valor de cima
vendas_df = vendas_df.ffill() 

# Conta a quantidade de vezes que determinados valores aparecem e retorna uma nova serie com os valores:
transacoes_loja =vendas_df['ID Loja'].value_counts()
display(transacoes_loja)

# Agrupa as informaçoes:
faturamento_produto = vendas_df.groupby('Produto').sum()
display(faturamento_produto)

# Agrupa as informaçoes de determinadas colunas:
faturamento_produto = vendas_df[['Produto', 'Valor Final']].groupby('Produto').sum()
display(faturamento_produto)

# Mesclar:
gerentes_df = pd.read_excel('Gerentes.xlsx')
vendas_df = vendas_df.merge(gerentes_df)
display(vendas_df)