"""
LumiCity - simulacao simples de iluminacao publica.
Projeto academico: valores estimados, nao sao projeto executivo.
Execute na raiz do repositorio:
    python simulacao/simulacao.py
"""

POSTES = 15
HORAS_POR_NOITE = 12
DIAS_POR_MES = 30

# Premissas de potencia; perdas de 18 W do reator sao hipoteticas.
POTENCIA_SODIO_W = 168
POTENCIA_LED_W = 80

# Premissas solares provisórias, a validar com dados locais e fichas técnicas.
PAINEL_WP = 400
HSP = 4.3
FATOR_DESEMPENHO = 0.67

# Bateria de referência por poste.
BATERIA_V = 25.6
BATERIA_AH = 60
PROFUNDIDADE_DESCARGA = 0.80
EFICIENCIA_BATERIA = 0.90


def consumo_mensal_kwh(potencia_w):
    return potencia_w * HORAS_POR_NOITE * DIAS_POR_MES * POSTES / 1000


def geracao_solar_mensal_kwh():
    geracao_por_poste_dia = (PAINEL_WP / 1000) * HSP * FATOR_DESEMPENHO
    return geracao_por_poste_dia * DIAS_POR_MES * POSTES


def autonomia_bateria_horas():
    capacidade_nominal_kwh = BATERIA_V * BATERIA_AH / 1000
    energia_util_kwh = capacidade_nominal_kwh * PROFUNDIDADE_DESCARGA * EFICIENCIA_BATERIA
    return energia_util_kwh / (POTENCIA_LED_W / 1000)


def main():
    sodio = consumo_mensal_kwh(POTENCIA_SODIO_W)
    led = consumo_mensal_kwh(POTENCIA_LED_W)
    economia = sodio - led
    percentual = economia / sodio * 100
    geracao = geracao_solar_mensal_kwh()
    demanda_solar = led
    autonomia = autonomia_bateria_horas()

    print("LumiCity - resultados estimados")
    print(f"Postes analisados: {POSTES}")
    print(f"Consumo vapor de sodio: {sodio:.1f} kWh/mes")
    print(f"Consumo LED conectado a rede: {led:.1f} kWh/mes")
    print(f"Economia LED vs. sodio: {economia:.1f} kWh/mes ({percentual:.1f}%)")
    print(f"Demanda mensal das luminarias solares: {demanda_solar:.1f} kWh/mes")
    print(f"Geracao solar mensal estimada: {geracao:.1f} kWh/mes")
    print(f"Autonomia teorica da bateria: {autonomia:.1f} horas")

    print("\nATENCAO:")
    print("- A demanda solar nao e consumo da rede eletrica.")
    print("- A comparacao mensal nao garante autonomia em dias nublados.")
    print("- HSP, fator de desempenho e componentes precisam ser validados.")
    print("- Potencias nao comprovam equivalencia luminotecnica.")


if __name__ == "__main__":
    main()
