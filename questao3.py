import json
def calcular_estatisticas_faturamento(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        dados_faturamento = json.load(arquivo)
        
    dias_com_faturamento = [valor for valor in dados_faturamento.values() if valor > 0]
    
    menor_faturamento =  min(dias_com_faturamento)
    maior_faturamento = max(dias_com_faturamento)
    
    media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)
    
    dias_acima_da_media = sum(1 for valor in dias_com_faturamento if valor > media_mensal)
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media
    
caminho_arquivo = "desafio target 2\\faturamento_mensal.json"
menor, maior, acima_media = calcular_estatisticas_faturamento(caminho_arquivo)

print("Menor valor de faturamento:", menor)
print("Maior valor de faturamento:", maior)
print("Número de dias com faturamentos acima da média mensal:", acima_media)    
