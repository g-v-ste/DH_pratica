fig, ax = plt.subplots(3,6, figsize=(25,12))
sns.set(font_scale = 1)
for i in range(len(house_prices.columns)):
     sns.violinplot(house_prices.iloc[:,i], ax=ax[i//6,i%6])
plt.show()