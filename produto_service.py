import decimal

from produto import Produto
from produto_repository import ProdutoRepository


class ProdutoService:
    def __init__(self, repository: ProdutoRepository | str | None = None):
        if isinstance(repository, str):
            self._repository = ProdutoRepository(repository)
        elif repository is not None:
            self._repository = repository
        else:
            self._repository = ProdutoRepository("dados/produtos.csv")

def cadastrar_produto(repository: ProdutoRepository) -> None:
    while True:
        try:
            id_produto = int(input("ID do produto: "))
            nome = input("Nome do produto: ").strip()
            quantidade = int(input("Quantidade: "))
            preco = decimal.Decimal(input("Preço: ").replace(",", "."))
            categoria = input("Categoria: ").strip()

            if repository.buscar_por_id(id_produto) is not None:
                raise ValueError(f"Já existe um produto com o id {id_produto}.")

            produto = Produto(
                id=id_produto,
                nome=nome,
                quantidade=quantidade,
                preco=preco,
                categoria=categoria,
            )
            repository.salvar(produto)
            print("Produto cadastrado com sucesso.")
        except (ValueError, decimal.InvalidOperation) as erro:
            print(f"Não foi possível cadastrar o produto: {erro}")

        continuar = input("Deseja cadastrar um novo produto? (s/n): ").strip().lower()
        if continuar != "s":
            break

def listar_produtos(repository: ProdutoRepository) -> list[Produto]:
    produtos = repository.listar()

    if not produtos:
        print("Nenhum produto cadastrado.")
        return produtos

    cabecalhos = [
        "ID",
        "Nome",
        "Quantidade",
        "Preço",
        "Categoria",
        "Data de criação",
        "Data da última alteração",
    ]
    linhas = [
        [
            str(produto.id),
            produto.nome,
            str(produto.quantidade),
            str(produto.preco),
            str(produto.categoria),
            str(produto.data_criacao),
            str(produto.data_ultima_alteracao),
        ]
        for produto in produtos
    ]
    larguras = [
        max(len(cabecalho), *(len(linha[indice]) for linha in linhas))
        for indice, cabecalho in enumerate(cabecalhos)
    ]
    separador = "+-" + "-+-".join("-" * largura for largura in larguras) + "-+"

    print("\n===== LISTA DE PRODUTOS =====")
    print(separador)
    print("| " + " | ".join(cabecalho.ljust(larguras[indice]) for indice, cabecalho in enumerate(cabecalhos)) + " |")
    print(separador)
    for linha in linhas:
        print("| " + " | ".join(valor.ljust(larguras[indice]) for indice, valor in enumerate(linha)) + " |")
    print(separador)

    return produtos

def buscar_por_id(self, id_produto: int) -> Produto | None:
    return self._repository.buscar_por_id(id_produto)

def atualizar_produto(repository: ProdutoRepository) -> None:
    try:
        id_produto = int(input("ID do produto que deseja alterar: "))
    except ValueError:
        print("ID inválido.")
        return

    produto = repository.buscar_por_id(id_produto)
    if produto is None:
        print(f"Produto com id {id_produto} não encontrado.")
        return

    print("\nDados atuais do produto:")
    print(f"ID: {produto.id}")
    print(f"Nome: {produto.nome}")
    print(f"Quantidade: {produto.quantidade}")
    print(f"Preço: {produto.preco}")
    print(f"Categoria: {produto.categoria}")
    print(f"Data de criação: {produto.data_criacao}")
    print(f"Data da última alteração: {produto.data_ultima_alteracao}")
    print("Pressione Enter para manter o valor atual.")

    nome_digitado = input(f"Novo nome [{produto.nome}]: ").strip()
    quantidade_texto = input(f"Nova quantidade [{produto.quantidade}]: ").strip()
    preco_texto = input(f"Novo preço [{produto.preco}]: ").strip()
    categoria_digitada = input(f"Nova categoria [{produto.categoria}]: ").strip()

    try:
        nome = nome_digitado if nome_digitado else produto.nome
        quantidade = int(quantidade_texto) if quantidade_texto else produto.quantidade
        preco = decimal.Decimal(preco_texto.replace(",", ".")) if preco_texto else produto.preco
        categoria = categoria_digitada if categoria_digitada else produto.categoria
        produto.atualizar_dados(
            nome=nome,
            quantidade=quantidade,
            preco=preco,
            categoria=categoria,
        )
        repository.salvar(produto)
        print("Produto atualizado com sucesso.")
    except (ValueError, decimal.InvalidOperation) as erro:
        print(f"Não foi possível atualizar o produto: {erro}")

def remover_produto(repository: ProdutoRepository) -> None:
    try:
        id_produto = int(input("ID do produto que deseja remover: "))
    except ValueError:
        print("ID inválido.")
        return

    produto = repository.buscar_por_id(id_produto)
    if produto is None:
        print(f"Produto com id {id_produto} não encontrado.")
        return

    repository.remover(id_produto)
    print(f"Produto '{produto.nome}' removido com sucesso.")


