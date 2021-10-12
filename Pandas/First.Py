import pandas as pd

venda = {

    'Data':['15/02/2021', '16/02/2021'],
    'valor' : [500, 300],
    'Produto' : ['feijao', 'arroz'],
    'qtde' : [50, 70]

}

vendas_df =pd.DataFrame(venda)

print(vendas_df)
