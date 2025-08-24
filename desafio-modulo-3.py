# Lista de Compras Simples

def exibir_cabecalho():
    print("\n" + "=" * 40)
    print("       LISTA DE COMPRAS SIMPLES")
    print("=" * 40 + "\n")

def exibir_produtos(produtos):
    if not produtos:
        print("\n[INFO] Nenhum produto na lista.\n")
        return
    print("\nProdutos na lista:")
    print("-" * 40)
    for produto in produtos:
        print(f"ID: {produto['id']} | Nome: {produto['nome']} | "
              f"Qtd: {produto['quantidade']} {produto['unidade']} | "
              f"Descrição: {produto['descricao']}")
    print("-" * 40)

def exibir_menu():
    print("\nMenu:")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Pesquisar produtos")
    print("4 - Sair")

def obter_opcao():
    while True:
        opcao = input("Escolha uma opção: ")
        if opcao in ["1", "2", "3", "4"]:
            return opcao
        print("[ERRO] Opção inválida. Tente novamente.")

def obter_unidade():
    unidades = ["Quilograma", "Grama", "Litro", "Mililitro", "Unidade", "Metro", "Centímetro"]
    print("\nEscolha a unidade de medida:")
    for i, unidade in enumerate(unidades, start=1):
        print(f"{i} - {unidade}")
    while True:
        escolha = input("Digite o número da unidade: ")
        if escolha.isdigit() and 1 <= int(escolha) <= len(unidades):
            return unidades[int(escolha) - 1]
        print("[ERRO] Unidade inválida. Tente novamente.")

def adicionar_produto(produtos, ultimo_id):
    nome = input("Nome do produto: ").strip()
    if not nome:
        print("[ERRO] O nome não pode ser vazio.")
        return ultimo_id
    unidade = obter_unidade()
    while True:
        try:
            quantidade = float(input("Quantidade: "))
            break
        except ValueError:
            print("[ERRO] Digite um número válido para a quantidade.")
    descricao = input("Descrição do produto: ").strip()
    novo_id = ultimo_id + 1
    produtos.append({
        "id": novo_id,
        "nome": nome,
        "unidade": unidade,
        "quantidade": quantidade,
        "descricao": descricao
    })
    print(f"[SUCESSO] Produto '{nome}' adicionado com ID {novo_id}.")
    return novo_id

def remover_produto(produtos):
    if not produtos:
        print("[INFO] Não há produtos para remover.")
        return
    try:
        id_remover = int(input("Digite o ID do produto a remover: "))
    except ValueError:
        print("[ERRO] ID inválido.")
        return
    for produto in produtos:
        if produto["id"] == id_remover:
            produtos.remove(produto)
            print(f"[SUCESSO] Produto ID {id_remover} removido.")
            return
    print("[ERRO] Produto não encontrado.")

def pesquisar_produtos(produtos):
    termo = input("Digite o nome ou parte do nome para pesquisar: ").strip().lower()
    if not termo:
        print("[ERRO] O termo de pesquisa não pode ser vazio.")
        return
    encontrados = [p for p in produtos if termo in p["nome"].lower()]
    if encontrados:
        print(f"\n[INFO] {len(encontrados)} produto(s) encontrado(s):")
        for p in encontrados:
            print(f"ID: {p['id']} | Nome: {p['nome']} | Qtd: {p['quantidade']} {p['unidade']}")
    else:
        print("[INFO] Nenhum produto encontrado.")

def main():
    exibir_cabecalho()
    produtos = []
    ultimo_id = 0
    while True:
        exibir_produtos(produtos)
        exibir_menu()
        opcao = obter_opcao()
        if opcao == "1":
            ultimo_id = adicionar_produto(produtos, ultimo_id)
        elif opcao == "2":
            remover_produto(produtos)
        elif opcao == "3":
            pesquisar_produtos(produtos)
        elif opcao == "4":
            print("\n[INFO] Programa encerrado. Até logo!\n")
            break

if __name__ == "__main__":
    main()
