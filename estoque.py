def cadastrarProduto():
    nome = input("Digite o nome do produto: ")
    codigo = int(input("Digite o código do produto: "))
    quantidade = int(input("Digite a quantidade em estoque: "))
    preco = float(input("Digite o preço do produto: "))

    produto = {
        'nome': nome,
        'codigo': codigo,
        'quantidade': quantidade,
        'preco': preco
    }

    produtos.append(produto)
    
    def adicionarEstoque():
    codigo = int(input("Digite o código do produto: "))

    for produto in produtos:
        if produto['codigo'] == codigo:
            quantidade = int(input("Digite a quantidade que deseja adicionar: "))

            produto['quantidade'] += quantidade

            print("Estoque atualizado!")
            return

    print("Produto não encontrado!")