from enum import Enum


class Categoria(Enum):
    VESTUARIO = "VESTUARIO"
    FUTEBOL = "FUTEBOL"
    VOLEIBOL = "VOLEIBOL"
    CALCADOS = "CALCADOS"
    ACESSORIOS = "ACESSORIOS"
    OUTROS = "OUTROS"

    @classmethod
    def validar(cls, valor: str) -> str:
        valor_normalizado = str(valor).strip().upper()
        valores_validos = {categoria.value for categoria in cls}

        if valor_normalizado not in valores_validos:
            raise ValueError(
                f"Categoria inválida: '{valor}'. Valores válidos: {sorted(valores_validos)}"
            )

        return valor_normalizado


CATEGORIAS_VALIDAS = [categoria.value for categoria in Categoria]
