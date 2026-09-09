import csv
import datetime
import decimal
import pathlib

from produto import Produto


class ProdutoRepository:
    def __init__(self, arquivo_csv: str = "produtos.csv"):
        self._arquivo_csv = pathlib.Path(arquivo_csv)
        self._dados: list[Produto] = self._carregar_do_csv()

    def _carregar_do_csv(self) -> list[Produto]:
        if not self._arquivo_csv.exists():
            return []

        produtos: list[Produto] = []
        with self._arquivo_csv.open("r", encoding="utf-8", newline="") as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                produtos.append(
                    Produto(
                        id=int(linha["id"]),
                        nome=linha["nome"],
                        quantidade=int(linha["quantidade"]),
                        preco=decimal.Decimal(linha["preco"]),
                        categoria=linha["categoria"],
                        data_criacao=datetime.datetime.fromisoformat(linha["data_criacao"]),
                        data_ultima_alteracao=datetime.datetime.fromisoformat(linha["data_ultima_alteracao"]),
                    )
                )
        return produtos

    def salvar(self, produto: Produto) -> None:
        if self.buscar_por_id(produto.id) is None:
            self._dados.append(produto)
        else:
            for indice, item in enumerate(self._dados):
                if item.id == produto.id:
                    self._dados[indice] = produto
                    break
        self._persistir()

    def listar(self) -> list[Produto]:
        return self._dados

    def buscar_por_id(self, id_produto: int) -> Produto | None:
        for produto in self._dados:
            if produto.id == id_produto:
                return produto
        return None

    def remover(self, id_produto: int) -> bool:
        produto = self.buscar_por_id(id_produto)
        if produto is None:
            return False

        self._dados = [item for item in self._dados if item.id != id_produto]
        self._persistir()
        return True

    def _persistir(self) -> None:
        self._arquivo_csv.parent.mkdir(parents=True, exist_ok=True)
        with self._arquivo_csv.open("w", encoding="utf-8", newline="") as arquivo:
            escritor = csv.DictWriter(
                arquivo,
                fieldnames=[
                    "id",
                    "nome",
                    "quantidade",
                    "preco",
                    "categoria",
                    "data_criacao",
                    "data_ultima_alteracao",
                ],
            )
            escritor.writeheader()
            for produto in self._dados:
                escritor.writerow(
                    {
                        "id": produto.id,
                        "nome": produto.nome,
                        "quantidade": produto.quantidade,
                        "preco": str(produto.preco),
                        "categoria": produto.categoria,
                        "data_criacao": produto.data_criacao.isoformat(),
                        "data_ultima_alteracao": produto.data_ultima_alteracao.isoformat(),
                    }
                )

    def salvar_arquivo(self) -> None:
        self._persistir()
