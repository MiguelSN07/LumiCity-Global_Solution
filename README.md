# LumiCity — Simulação Energética

Projeto acadêmico de análise de eficiência energética na iluminação pública, considerando uma rua hipotética em São Paulo com **15 postes**.

> **Importante:** todos os resultados são estimativas acadêmicas baseadas nas premissas descritas abaixo. Não são medições reais nem um projeto executivo.

## Arquivos
- `simulacao/simulacao.py`: calcula consumo, economia, geração solar estimada e autonomia teórica da bateria.
- `dados/dados.csv`: dados usados na comparação.
- `imagens/diagrama.png`: diagrama conceitual do sistema solar independente.

## Como executar
É necessário ter Python 3 instalado. Na pasta principal do repositório, execute:

```bash
python simulacao/simulacao.py
```

Não é necessário instalar bibliotecas externas.

## Problema e objetivo
O estudo considera uma via pública hipotética em São Paulo. O problema analisado é o consumo de energia associado à iluminação pública e a possibilidade de reduzi-lo com luminárias mais eficientes e, no cenário solar, com geração fotovoltaica local.

O objetivo é comparar três alternativas para os mesmos 15 pontos de iluminação:
1. Lâmpadas de vapor de sódio;
2. Luminárias LED conectadas à rede elétrica;
3. Luminárias LED com sistema solar independente em cada poste.

## Premissas da simulação
- Quantidade: 15 postes;
- Funcionamento: 12 horas por noite;
- Período de referência: 30 dias por mês;
- Vapor de sódio: 168 W por ponto, sendo 150 W da lâmpada + 18 W **assumidos** para perdas do reator;
- LED: 80 W por ponto;
- Sistema solar: painel de 400 Wp por poste;
- Recurso solar: 4,3 horas de sol pico por dia (**premissa provisória; precisa ser confirmada para o local e plano do painel**);
- Fator global de desempenho: 0,67 (**premissa de simulação, não valor medido nem validado para um equipamento específico**);
- Bateria de referência: 25,6 V e 60 Ah;
- Profundidade de descarga considerada: 80%;
- Eficiência global da bateria considerada: 90%.

A potência de 168 W para o cenário de sódio não deve ser tratada como especificação universal: os 18 W adicionais são uma hipótese de cálculo e precisam ser substituídos por dados de placa ou ficha técnica do conjunto lâmpada/reator escolhido.

## Fórmulas e resultados
Consumo mensal:

`Energia (kWh/mês) = potência (W) × horas/dia × dias/mês × quantidade ÷ 1.000`

- Vapor de sódio: 168 × 12 × 30 × 15 ÷ 1.000 = **907,2 kWh/mês**.
- LED conectado à rede: 80 × 12 × 30 × 15 ÷ 1.000 = **432 kWh/mês**.
- Economia estimada do LED em relação ao cenário de sódio: **475,2 kWh/mês**, ou **52,4%**.

Geração fotovoltaica simplificada:

`Geração (kWh/mês) = potência do painel (kWp) × HSP (h/dia) × fator de desempenho × dias × quantidade`

- Por poste: 0,4 × 4,3 × 0,67 × 30 = **34,57 kWh/mês**.
- Para 15 postes: aproximadamente **518,6 kWh/mês**.

Demanda das luminárias solares:
- 0,08 kW × 12 h × 30 dias × 15 postes = **432 kWh/mês**.

**Atenção:** os 432 kWh/mês no cenário solar representam a demanda das luminárias, não consumo da rede. A comparação entre geração e demanda é apenas mensal e agregada; não comprova autonomia diária nem garante atendimento durante sequências de dias nublados. O sistema precisa de dimensionamento horário e análise de armazenamento.

Autonomia teórica da bateria:
- Capacidade nominal: 25,6 V × 60 Ah = **1,536 kWh**.
- Energia útil estimada: 1,536 × 0,80 × 0,90 = **1,106 kWh**.
- Autonomia teórica a 80 W: 1,106 ÷ 0,08 = **13,8 horas**.

A autonomia é uma aproximação simplificada e não considera todas as perdas do controlador, cabos, temperatura, envelhecimento, limites de descarga do fabricante ou variação da carga.

## Interpretação
Sob as premissas adotadas, o LED conectado à rede consome cerca de 52,4% menos energia que o cenário de sódio. O LED solar tem a mesma demanda elétrica das luminárias LED, mas a energia é prevista para vir de painéis e baterias individuais. A geração média mensal estimada supera a demanda mensal estimada, mas isso, isoladamente, não prova que o sistema independente funcionará durante todo o ano.

Onde a rede elétrica já existe, o LED conectado à rede pode ser a alternativa mais simples. O sistema solar independente pode reduzir a dependência da rede, mas exige mais componentes, investimento inicial, espaço, manutenção e verificação de autonomia.

## Indicadores para o dashboard
- Consumo mensal estimado do cenário de sódio: 907,2 kWh/mês;
- Consumo mensal estimado do LED conectado à rede: 432 kWh/mês;
- Economia estimada de energia: 475,2 kWh/mês (52,4%);
- Demanda mensal das luminárias solares: 432 kWh/mês;
- Geração solar mensal estimada: 518,6 kWh/mês;
- Autonomia teórica da bateria de referência: 13,8 horas.

## Limitações e validações pendentes
1. **Iluminação equivalente:** 168 W e 80 W não garantem o mesmo nível de iluminação. É necessário projeto luminotécnico conforme os requisitos aplicáveis da ABNT NBR 5101:2024, considerando classe da via, iluminância/luminância, uniformidade e distribuição fotométrica.
2. **Perdas do reator:** validar os 18 W assumidos com ficha técnica do conjunto de 150 W escolhido.
3. **Recurso solar:** consultar o Atlas Brasileiro de Energia Solar do INPE para a localização específica, orientação e inclinação do painel. A HSP de 4,3 h/dia permanece provisória até essa consulta.
4. **Fator de desempenho:** o valor 0,67 é uma hipótese global da simulação. Deve ser revisto com dados do equipamento, instalação, sombreamento, temperatura, sujeira, cabos e controlador.
5. **Bateria e controlador:** verificar corrente, tensão, compatibilidade, BMS, limites de descarga, perdas e autonomia para dias de baixa geração.
6. **Estrutura e segurança:** verificar fixação, peso, vento, proteção elétrica, aterramento e manutenção.
7. **Custos e emissões:** não foram calculados custos de aquisição/instalação/manutenção, tarifa efetiva nem emissões evitadas. Não apresentar esses valores sem fontes e metodologia verificadas.

## Referências
- **INPE / LABREN.** Atlas Brasileiro de Energia Solar — 2ª edição. Dados e consulta de irradiação para o Estado de São Paulo. https://labren.ccst.inpe.br/atlas_2017_SP.html
- **INPE / LABREN.** Atlas Brasileiro de Energia Solar — informações sobre a base de dados e forma de citação. https://labren.ccst.inpe.br/atlas_2017.html
- **NREL.** PVWatts — System Losses. Explica categorias de perdas fotovoltaicas; não valida por si só o fator 0,67 usado nesta simulação. https://pvwatts.nlr.gov/docs/help_system_sysloss.php
- **EDP.** Especificação Técnica ES.DT.PDN.00147, versão 08, “Iluminação Pública — Acessórios” (25 set. 2023). Documento de acessórios de iluminação pública e referências normativas; não foi usado para afirmar um valor específico de perda de 18 W ou 22 W. https://www.edp.com.br/media/ueue3xtd/esdtpdn00147_v8.pdf
- **ABNT.** NBR 5101:2024 — Iluminação viária. Consultar a norma oficial para requisitos de projeto luminotécnico. https://www.abntcatalogo.com.br/

As fontes acima fundamentam o método e apontam onde validar as premissas. Os valores de 18 W, 80 W, 400 Wp, 4,3 HSP, 0,67, 25,6 V e 60 Ah permanecem hipóteses de cenário até serem confirmados por fichas técnicas ou dados locais.
