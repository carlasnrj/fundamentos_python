#teste

# Sistema de Gestão de Produtos

Aplicação de linha de comando desenvolvida em Python para cadastro e gerenciamento de produtos.

## Funcionalidades

- Login de acesso
- Cadastro de produtos
- Listagem em formato de tabela
- Atualização parcial de produtos
- Remoção de produtos
- Persistência em arquivo CSV local

## Requisitos

- Python 3.10 ou superior

## Como executar

Na raiz do projeto, execute:

```bash
python main.py
```

Use as opções exibidas no menu para cadastrar, consultar, alterar ou remover produtos.

## Dados locais

O arquivo `dados/produtos.csv` é criado e mantido somente na máquina local. Ele está ignorado pelo Git para que os dados de uso não sejam publicados no GitHub. A pasta `dados` é mantida no repositório apenas por meio de `.gitkeep`.

## Estrutura principal

```text
.
|-- main.py
|-- menu.py
|-- login.py
|-- produto.py
|-- produto_service.py
|-- produto_repository.py
|-- categoria.py
|-- categoria_item.py
`-- dados/
```

## Categorias disponíveis

`VESTUARIO`, `FUTEBOL`, `VOLEIBOL`, `CALCADOS`, `ACESSORIOS` e `OUTROS`.
