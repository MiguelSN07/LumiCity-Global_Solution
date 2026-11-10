"""
LumiCity - simulacao simples de iluminacao publica
Projeto academico: valores estimados, nao sao projeto executivo.
"""

POSTES = 15
HORAS_POR_NOITE = 12
DIAS_POR_MES = 30
POTENCIA_SODIO_W = 168  # lampada de 150 W + 18 W estimados de reator
POTENCIA_LED_W = 80
PAINEL_WP = 400
HSP = 4.3                 # horas de sol pico por dia (premissa)
FATOR_DESEMPENHO = 0.67
BATERIA_V = 25.6
BATERIA_AH = 60
PROFUNDIDADE_DESCARGA = 0.80
EFICIENCIA_BATERIA = 0.90


def consumo_mensal_kwh(potencia_w):
    return potencia_w * HORAS_POR_NOITE * DIAS_POR_MES * POSTES / 1000


def geracao_solar_mensal_kwh():
    por_poste_dia = (PAINEL_WP / 1000) * HSP * FATOR_DESEMPENHO
    return por_poste_dia * DIAS_POR_MES * POSTES


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

    print("LumiCity - resultados estimados")
    print(f"Postes analisados: {POSTES}")
    print(f"Consumo sodio: {sodio:.1f} kWh/mes")
    print(f"Consumo LED: {led:.1f} kWh/mes")
    print(f"Economia LED vs. sodio: {economia:.1f} kWh/mes ({percentual:.1f}%)")
    print(f"Demanda atendida pelo LED solar: {led:.1f} kWh/mes")
    print(f"Geracao solar estimada: {geracao:.1f} kWh/mes")
    print(f"Autonomia teorica da bateria: {autonomia_bateria_horas():.1f} horas")

    if geracao >= led:
        print("Resultado solar: geracao mensal estimada cobre a demanda mensal.")
    else:
        print("Resultado solar: geracao mensal estimada nao cobre toda a demanda.")

    print("\nObservacao: a media mensal nao garante autonomia em dias nublados.")
    print("Validar iluminancia, dimensionamento, sombreamento e normas antes de instalar.")


if __name__ == "__main__":
    main()
