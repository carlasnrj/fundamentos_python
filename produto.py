from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal

from categoria_item import Categoria


@dataclass(slots=True)
class Produto:
    id: int
    nome: str
    quantidade: int
    preco: Decimal
    categoria: str | Categoria
    data_criacao: datetime = field(default_factory=datetime.now)
    data_ultima_alteracao: datetime | None = None

    def __post_init__(self):
        self.categoria = self._normalizar_categoria(self.categoria)

        agora = datetime.now()  # noqa: DTZ005
        if self.data_criacao is None:
            self.data_criacao = agora        
        self.data_ultima_alteracao = agora

    @staticmethod
    def _normalizar_categoria(categoria: str | Categoria) -> str:
        if isinstance(categoria, Categoria):
            return categoria.value
        return Categoria.validar(categoria)


    def atualizar_dados(
        self,
        *,
        nome: str | None = None,
        quantidade: int | None = None,
        preco: Decimal | None = None,
        categoria: str | Categoria | None = None,
    ) -> None:
        if nome is not None:
            self.nome = nome
        if quantidade is not None:
            self.quantidade = quantidade
        if preco is not None:
            self.preco = preco
        if categoria is not None:
            self.categoria = self._normalizar_categoria(categoria)

        self.data_ultima_alteracao = datetime.now()  # noqa: DTZ005
