import numpy as np

def gerar_dados_sinteticos(df_original):
    np.random.seed(42)
    n = len(df_original)

    df_original['porosidade_pct'] = np.clip(np.random.normal(18, 4, n), 8, 28)
    df_original['espessura_zona_prod_m'] = np.random.uniform(5, 60, n)
    df_original['pressao_reservatorio_psi'] = np.random.lognormal(mean=8, sigma=0.6, size=n)
    df_original['pressao_reservatorio_psi'] = np.clip(df_original['pressao_reservatorio_psi'], 100, 5000)
    df_original['saturacao_oleo_pct'] = np.random.uniform(30, 85, n)

    litologias = ['Arenito', 'Folhelho', 'Calcário', 'Conglomerado']
    probs = [0.6, 0.25, 0.1, 0.05]
    df_original['litologia'] = np.random.choice(litologias, size=n, p=probs)

    df_original['produtividade_inicial_bpd'] = (
        0.8 * df_original['porosidade_pct'] +
        1.2 * df_original['espessura_zona_prod_m'] +
        0.015 * df_original['pressao_reservatorio_psi'] +
        np.random.normal(0, 20, n)
    )

    df_original['produtividade_inicial_bpd'] = df_original['produtividade_inicial_bpd'].clip(lower=50)
    return df_original
