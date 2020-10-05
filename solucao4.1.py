- (20 min): Preprocessing (scalling e train/test)
- (10 min): Solução proposta
- (10 min): Feature selection (correlações)
- (05 min): Solução proposta
- (10 min): Regressão linear simples
- (05 min): Solução proposta
- (10 min): Intervalo
- (30 min): Regressão linear múltipla - teste de diferentes modelos 
- (15 min): Solução proposta
- (30 min): Análise dos resultados

## ----------------------------- ##
## ---- dividir celula aqui ---- ##
## ----------------------------- ##
## FEATURE SELECTION
Procure entender as relações existentes entre as variáveis, especialmente com a variável target. Verifique se existem relações lineares ou não lineares.
Como em todos os outros passos, essa etapa pode gerar novos insights que te farão voltar a etapas anteriores (por exemplo, construir uma nova feature). Lembrando que algumas features devem ser calculadas após a separação treino-teste. 
Obs.: a análise das relações entre as variáveis pode ser considerada também como parte do EDA.

## ----------------------------- ##
## ---- dividir celula aqui ---- ##
## ----------------------------- ##
%load solucao4.3.py
# resposta
# matriz de correlações
# análise das variáveis categóricas
- Testes T
- demonstrar a superposição das distribuições de preço de uma variável categórica
# conclusões: 
 - Variáveis com alta correlação entre si não são desejáveis no modelo, pois na hora da otimização o modelo terá que compensar os efeitos duplicados. Contudo, é possível criar alguma feature que capture a informação que deseja (ex.: prevendo a demanda por pneus, utilizar frota e consumo de gasolina por veículo ao invés de frota e consumo total de gasolina).
 - Scalling afetou a correlação?
 
%load solucao4.3adicional.py
# PPS

## ----------------------------- ##
## ---- dividir celula aqui ---- ##
## ----------------------------- ##
## PREPROCESSING
Desenvolva o pre-processamento adequado para realizar a modelagem. Dentre as opções que conhece, tente imaginar qual será mais adequada e porquê.

## ----------------------------- ##
## ---- dividir celula aqui ---- ##
## ----------------------------- ##
%load solucao4.2.py
# resposta

## ----------------------------- ##
## ---- dividir celula aqui ---- ##
## ----------------------------- ##
## MODELO SIMPLES
Novamente, pense em um caminho de trabalho: 
- Priorize as informações que irá testar em seu modelo
- Procure começar com relações mais simples

## ----------------------------- ##
## ---- dividir celula aqui ---- ##
## ----------------------------- ##
%load solucao4.5.py
# resposta

## ----------------------------- ##
## ---- dividir celula aqui ---- ##
## ----------------------------- ##
## MODELO MULTIVARIAVEL

## ----------------------------- ##
## ---- dividir celula aqui ---- ##
## ----------------------------- ##
%load solucao4.6.py
# resposta

## ----------------------------- ##
## ---- dividir celula aqui ---- ##
## ----------------------------- ##
## ANALISE DOS RESULTADOS

## ----------------------------- ##
## ---- dividir celula aqui ---- ##
## ----------------------------- ##
%load solucao4.7.py
# resposta
