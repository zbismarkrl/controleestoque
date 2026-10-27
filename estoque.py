produtos = []

def cadastrarProduto():
    nome = input("Digite o nome do produto: ")

    if not nome.strip():
        print("O nome do produto não pode ficar vazio!")
        return

    try:
        codigo = int(input("Digite o código do produto: "))
        quantidade = int(input("Digite a quantidade em estoque: "))
        preco = float(input("Digite o preço do produto: "))
    except ValueError:
        print("Erro: digite valores numéricos válidos!")
        return

    for produto in produtos:
        if produto['codigo'] == codigo:
            print("Já existe um produto com esse código!")
            return

    if quantidade < 0:
        print("A quantidade não pode ser negativa!")
        return

    if preco < 0:
        print("O preço não pode ser negativo!")
        return

    produto = {
        'nome': nome,
        'codigo': codigo,
        'quantidade': quantidade,
        'preco': preco
    }

    produtos.append(produto)

    print("Produto cadastrado com sucesso!")

def adicionarEstoque():
    try:
        codigo = int(input("Digite o código do produto: "))
    except ValueError:
        print("Erro: digite um código numérico válido!")
        return

    for produto in produtos:
        if produto['codigo'] == codigo:
            try:
                quantidade = int(
                    input("Digite a quantidade que deseja adicionar: ")
                )
            except ValueError:
                print("Erro: digite uma quantidade válida!")
                return

            if quantidade <= 0:
                print("A quantidade deve ser maior que zero!")
                return

            produto['quantidade'] += quantidade

            print("Estoque atualizado com sucesso!")
            return

    print("Produto não encontrado!")

def retirarEstoque():
    try:
        codigo = int(input("Digite o código do produto: "))
    except ValueError:
        print("Erro: digite um código numérico válido!")
        return

    for produto in produtos:
        if produto['codigo'] == codigo:
            try:
                quantidade = int(
                    input("Digite a quantidade que deseja retirar: ")
                )
            except ValueError:
                print("Erro: digite uma quantidade válida!")
                return

            if quantidade <= 0:
                print("A quantidade deve ser maior que zero!")
                return

            if quantidade <= produto['quantidade']:
                produto['quantidade'] -= quantidade
                print("Estoque atualizado com sucesso!")
            else:
                print("Quantidade insuficiente em estoque!")

            return

    print("Produto não encontrado!")

def alterarProduto():
    try:
        codigo = int(input("Digite o código do produto: "))
    except ValueError:
        print("Erro: digite um código numérico válido!")
        return

    for produto in produtos:
        if produto['codigo'] == codigo:
            print("Produto encontrado!")
            print("Digite (1) para alterar o nome")
            print("Digite (2) para alterar o preço")
            print("Digite (3) para alterar os dois")

            try:
                op = int(input("Digite a opção desejada: "))
            except ValueError:
                print("Erro: digite uma opção válida!")
                return

            if op == 1:
                nome = input("Digite o novo nome: ")

                if not nome.strip():
                    print("O nome não pode ficar vazio!")
                    return

                produto['nome'] = nome

            elif op == 2:
                try:
                    preco = float(input("Digite o novo preço: "))
                except ValueError:
                    print("Erro: digite um preço válido!")
                    return

                if preco < 0:
                    print("O preço não pode ser negativo!")
                    return

                produto['preco'] = preco

            elif op == 3:
                nome = input("Digite o novo nome: ")

                if not nome.strip():
                    print("O nome não pode ficar vazio!")
                    return

                try:
                    preco = float(input("Digite o novo preço: "))
                except ValueError:
                    print("Erro: digite um preço válido!")
                    return

                if preco < 0:
                    print("O preço não pode ser negativo!")
                    return

                produto['nome'] = nome
                produto['preco'] = preco

            else:
                print("Opção inválida!")
                return

            print("Produto alterado com sucesso!")
            return

    print("Produto não encontrado!")

def mostrarEstoque():
    if not produtos:
        print("Nenhum produto cadastrado!")
        return

    print("\n===== ESTOQUE DE PRODUTOS =====")

    for produto in produtos:
        print("-------------------------")
        print("Nome:", produto['nome'])
        print("Código:", produto['codigo'])
        print("Quantidade:", produto['quantidade'])
        print("Preço: R$ {:.2f}".format(produto['preco']))

    print("-------------------------")

while True:
    print("\n===== SISTEMA DE CONTROLE DE ESTOQUE =====")
    print("1 - Cadastrar produto")
    print("2 - Adicionar estoque")
    print("3 - Retirar estoque")
    print("4 - Alterar produto")
    print("5 - Mostrar estoque")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrarProduto()

    elif opcao == "2":
        adicionarEstoque()

    elif opcao == "3":
        retirarEstoque()

    elif opcao == "4":
        alterarProduto()

    elif opcao == "5":
        mostrarEstoque()

    elif opcao == "6":
        print("Sistema encerrado!")
        break

    else:
        print("Opção inválida! Tente novamente.")