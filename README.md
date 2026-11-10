# LumiCity — Simulação Energética

Projeto acadêmico de análise de eficiência energética na iluminação pública, considerando uma rua hipotética em São Paulo com **15 postes**.

## Arquivos
- `simulacao.py`: calcula consumo, economia, geração solar estimada e autonomia teórica da bateria.
- `dados/dados.csv`: dados usados na comparação.
- `imagens/diagrama-poste-solar.svg`: diagrama conceitual do sistema solar independente.

## Como executar
É necessário ter Python 3 instalado. No terminal, dentro da pasta do projeto:

```bash
python simulacao.py
```

Não é necessário instalar bibliotecas externas.

## Premissas da simulação
- 15 pontos de iluminação;
- funcionamento por 12 horas por noite e 30 dias por mês;
- vapor de sódio: 168 W por ponto (150 W da lâmpada + 18 W estimados de perdas do reator);
- LED: 80 W por ponto;
- sistema solar independente: painel de 400 Wp por poste;
- horas de sol pico: 4,3 h/dia e fator de desempenho de 0,67;
- bateria de referência: 25,6 V e 60 Ah, com profundidade de descarga de 80% e eficiência de 90%.

## Fórmula de consumo
`Energia (kWh) = Potência (W) × horas × dias × quantidade ÷ 1000`

## Resultados principais
- Sódio: **907,2 kWh/mês**.
- LED: **432 kWh/mês**.
- Economia do LED em relação ao sódio: **475,2 kWh/mês (52,4%)**.
- Geração solar estimada com as premissas adotadas: **518,6 kWh/mês** para os 15 painéis.

**Atenção:** no cenário solar, 432 kWh/mês é a demanda das lâmpadas, não consumo da rede elétrica. A geração mensal estimada não garante atendimento em todos os dias, especialmente em períodos nublados.

## Limitações
Os valores são estimativas acadêmicas, não um projeto executivo. Não foram dimensionados iluminação conforme a norma aplicável, estrutura dos postes, sombreamento, variação sazonal da irradiação, cabeamento, proteções, custos de instalação ou ciclo de vida das baterias. A equivalência de iluminação entre as lâmpadas de 168 W e 80 W precisa ser validada por projeto luminotécnico. As premissas devem ser verificadas antes de qualquer aplicação real.
