import produto_service
from produto_repository import ProdutoRepository


def mostrar_menu() -> None:
    print("\n===== SISTEMA DE GESTÃO DE PRODUTOS =====")
    print("1 - Cadastrar produto")
    print("2 - Consultar produtos")
    print("3 - Alterar produto")
    print("4 - Excluir produto")
    print("0 - Sair")

def selecionar_opcao() -> str:
    return input("Escolha uma opção: ").strip()

def executar_opcao(opcao: str) -> bool:
    repository = ProdutoRepository("dados/produtos.csv")    
    if opcao == "1":
        produto_service.cadastrar_produto(repository)
    elif opcao == "2":
        produto_service.listar_produtos(repository)
    elif opcao == "3":
        produto_service.atualizar_produto(repository)
    elif opcao == "4":
        produto_service.remover_produto(repository)
    elif opcao == "0":
        print("Encerrando o sistema...")
        return False
    else:
        print("Opção inválida. Tente novamente.")
    return True