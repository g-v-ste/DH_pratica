# Irei analisar com mais detalhe a distribuição dos dados, em especial o efeito do preço e o aspecto geográfico. A informação geográfica de determinado item é uma composição de duas variáveis (lat e long) que, isoladamente é difícil fazer sentido.
def normal(df, col, threshold=0.05):
    try:
        zscore, p_value = stats.normaltest(df[col])
        if p_value < threshold:
            result = 'not_normal'
        else:
            result = 'normal'
    except:
        zscore = p_value = np.nan
        result = 'not_applicable'
    return result

def outliers_count_IQR(df, col):
    try:
        if len(df[col].unique())>2: # if para eliminar features binárias
            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)
            iqr_range = q3 - q1
            lower = q1 - 1.5*iqr_range
            upper = q3 + 1.5*iqr_range
            out_low = df[df[col] < lower].count()[0]
            out_up = df[df[col] > upper].count()[0]
            outliers = out_low + out_up
            outliers_perc = round(outliers / df.shape[0],2)
        else:
            outliers = np.nan
            outliers_perc = np.nan
    except:
        outliers = np.nan
        outliers_perc = np.nan
    return outliers, outliers_perc

def EDA_morestats(df):
    eda_df = {}
    eda_df['Amount_NaN'] = df.isnull().sum()
    eda_df['%_NaN'] = df.isnull().mean().round(2)
    eda_df['DType'] = df.dtypes
    eda_df['Amount_Data'] = df.count()
    
    # Outro ponto para ser verificado, porque para criar a coluna com a quantidade de valores unicos por coluna
    # Não utilizei a função df.unique() 
    colunas = df.columns.tolist()
    
        
    eda_df['Amount_Unique'] = pd.Series(map(lambda x: len(df[x].unique().tolist()), colunas), index=colunas)
    
    eda_df['Mean'] = df.mean().round(3)
    eda_df['Min'] = df.min()
    eda_df['Max'] = df.max()
    eda_df['STD'] = df.std().round(3)
    eda_df['Normality'] = pd.Series(map(lambda x: normal(df, x), colunas), index=colunas)
    eda_df['Amount_Outliers'] = pd.Series(map(lambda x: outliers_count_IQR(df, x)[0], colunas), index=colunas)
    eda_df['%_Outliers'] = pd.Series(map(lambda x: outliers_count_IQR(df, x)[1], colunas), index=colunas)
    df = pd.DataFrame(eda_df)
    return df.loc[colunas,:]

## ----------------------------- ##
## ---- dividir celula aqui ---- ##
## ----------------------------- ##
EDA_morestats(house_prices)

## ----------------------------- ##
## ---- dividir celula aqui ---- ##
## ----------------------------- ##
plt.figure(figsize=(15,10))
sns.scatterplot(x=house_prices.longitude, y=house_prices.latitude);
plt.show()

## ----------------------------- ##
## ---- dividir celula aqui ---- ##
## ----------------------------- ##
plt.figure(figsize=(15,10))
sns.scatterplot(x=house_prices.longitude, y=house_prices.latitude, hue=house_prices.price.tolist());
plt.show()

## ----------------------------- ##
## ---- dividir celula aqui ---- ##
## ----------------------------- ##
# Como a variável preço tem uma cauda longa a direita, a visualização da distribuição dos preços no mapa fica ruim.
# Vamos aplicar log para redristribuir. Essa transformação irá afetar diretamente o seu modelo. Ele irá passar a prever o log do preço. Para que a saída da sua previsão seja compreendida de forma monetária como os dados de entrada, você deverá fazer a transformação inversa (exp).
# Essa transformação, na prática, introduz uma não lineariedade ao seu modelo e às relações entre as variáveis. Ou seja, as variáveis que influenciam o preço da casa irão influenciar em escala exponencial (para cada variação unitária em X, Y variará 10). 
plt.figure(figsize=(20,5))
plt.subplot(121)
plt.hist(house_prices.price)
plt.subplot(122)
plt.hist(np.log(house_prices.price))
plt.show()

## ----------------------------- ##
## ---- dividir celula aqui ---- ##
## ----------------------------- ##
fig, ax = plt.subplots(1,2,figsize=(20,10))

sns.scatterplot(x=house_prices.longitude, y=house_prices.latitude, hue=house_prices.price.tolist(), ax=ax[0])
sns.scatterplot(x=house_prices.longitude, y=house_prices.latitude, hue=np.log(house_prices.price.tolist()), ax=ax[1])
plt.show()

## ----------------------------- ##
## ---- dividir celula aqui ---- ##
## ----------------------------- ##
house_prices['price_log'] = np.log(house_prices.price)
house_prices['price_log']

## ----------------------------- ##
## ---- dividir celula aqui ---- ##
## ----------------------------- ##
# Geograficamente falando, parece haver outliers. Regiões distantes com baixo volume de casos (ex.: long > -121.6 ou lat < ~47.25)
long_thrs = -121.6
lat_thrs = 47.25
house_prices_selected = house_prices.loc[(house_prices.longitude < long_thrs) & (house_prices.latitude > lat_thrs) ,:] # tirando dos dados uma região onde tem poucos dados
print("Outliers dropped:", house_prices.shape[0] - house_prices_selected.shape[0])
print("Outliers %:", (house_prices.shape[0] - house_prices_selected.shape[0])/house_prices.shape[0])

## ----------------------------- ##
## ---- dividir celula aqui ---- ##
## ----------------------------- ##
fig, ax = plt.subplots(1,2,figsize=(20,10))
sns.scatterplot(x=house_prices.longitude, y=house_prices.latitude, hue=np.log(house_prices.price.tolist()), ax=ax[0])
sns.scatterplot(x=house_prices_selected.longitude, y=house_prices_selected.latitude, hue=np.log(house_prices_selected.price.tolist()), ax=ax[1])
plt.show()