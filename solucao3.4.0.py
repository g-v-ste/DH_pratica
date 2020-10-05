## ----------------------------- ##
## ---- mudar para markdown ---- ##
## ----------------------------- ##

- Renovation_date na verdade é um ano. Como não há informação sobre dia ou mês, será mantido como numérico. 
- Contudo, o valor '0' significa que nunca houve reforma. Tratando-se de um atributo que deveria aumentar o valor do imóvel quanto menor fosse, os '0' não são consistentes com os outros valores. Acredito que deveria substituir pelo ano em que foi construído
- Há 5 colunas categóricas com valores numéricos:
  - Ordenadas: condition, beds, bathrooms
  - Não ordenadas: is_waterfront, zip
- Não está claro em nenhum lugar a definição de neighbor para as variáveis 14 e 15. Talvez seja equivalente a zip. A testar.
- Existem 22 diferentes valores para banheiros. Os valores assumem frações para representar lavabos. Será possível separar em duas variáveis: qtd de banheiros e qtd de lavabos?
- O dataset possui lat e long! Certamente plotaremos um mapa.
- Com um mapa poderemos verificar inúmeros aspectos (ex.: o que significa waterfront - mar, rio, lago, etc)
- Na descrição do dataset diz que size_house já inclui size_basement. Algumas possíveis novas  features: area_ex_basement, basement_ratio, area_per_floor, baths_bed_ratio
- As variáveis estão em escalas bem distintas. Algum tipo de scaling será necessário
- Outliers: 
    - Algumas distribuições estão bastante assimétricas. São outliers ou existe uma relação não linear dessas variáveis com as outras? Para as séries com assimetria a direita (cauda longa para valores maiores), como por exemplo price, podemos experimentar a utilização do log para corrigir. 
    - Poderemos também excluir se houver indícios de que é um erro ou que é um tipo de imóvel muito diferente (ex.: imóvel sem banheiro ou sem quarto, imóvel com 100% da área em basement).