estabelecimentos_sp = [
    {
        "Nome": "Hospital A",
        "Endereço": "Rua 1, 123",
        "Número": "123",
        "Bairro": "Centro",
        "CEP": "12345-678",
        "Telefone": "(11) 1234-5678",
        "Email": "hospitala@example.com",
        "Município": "São Paulo"
    },
    {
        "Nome": "Clínica B",
        "Endereço": "Av. 2, 456",
        "Número": "456",
        "Bairro": "Bela Vista",
        "CEP": "98765-432",
        "Telefone": "(11) 9876-5432",
        "Email": "clinicab@example.com",
        "Município": "Campinas"
    },
]
def validar_estado(estado):
    estados_validos = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR",
                       "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]

    return estado.upper() in estados_validos

def exibir_menu_principal():
    print("\n=== Menu Health Spotter ===")
    print("1. Buscar Serviços de Saúde Próximos")
    print("2. Sair")

def buscar_estabelecimentos():
    estado = input("Digite a sigla do estado (ex: SP): ")

    if not validar_estado(estado):
        print("Sigla de estado inválida.")
        return

    municipio = input("Digite o nome do município: ")

    resultados = [estabelecimento for estabelecimento in estabelecimentos_sp
                  if estabelecimento["Município"].lower() == municipio.lower()]

    if resultados:
        print("\nResultados encontrados:")
        for estabelecimento in resultados:
            print("\n---")
            for chave, valor in estabelecimento.items():
                print(f"{chave}: {valor}")
    else:
        print(f"Nenhum estabelecimento encontrado em {municipio}, {estado}.")

def main():
    while True:
        exibir_menu_principal()
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            buscar_estabelecimentos()
        elif opcao == "2":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
