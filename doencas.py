# Base de conhecimento: doenças e seus sintomas
# Contém uma lista de doenças e os sintomas associados,  
# que é um dicionário onde as chaves são nomes de doenças
#  (como "Covid") e os valores são listas de sintomas associados a cada doença.

base_conhecimento = {
    "Covid": ["tosse", "falta de ar", "dor ao engolir"],
    "Pneumonia": ["febre alta", "tosse persistente", "dor no peito", "sudorese"],
    "Gripe H1N1": ["calafrios", "congestão nasal", "dores musculares", "tosse intensa"]
}

# Define a função diagnosticar, que recebe uma lista de sintomas fornecida pelo usuário (sintomas_usuario) como entrada.

def diagnosticar(sintomas_usuario):
    resultados = {} # Cria um dicionário vazio chamado resultados. Ele será usado para armazenar o número de sintomas correspondentes encontrados para cada doença.
    for doenca, sintomas in base_conhecimento.items(): # loop que percorre a base de conhecimento
        # Calcula a quantidade de sintomas correspondentes
        sintomas_correspondentes = set(sintomas_usuario).intersection(sintomas)
        resultados[doenca] = len(sintomas_correspondentes) # Armazena no dicionário resultados o número de sintomas correspondentes
    
    # Verifica qual doença tem o maior número de sintomas correspondentes com a função max
    doenca_diagnosticada = max(resultados, key=resultados.get) 
    
    if resultados[doenca_diagnosticada] > 0:
        return f"Possível diagnóstico: {doenca_diagnosticada} ({resultados[doenca_diagnosticada]} sintomas correspondentes)."
    else:
        return "Nenhuma doença correspondente foi encontrada para os sintomas fornecidos."

# Solicita os sintomas do usuário
print("Informe seus sintomas separados por vírgula:")
sintomas_usuario = input().lower().split(", ")
diagnostico = diagnosticar(sintomas_usuario) # Chama a função diagnosticar, passando a lista de sintomas 
# fornecida pelo usuário como argumento. Armazena o resultado na variável diagnostico

# Exibe o diagnóstico
print(diagnostico)

