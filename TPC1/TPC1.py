class AnalisadorCSV:
    def __init__(self, file_path: str):
        with open(file_path) as f:
            linhas = f.readlines()

        dataset = [linha.replace('\n', '').split(',') for linha in linhas]
        # Remover cabeçalho
        header = dataset.pop(0)

        # Variáveis para as estatísticas
        modalidades = set()
        aptos = 0
        inaptos = 0
        idades = []

        # 0    1      2         3          4           5     6      7        8        9    10      11      12
        #_id,index,dataEMD,nome/primeiro,nome/último,idade,género,morada,modalidade,clube,email,federado,resultado
        for line in dataset:
            modalidades.add(line[8])

            # Verificando se o atleta é apto ou inapto
            if line[12] == 'true':
                aptos += 1
            else:
                inaptos += 1

            # Recolha das idades para a distribuição etária
            idade = int(line[5])  # Considerando idade mínima de 30 anos
            idades.append(idade)

        # Calculando percentagens de aptos e inaptos
        total_atletas = len(dataset)
        percent_aptos = (aptos / total_atletas) * 100
        percent_inaptos = (inaptos / total_atletas) * 100

        # Ordenando modalidades alfabeticamente
        modalidades_ordenadas = sorted(modalidades)

        # Criando distribuição de atletas por escalão etário
        idades.sort()
        escaloes = {}
        for idade in idades:
            if idade >= 30:
                escalao = (idade // 5) * 5
                escaloes[escalao] = escaloes.get(escalao, 0) + 1

        self.modalidades_ordenadas = modalidades_ordenadas
        self.percent_aptos = percent_aptos
        self.percent_inaptos = percent_inaptos
        self.escaloes_etarios = escaloes

# Exemplo de uso
analise = AnalisadorCSV('emd.csv')
print("Modalidades:", analise.modalidades_ordenadas)
print("Percentagem de Aptos:", analise.percent_aptos)
print("Percentagem de Inaptos:", analise.percent_inaptos)
print("Distribuição de Idade:", analise.escaloes_etarios)