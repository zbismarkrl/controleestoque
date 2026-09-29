# PRD: Sistema Simples de Controle de Estoque

**Versão:** 1.0  
**Data:** 29/09/2026  
**Status:** Rascunho inicial

## 1. Visão geral

Criar um sistema web simples para registrar produtos, acompanhar entradas e saídas e consultar o saldo atual do estoque. O sistema deve ajudar pequenos comércios e equipes a reduzir erros de anotação e identificar rapidamente produtos com estoque baixo.

## 2. Problema

O controle feito em papel ou planilhas pode ficar desatualizado, dificultar a consulta dos saldos e não deixar claro quem registrou cada movimentação. Isso pode causar falta de produtos, compras desnecessárias e divergências no inventário.

## 3. Objetivo

Permitir que uma pessoa responsável consulte e atualize o estoque em um único lugar, com histórico das movimentações e aviso visual para itens que estejam no limite mínimo.

### Indicadores de sucesso

- O responsável consegue cadastrar um produto e registrar uma movimentação sem ajuda técnica.
- O saldo exibido é atualizado após cada entrada ou saída.
- Produtos abaixo do estoque mínimo ficam fáceis de identificar.
- Cada movimentação mantém data, tipo, quantidade e usuário responsável.
- A consulta da lista de produtos leva poucos segundos em um catálogo pequeno ou médio.

## 4. Usuários

### Usuário administrador

Responsável por cadastrar produtos, corrigir informações e consultar o estoque.

### Usuário operador

Responsável por registrar entradas e saídas. No MVP, administrador e operador podem ter as mesmas permissões para manter o sistema simples. A separação de permissões fica para uma versão futura.

## 5. Escopo do MVP

### Incluído

- Acesso por login.
- Cadastro, edição, consulta e inativação de produtos.
- Registro de entrada e saída de estoque.
- Histórico de movimentações.
- Pesquisa e filtros básicos.
- Indicação de estoque baixo.
- Painel inicial com números resumidos.
- Exportação simples da lista de produtos para CSV.

### Fora do escopo inicial

- Controle de vendas, pedidos e fornecedores.
- Emissão de nota fiscal.
- Integração com leitor de código de barras.
- Vários depósitos ou filiais.
- Aplicativo móvel nativo.
- Compras automáticas.
- Previsão de demanda.
- Integração com sistemas contábeis.

## 6. Requisitos funcionais

| ID | Requisito |
|---|---|
| RF-01 | O sistema deve permitir que o usuário entre com e-mail e senha. |
| RF-02 | O sistema deve permitir cadastrar produto com nome, código/SKU, categoria, unidade, quantidade inicial, estoque mínimo e descrição opcional. |
| RF-03 | O sistema deve impedir o cadastro de dois produtos ativos com o mesmo código/SKU. |
| RF-04 | O sistema deve permitir editar os dados de um produto. Alterar o cadastro não deve apagar seu histórico. |
| RF-05 | O sistema deve permitir inativar um produto sem excluir suas movimentações anteriores. |
| RF-06 | O sistema deve permitir registrar entrada ou saída, informando produto, quantidade e observação opcional. |
| RF-07 | Ao registrar entrada, o sistema deve somar a quantidade ao saldo atual. |
| RF-08 | Ao registrar saída, o sistema deve subtrair a quantidade do saldo atual e impedir saldo negativo. |
| RF-09 | Cada movimentação deve guardar produto, tipo, quantidade, saldo após a operação, data e hora, usuário e observação. |
| RF-10 | O sistema deve mostrar uma lista de produtos com nome, código, categoria, saldo e situação do estoque. |
| RF-11 | O usuário deve poder pesquisar por nome ou código e filtrar por categoria e situação do estoque. |
| RF-12 | O sistema deve sinalizar produtos cujo saldo seja menor ou igual ao estoque mínimo. |
| RF-13 | O sistema deve mostrar um resumo com total de produtos ativos, itens com estoque baixo e movimentações recentes. |
| RF-14 | O sistema deve permitir consultar o histórico de movimentações de um produto, com filtro por período e tipo. |
| RF-15 | O sistema deve permitir exportar a lista filtrada de produtos para CSV. |

## 7. Regras de negócio

- O saldo inicial deve ser zero ou maior.
- A quantidade de uma movimentação deve ser um número positivo.
- Saídas que deixem o saldo negativo devem ser recusadas, com uma mensagem clara.
- O saldo atual deve ser calculado a partir do saldo inicial e das movimentações registradas, ou mantido atualizado de forma consistente.
- Movimentações confirmadas não devem ser apagadas diretamente. Para corrigir um lançamento, o usuário registra uma movimentação inversa com justificativa.
- Produtos inativos não aparecem na lista padrão de produtos disponíveis para novas movimentações, mas continuam acessíveis no histórico.
- O alerta de estoque baixo ocorre quando **saldo atual ≤ estoque mínimo**.
- O código/SKU pode ser opcional, mas, quando informado, deve ser único entre os produtos ativos.

## 8. Requisitos não funcionais

- Interface em português brasileiro, responsiva para computador e celular.
- Operações comuns devem responder em até 2 segundos em condições normais, considerando até 5 mil produtos.
- Senhas devem ser armazenadas com hash seguro, nunca em texto puro.
- O acesso às telas e aos dados deve exigir autenticação.
- O sistema deve validar os dados no navegador e no servidor.
- A aplicação deve informar erros de forma clara e preservar os dados já preenchidos quando possível.
- Deve haver rotina de backup do banco de dados definida para o ambiente de produção.

## 9. Fluxos principais

### Cadastrar produto

1. Usuário abre **Produtos** e seleciona **Novo produto**.
2. Preenche nome, código, categoria, unidade e estoque mínimo.
3. Informa o saldo inicial, se necessário.
4. Salva e recebe confirmação ou indicação dos campos inválidos.

### Registrar entrada ou saída

1. Usuário seleciona **Nova movimentação**.
2. Escolhe o produto e o tipo: entrada ou saída.
3. Informa a quantidade e, se quiser, uma observação.
4. Confirma a operação.
5. O sistema atualiza o saldo e registra a movimentação no histórico.

### Consultar estoque baixo

1. Usuário abre o painel ou a lista de produtos.
2. Seleciona o filtro **Estoque baixo**.
3. Visualiza produtos com saldo igual ou inferior ao mínimo definido.

## 10. Critérios de aceitação

- Um produto cadastrado aparece na lista com os dados e saldo informados.
- Uma entrada de 10 unidades em um produto com saldo 5 resulta em saldo 15.
- Uma saída de 3 unidades em um produto com saldo 5 resulta em saldo 2.
- Uma saída maior que o saldo disponível não altera o estoque e apresenta mensagem explicativa.
- Cada operação confirmada aparece no histórico com usuário e data/hora.
- Um produto com saldo igual ao estoque mínimo recebe a indicação de estoque baixo.
- Um produto inativado deixa de aparecer nas opções de novas movimentações, mas seu histórico continua disponível.
- O CSV exportado contém os produtos correspondentes aos filtros aplicados.

## 11. Telas previstas

1. **Login:** e-mail e senha.
2. **Painel:** indicadores e movimentações recentes.
3. **Produtos:** tabela, pesquisa, filtros e botão para cadastrar.
4. **Cadastro/edição de produto:** formulário com dados do item.
5. **Movimentação:** formulário para entrada ou saída.
6. **Detalhes do produto:** saldo, estoque mínimo e histórico.
7. **Usuários:** criação e gerenciamento básico de acessos, se necessário para a implantação.

## 12. Dados principais

### Produto

- ID
- Nome
- Código/SKU
- Categoria
- Unidade de medida
- Descrição
- Estoque mínimo
- Saldo atual
- Situação: ativo ou inativo
- Data de criação e última atualização

### Movimentação

- ID
- Produto
- Tipo: entrada ou saída
- Quantidade
- Saldo após a movimentação
- Observação
- Usuário responsável
- Data e hora

### Usuário

- ID
- Nome
- E-mail
- Senha armazenada com hash
- Situação: ativo ou inativo

## 13. Premissas e decisões em aberto

Este PRD considera uma única empresa e um único local de estoque, com poucos usuários e sem integração com vendas. Antes do desenvolvimento, confirmar:

- Se o código/SKU será obrigatório.
- Quais categorias e unidades de medida serão oferecidas.
- Se o sistema será usado por uma ou várias pessoas ao mesmo tempo.
- Onde a aplicação será hospedada e qual será a política de backup.
- Se será necessário importar produtos de uma planilha existente.
