faturamento_por_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total_mensal = sum(faturamento_por_estados.values())

percentuais_por_estados = {}

for estado, faturamento in faturamento_por_estados.items():
    percentual = (faturamento/ total_mensal) * 100
    percentuais_por_estados[estado] = percentual
    
print("Percentual de representação de cada estado no valor total mensal da distribuidora: ")
for estado, percentual in percentuais_por_estados.items():
    print(f"{estado}: {percentual: .2f}%")
