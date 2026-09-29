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