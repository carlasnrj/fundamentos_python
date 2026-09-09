from login import login_app
from menu import (
    executar_opcao,
    mostrar_menu,
    selecionar_opcao,
)


def main() -> None:

    if not login_app():
        return

    while True:
        mostrar_menu()
        opcao = selecionar_opcao()
        if not executar_opcao(opcao):
            break

if __name__ == "__main__":
    main()