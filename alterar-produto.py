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