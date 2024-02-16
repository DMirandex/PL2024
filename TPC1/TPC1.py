class AnalisadorCSV:
    def __init__(self, file_path: str):
        with open(file_path) as f:
            linhas = f.readlines()

        dataset = [linha.replace('\n', '').split(',') for linha in linhas]
        # Remover cabeçalho
        header = dataset.pop(0)

        # Variáveis para as estatísticas
        self.modalidades = set()
        self.aptos = 0
        self.inaptos = 0
        self.idades = []

        # 0    1      2         3          4           5     6      7        8        9    10      11      12
        #_id,index,dataEMD,nome/primeiro,nome/último,idade,género,morada,modalidade,clube,email,federado,resultado
        for line in dataset:
            self.modalidades.add(line[8])

            # Verificando se o atleta é apto ou inapto
            if line[12] == 'true':
                self.aptos += 1
            else:
                self.inaptos += 1

            # Recolha das idades para a distribuição etária
            idade = int(line[5])  # Considerando idade mínima de 30 anos
            self.idades.append(idade)

        # Ordenando modalidades alfabeticamente
        self.modalidades_ordenadas = sorted(self.modalidades)

        # Criando distribuição de atletas por escalão etário
        self.idades.sort()
        self.escaloes_etarios = {}
        for idade in self.idades:
            # Encontrando o intervalo etário
            escalao_inicio = (idade // 5) * 5
            escalao_fim = escalao_inicio + 4
            escalao = f"[{escalao_inicio}-{escalao_fim}]"
            self.escaloes_etarios[escalao] = self.escaloes_etarios.get(escalao, 0) + 1

        # Removendo intervalos sem atletas
        self.escaloes_etarios = {k: v for k, v in self.escaloes_etarios.items() if v > 0}

    def mostrar_modalidades(self):
        print("Modalidades:", self.modalidades_ordenadas)

    def mostrar_percentagens(self):
        print("Percentagem de Aptos:", (self.aptos / (self.aptos + self.inaptos)) * 100)
        print("Percentagem de Inaptos:", (self.inaptos / (self.aptos + self.inaptos)) * 100)

    def mostrar_distribuicao_idade(self):
        print("Distribuição de Idade:", self.escaloes_etarios)


# Função para exibir o menu
def exibir_menu():
    print("Menu:")
    print("1. Lista ordenada alfabeticamente das modalidades desportivas")
    print("2. Percentagens de atletas aptos e inaptos para a prática desportiva")
    print("3. Distribuição de atletas por escalão etário")
    print("4. Sair")


# Exemplo de uso
if __name__ == "__main__":
    analise = AnalisadorCSV('emd.csv')
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            analise.mostrar_modalidades()
        elif opcao == "2":
            analise.mostrar_percentagens()
        elif opcao == "3":
            analise.mostrar_distribuicao_idade()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
