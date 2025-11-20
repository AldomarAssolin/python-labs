
def busca_binaria_com_passos(lista, item):
    passos = []
    baixo = 0
    alto = len(lista) - 1
    iteracao = 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            passos.append({
                "iteração": iteracao,
                "baixo": baixo,
                "alto": alto,
                "meio": meio,
                "chute": chute,
                "decisão": "encontrado ✅"
            })
            return meio, passos

        if chute > item:
            passos.append({
                "iteração": iteracao,
                "baixo": baixo,
                "alto": alto,
                "meio": meio,
                "chute": chute,
                "decisão": "chute > item → vai para esquerda"
            })
            alto = meio - 1
        else:
            passos.append({
                "iteração": iteracao,
                "baixo": baixo,
                "alto": alto,
                "meio": meio,
                "chute": chute,
                "decisão": "chute < item → vai para direita"
            })
            baixo = meio + 1

        iteracao += 1

    # só chega aqui se não encontrar
    return None, passos
