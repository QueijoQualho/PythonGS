estabelecimentos_exemplo = [
    {
        "Nome": "Hospital A",
        "Endereço": "Rua 1, 123",
        "Número": "123",
        "Bairro": "Centro",
        "Município": "São Paulo",
        "Estado": "SP",
        "CEP": "12345-678",
        "Telefone": "(11) 1234-5678",
        "Email": "hospitala@example.com",
    },
    {
        "Nome": "Clínica B",
        "Endereço": "Av. 2, 456",
        "Número": "456",
        "Bairro": "Bela Vista",
        "Município": "Campinas",
        "Estado": "AM",
        "CEP": "98765-432",
        "Telefone": "(11) 9876-5432",
        "Email": "clinicab@example.com",
    }
]

""" Valida se o input de estado do usuario é valido """
def validar_estado(estado):
    return estado.upper() in ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR",
                               "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]

""" Exibe a interface do menu para o usuario """
def exibir_menu_principal():
    print("\n=== Menu Health Spotter === \n"
          + "1. Buscar Serviços de Saúde Próximos \n"
          + "2. Adicionar Estabelecimento \n" 
          + "3. Remover Estabelecimento \n"
          + "4. Atualizar Estabelecimento \n"
          + "5. Sair")

""" Faz a busca dentro do Json para ver se tem algum objeto/estabelecimento
localizado no estado e municipio dado pelo user """

def buscar_estabelecimentos():
    estado = input("Digite a sigla do estado (ex: SP): ").upper()

    if not validar_estado(estado):
        print("Sigla de estado inválida.")
        return

    municipio = input("Digite o nome do município: ")

    resultados = [estabelecimento for estabelecimento in estabelecimentos_exemplo
                  if estabelecimento["Município"].lower() == municipio.lower()]

    if resultados:
        print("\nResultados encontrados:")
        for estabelecimento in resultados:
            print("\n---")
            for chave, valor in estabelecimento.items():
                print(f"{chave}: {valor}")
    else:
        print(f"Nenhum estabelecimento encontrado em {municipio}, {estado}.")

""" Adiciona um novo objeto/estabelecimento dentro do Json """
def adicionar_estabelecimento():
    novo_estabelecimento = {}
    for key in estabelecimentos_exemplo[0].keys():
        if key != "Estado":
            valor = input(f"Digite o(a) {key.lower()}: ")
            novo_estabelecimento[key] = valor
    novo_estabelecimento["Estado"] = input("Digite a sigla do estado: ")
    estabelecimentos_exemplo.append(novo_estabelecimento)
    print("Estabelecimento adicionado com sucesso!")

""" Remove o objeto/estabelecimento dentro do Json """
def remover_estabelecimento():
    nome = str(input("Qual o nome do estabeleciemento: "))

    for i in estabelecimentos_exemplo:
        if nome.lower() == i["Nome"].lower():
            estabelecimentos_exemplo.remove(i)
            print(f"Estabelecimento {nome} removido com sucesso.")
            return

    print(f"Estabelecimento {nome} não encontrado.")

""" Atualiza os dados de um estabelecimento solicitado """
def atualizar_estabelecimento():
    nome = input("Digite o nome do estabelecimento que deseja atualizar: ")

    for estabelecimento in estabelecimentos_exemplo:
        if nome.lower() == estabelecimento["Nome"].lower():
            print(f"Encontrado: {estabelecimento['Nome']}")
            campo = input("Digite o campo que deseja atualizar: ")
            if campo in estabelecimento:
                valor = input(f"Digite o novo valor para {campo}: ")
                estabelecimento[campo] = valor
                print(f"{campo} atualizado para {valor}")
                return
            else:
                print("Campo inválido.")
                return

    print(f"Estabelecimento {nome} não encontrado.")

def main():
    while True:
        exibir_menu_principal()
        try:
            opcao = input("Digite o número da opção desejada: ")
            if opcao == "1":
                buscar_estabelecimentos()
            elif opcao == "2":
                adicionar_estabelecimento()
            elif opcao == "3":
                remover_estabelecimento()
            elif opcao == "4":
                atualizar_estabelecimento()
            elif opcao == "5":
                print("Saindo do programa. Até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except KeyboardInterrupt:
            print("\nSaindo do programa. Até logo!")
            break

""" Roda o programa """
if __name__ == "__main__":
    main()
