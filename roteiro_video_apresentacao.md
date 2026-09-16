# Roteiro do vídeo: Sistema de Gestão de Produtos

**Duração sugerida:** 8 a 10 minutos  
**Formato:** MP4, gravação de tela com narração  
**Apresentadores:** dividir as falas entre os integrantes do grupo

## Organização do vídeo

| Tempo | Parte | Objetivo |
|---|---|---|
| 0:00-0:30 | Abertura | Apresentar o grupo e o projeto |
| 0:30-1:45 | Problema e requisitos | Explicar a necessidade e o escopo |
| 1:45-3:30 | Estrutura da solução | Mostrar a arquitetura e as principais partes do código |
| 3:30-6:30 | Demonstração | Executar o programa e mostrar o fluxo principal |
| 6:30-8:00 | Racional técnico | Explicar as escolhas feitas |
| 8:00-9:00 | Reflexão e encerramento | Relacionar Python a um problema real |

---

## 1. Abertura — 0:00 a 0:30

**Tela:** título da apresentação ou a primeira página do PDF.

**Fala sugerida:**

> Olá. Nós somos o grupo [nome do grupo] e vamos apresentar o nosso projeto de Fundamentos de Python: um Sistema de Gestão de Produtos.
>
> A aplicação foi desenvolvida para funcionar no terminal e permite autenticar um usuário, cadastrar produtos, consultar o estoque, alterar informações e remover registros. Durante a apresentação, vamos explicar o problema, mostrar como o código foi organizado e demonstrar o programa funcionando.

---

## 2. Problema proposto e requisitos — 0:30 a 1:45

**Tela:** slide “O problema que o sistema resolve”.

**Fala sugerida:**

> O problema escolhido foi a necessidade de manter um catálogo de produtos de forma simples e organizada. Mesmo em uma aplicação pequena, é necessário guardar informações como identificação, nome, quantidade, preço e categoria.
>
> A partir desse problema, levantamos os seguintes requisitos funcionais:
>
> Primeiro, o sistema deve exigir login antes de liberar o acesso. Segundo, deve permitir cadastrar produtos. Terceiro, deve listar os produtos cadastrados. Quarto, deve permitir alterar os dados de um produto. Quinto, deve permitir excluir um produto. Por fim, os dados precisam continuar disponíveis depois que o programa for encerrado.
>
> Como requisito técnico, escolhemos Python e o armazenamento em um arquivo CSV local. Essa escolha mantém o projeto simples, sem exigir a instalação de um banco de dados, mas ainda permite persistir os dados.

**Pontos que devem aparecer na tela:**

- Login de acesso.
- Cadastro, consulta, alteração e exclusão.
- Persistência dos dados.
- Execução em terminal.

---

## 3. Solução implementada e estrutura do código — 1:45 a 3:30

### 3.1 Entrada do programa — 1:45 a 2:05

**Tela:** abrir `main.py`.

**Fala sugerida:**

> A execução começa em `main.py`. A função `main()` chama o login e, caso o acesso seja autorizado, entra em um laço principal. Esse laço mostra o menu, lê a opção escolhida e continua executando até o usuário escolher a opção zero.

**Mostrar rapidamente:**

```python
if not login_app():
    return

while True:
    mostrar_menu()
    opcao = selecionar_opcao()
    if not executar_opcao(opcao):
        break
```

### 3.2 Autenticação e menu — 2:05 a 2:25

**Tela:** abrir `login.py` e depois `menu.py`.

**Fala sugerida:**

> O arquivo `login.py` concentra a autenticação. Para esta versão, foi definido um usuário de demonstração e um limite de três tentativas. Depois do login, `menu.py` apresenta as opções disponíveis e direciona cada escolha para a operação correspondente.

> Essa separação evita colocar toda a lógica em um único arquivo e torna o fluxo principal mais legível.

### 3.3 Entidade Produto — 2:25 a 2:50

**Tela:** abrir `produto.py`.

**Fala sugerida:**

> O arquivo `produto.py` define a entidade central do sistema: `Produto`. Usamos `dataclass` para declarar os campos de forma objetiva. O produto possui ID, nome, quantidade, preço, categoria e datas de criação e alteração.

> O preço usa `Decimal`, que é mais adequado para valores monetários do que `float`. A categoria é normalizada e validada com um `Enum`, evitando aceitar categorias que não fazem parte do conjunto definido.

### 3.4 Serviço e repositório — 2:50 a 3:30

**Tela:** mostrar `produto_service.py` e `produto_repository.py`.

**Fala sugerida:**

> `produto_service.py` concentra as operações de cadastro, listagem, atualização e remoção. Ele recebe as entradas do usuário, converte os valores e trata erros de conversão.

> `produto_repository.py` é responsável pela persistência. Ele lê o CSV e transforma cada linha em um objeto `Produto`. No sentido contrário, transforma os objetos em linhas e grava o arquivo novamente.

> Assim, o menu coordena o fluxo, o serviço trata as operações, o modelo representa o produto e o repositório cuida do arquivo. Essa divisão é o principal racional da estrutura do projeto.

**Mostrar o fluxo visualmente:**

```text
main.py -> menu.py -> produto_service.py -> produto_repository.py -> dados/produtos.csv
                              |
                          produto.py
```

---

## 4. Demonstração do programa — 3:30 a 6:30

> **Importante:** antes de iniciar a gravação, abra o terminal na pasta raiz do projeto e confirme que o arquivo `dados/produtos.csv` está disponível. Digite os valores com calma e deixe cada mensagem aparecer por alguns segundos.

### 4.1 Inicialização e login — 3:30 a 4:00

**Tela:** terminal.

**Ação:** executar:

```text
python main.py
```

**Entrada da demonstração:**

```text
Usuário: admin
Senha: 1234
```

**Fala sugerida:**

> Agora vamos executar o sistema. Primeiro aparece a tela de login. Depois de informar as credenciais válidas, o acesso é liberado e o menu principal é exibido.

### 4.2 Consulta dos produtos — 4:00 a 4:35

**Ação:** escolher a opção `2`.

**Fala sugerida:**

> Na opção 2, o sistema consulta o repositório e exibe os produtos em uma tabela. Os dados foram carregados do arquivo CSV no momento em que o repositório foi criado.

**Mostrar:** deixar a tabela visível por aproximadamente 10 segundos.

### 4.3 Cadastro de produto — 4:35 a 5:15

**Ação:** escolher a opção `1` e informar um exemplo como:

```text
ID: 30
Nome: Camisa de treino
Quantidade: 12
Preço: 89,90
Categoria: VESTUARIO
Deseja cadastrar um novo produto? (s/n): n
```

**Fala sugerida:**

> Na opção 1, o sistema coleta os campos do produto. O preço aceita vírgula e é convertido para `Decimal`. Antes de salvar, o programa verifica se já existe um produto com o mesmo ID e também valida a categoria.

> Depois da confirmação, o repository atualiza o arquivo CSV. Esse é o momento em que vemos a entrada do usuário virar um objeto `Produto` e depois virar um registro persistido.

### 4.4 Alteração parcial — 5:15 a 5:55

**Ação:** escolher a opção `3`, informar o ID `30` e alterar somente alguns campos:

```text
ID do produto que deseja alterar: 30
Novo nome [Camisa de treino]: Camisa de treino premium
Nova quantidade [12]: 15
Novo preço [89.90]:
Nova categoria [VESTUARIO]:
```

**Fala sugerida:**

> A opção 3 demonstra uma decisão importante: a atualização é parcial. Quando pressionamos Enter, o valor atual é mantido. Neste exemplo, alteramos o nome e a quantidade, mas preservamos o preço e a categoria.

### 4.5 Consulta e remoção — 5:55 a 6:30

**Ação:** escolher `2` novamente para mostrar a alteração. Depois escolher `4` e remover o produto `30`.

**Fala sugerida:**

> Vamos consultar novamente para confirmar a alteração. Em seguida, usamos a opção 4 para remover o produto de demonstração. O repository retira o item da lista em memória e persiste o novo conteúdo do CSV.

> Finalmente, podemos consultar mais uma vez para confirmar que o registro não aparece mais.

---

## 5. Racional técnico — 6:30 a 8:00

**Tela:** slide “Decisões que tornam o código compreensível”.

**Fala sugerida:**

> A primeira decisão foi usar somente recursos da biblioteca padrão do Python. Isso deixa o projeto fácil de executar e adequado ao objetivo da disciplina.
>
> A segunda foi separar o repositório das regras de interação. Dessa forma, se no futuro trocarmos o CSV por um banco de dados, a maior parte do menu e do serviço poderá continuar igual.
>
> Também usamos `dataclass` porque ela reduz código repetitivo na definição da entidade. O `Enum` ajuda a controlar as categorias, e o `Decimal` representa preços com mais segurança.
>
> O CSV foi suficiente para o escopo porque os dados são locais e o volume esperado é pequeno. Para uma aplicação maior, seria necessário considerar banco de dados, controle de concorrência, autenticação mais segura e testes automatizados.

---

## 6. Reflexão sobre Python e encerramento — 8:00 a 9:00

**Tela:** slide “O que eu melhoraria em uma próxima versão”.

**Fala sugerida:**

> Este projeto mostra que Python pode resolver um problema real com uma quantidade relativamente pequena de código. A linguagem oferece estruturas como funções, classes, `dataclass`, `Enum`, tratamento de exceções e bibliotecas para trabalhar com arquivos.
>
> Ao mesmo tempo, a solução também mostra que fazer o programa funcionar é apenas uma parte do desenvolvimento. Em uma próxima versão, melhoraríamos a segurança das credenciais, validaríamos valores negativos e nomes vazios, trataríamos arquivos CSV inválidos e criaríamos testes automatizados.
>
> A principal conclusão do grupo é que a organização do código é tão importante quanto a funcionalidade. Separar responsabilidades tornou o sistema mais fácil de explicar, manter e evoluir.
>
> Obrigado por assistir à nossa apresentação.

---

## Checklist antes de exportar o vídeo

- [ ] Todos os integrantes aparecem ou participam da narração.
- [ ] O vídeo está em formato MP4.
- [ ] O áudio está compreensível e sem notificações do computador.
- [ ] O terminal está com zoom suficiente para ler os textos.
- [ ] O login, a consulta, o cadastro, a alteração e a remoção foram demonstrados.
- [ ] O arquivo CSV foi conferido antes e depois da demonstração.
- [ ] O vídeo menciona o problema, os requisitos, a solução e a reflexão sobre Python.
- [ ] A duração final está entre 8 e 10 minutos.

## Divisão sugerida entre integrantes

| Integrante | Participação |
|---|---|
| Integrante 1 | Abertura, problema e requisitos |
| Integrante 2 | Arquitetura e `main.py`/`menu.py`, `Produto`, serviço e repository|
| Integrante 3 | Demonstração e reflexão final |

Caso o grupo tenha menos integrantes, uma pessoa pode acumular as partes de código e outra pode conduzir a demonstração.