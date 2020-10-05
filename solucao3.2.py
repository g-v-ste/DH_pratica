# lendo o arquivo e armazenando os dados em um DataFrame a partir do DropBox
%time house_prices = pd.read_csv("./data/house_pricing_test.csv",delimiter=',')
house_prices.head()