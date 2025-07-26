 GeoProdML – Pipeline de Modelagem de Produtividade de Poços com Dados Sintéticos

Projeto de ciência de dados voltado à simulação, predição e análise de produtividade de poços de petróleo, utilizando dados sintéticos gerados com base em parâmetros técnicos realistas. O objetivo é construir um pipeline modular e replicável, com potencial de adaptação para dados reais da ANP ou bases privadas.

 

 Objetivos

- Gerar uma base sintética realista de poços com variáveis geológicas e operacionais.
- Modelar a produtividade inicial com algoritmos supervisionados.
- Simular curvas de produção com modelos de declínio.
- Aplicar técnicas de forecasting para projeção futura de produção.
- Criar visualizações interativas e mapas de localização.

 Funcionalidades Implementadas

- Geração de variáveis geotécnicas sintéticas: porosidade, espessura, saturação de óleo, pressão, litologia.
- Cálculo da produtividade inicial com base em proxy técnico.
- Modelagem preditiva com Regressão Linear, Random Forest e LightGBM.
- Simulação de curvas mensais de produção por poço (declínio exponencial).
- Previsão de produção futura com Prophet.
- Visualização de métricas de regressão.
- Mapas interativos com Folium.
- Gráficos interativos com Plotly.

 Stack Utilizada

- Python 3.10+
- Bibliotecas principais:
  - `pandas`, `numpy`, `scikit-learn`, `xgboost`, `lightgbm`
  - `matplotlib`, `seaborn`, `plotly`
  - `geopandas`, `folium`
  - `prophet`, `statsmodels`, `keras`, `tensorflow`
  - `tqdm`, `jupyter`

