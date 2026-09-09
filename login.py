def login_app() -> bool:
    usuarios = {"admin": "1234"}
    tentativas = 0

    while tentativas < 3:
        print("\n=== LOGIN ===")
        usuario = input("Usuário: ").strip()
        senha = input("Senha: ").strip()

        if usuarios.get(usuario) == senha:
            print("\nAcesso liberado.")
            return True

        tentativas += 1
        print(f"Usuário ou senha inválidos. Tentativas restantes: {3 - tentativas}")

    print("\nNúmero de tentativas excedido. Acesso bloqueado.")
    return False