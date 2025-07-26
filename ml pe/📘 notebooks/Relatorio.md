Relatório Técnico – Pipeline de Modelagem de Produtividade de Poços com Dados Sintéticos
   
   Objetivo Geral

Desenvolver e testar um pipeline completo para análise e predição da produtividade de poços de petróleo utilizando dados sintéticos baseados em parâmetros técnicos realistas. A estrutura foi pensada para ser modular, com foco em transferência futura para dados reais (ANP ou privados).
  
  Etapas Técnicas Executadas

1. Ingestão e Pré-processamento

    Leitura de base pública em .csv com codificação latin-1 e separador ;.

    Padronização de colunas e parsing de coordenadas geográficas de formato DMS para decimal.

    Estrutura de DataFrame unificada contendo metadados de cada poço (nome, bacia, operador, localização, ambiente).

2. Geração de Atributos Sintéticos

    Implementação de um gerador técnico de dados sintéticos baseado em distribuições realistas para:

        Porosidade (%)

        Espessura da zona produtiva (m)

        Saturação de óleo (%)

        Pressão de reservatório (psi)

        Litologia (categórico)

    Fórmula proxy para produtividade_inicial_bpd combinando variáveis geológicas + ruído gaussiano.

3. Modelagem Preditiva Supervisionada

    Testes com modelos:

        Regressão Linear (baseline)

        LightGBM (modelo principal no momento)

    Divisão treino/teste 80/20 e one-hot encoding das variáveis categóricas.

    Resultado (LightGBM):

        RMSE ≈ 24.1

        R² ≈ 2.12%

        Interpretação: baixa capacidade preditiva esperada, dado o nível de ruído dos dados sintéticos. Serve como prova de conceito da arquitetura.

4. Simulação de Produção Temporal

    Para cada poço, gerada curva de produção mensal por 24 meses via modelo de declínio exponencial.

    Variabilidade aleatória no fator de declínio por poço (0.02 a 0.08).

    Curvas armazenadas com poco_id, data, bpd.

5. Forecasting com Prophet

    Aplicação de Prophet para prever 12 meses futuros por poço.

    Gráficos mostram declínio contínuo com tendência exponencial compatível com campos reais.

    Visualizações Criadas

    Mapas Interativos (Folium):

        Poços plotados com CircleMarkers georreferenciados.

        Tooltips com litologia e produtividade.

    Gráficos de Distribuição (Seaborn + Plotly):

        Histograma e boxplot da produtividade.

        Boxplot interativo por litologia (Plotly Express).

    Gráfico com Animação Temporal:

        [Tentado] Gráfico estilo Gapminder com bolhas por produção no tempo (pendente por erro de sessão).

      Principais Conclusões Técnicas

    O pipeline é funcional, replicável e pode ser facilmente adaptado a dados reais.

    A modularidade permite inserir novos modelos, clusters ou visualizações com baixo custo técnico.

    A qualidade do modelo preditivo é limitada pela aleatoriedade dos dados sintéticos — comportamento esperado.

    A integração de dados espaciais com litologia e produtividade já permite análises visuais georreferenciadas.

