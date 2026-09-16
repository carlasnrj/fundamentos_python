from reportlab.lib import colors
from reportlab.lib.pagesizes import landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import Paragraph
from reportlab.pdfgen import canvas


WIDTH, HEIGHT = landscape((13.333 * inch, 7.5 * inch))
OUTPUT = "apresentacao_sistema_produtos.pdf"

NAVY = colors.HexColor("#102A43")
BLUE = colors.HexColor("#1F6F8B")
CORAL = colors.HexColor("#F26457")
MINT = colors.HexColor("#DDF3EE")
PALE = colors.HexColor("#F6F8F9")
INK = colors.HexColor("#243B53")
MUTED = colors.HexColor("#627D98")
WHITE = colors.white

styles = getSampleStyleSheet()
BODY = ParagraphStyle(
    "BodyCustom", parent=styles["BodyText"], fontName="Helvetica", fontSize=17,
    leading=25, textColor=INK, spaceAfter=8,
)
SMALL = ParagraphStyle(
    "SmallCustom", parent=BODY, fontSize=12, leading=17, textColor=MUTED,
)
CARD_TITLE = ParagraphStyle(
    "CardTitle", parent=BODY, fontName="Helvetica-Bold", fontSize=15,
    leading=18, textColor=NAVY, spaceAfter=7,
)
CODE = ParagraphStyle(
    "CodeCustom", parent=BODY, fontName="Courier", fontSize=11, leading=15,
    textColor=WHITE,
)


def paragraph(c, text, x, y, w, style=BODY, h=None):
    p = Paragraph(text, style)
    _, ph = p.wrap(w, h or HEIGHT)
    p.drawOn(c, x, y - ph)
    return ph


def header(c, number, eyebrow, title, subtitle=None):
    c.setFillColor(PALE)
    c.rect(0, 0, WIDTH, HEIGHT, fill=1, stroke=0)
    c.setFillColor(CORAL)
    c.rect(0, HEIGHT - 10, WIDTH, 10, fill=1, stroke=0)
    c.setFillColor(MUTED)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(0.65 * inch, HEIGHT - 0.58 * inch, eyebrow.upper())
    c.setFillColor(NAVY)
    c.setFont("Helvetica-Bold", 28)
    c.drawString(0.65 * inch, HEIGHT - 1.12 * inch, title)
    if subtitle:
        paragraph(c, subtitle, 0.67 * inch, HEIGHT - 1.34 * inch, 10.8 * inch, SMALL)
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 9)
    c.drawRightString(WIDTH - 0.65 * inch, 0.38 * inch, f"FUNDAMENTOS DE PYTHON  •  {number:02d}")


def card(c, x, y, w, h, title, text, accent=BLUE):
    c.setFillColor(WHITE)
    c.roundRect(x, y, w, h, 9, fill=1, stroke=0)
    c.setFillColor(accent)
    c.roundRect(x, y + h - 6, w, 6, 3, fill=1, stroke=0)
    paragraph(c, title, x + 16, y + h - 20, w - 32, CARD_TITLE)
    paragraph(c, text, x + 16, y + h - 52, w - 32, BODY)


def pill(c, text, x, y, w, fill=BLUE):
    c.setFillColor(fill)
    c.roundRect(x, y, w, 26, 13, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(x + w / 2, y + 8, text)


def bullet_list(c, items, x, y, w, font_size=17, color=INK):
    for item in items:
        c.setFillColor(CORAL)
        c.circle(x + 5, y - 8, 4, fill=1, stroke=0)
        paragraph(c, item, x + 20, y, w - 20, ParagraphStyle(
            "Bullet", parent=BODY, fontSize=font_size, leading=24, textColor=color,
        ))
        y -= 42


def code_box(c, text, x, y, w, h):
    c.setFillColor(NAVY)
    c.roundRect(x, y, w, h, 8, fill=1, stroke=0)
    lines = text.split("\n")
    c.setFillColor(colors.HexColor("#B8E0D2"))
    c.setFont("Courier", 11)
    for i, line in enumerate(lines):
        c.drawString(x + 16, y + h - 23 - i * 16, line)


def slide_title(c):
    c.setFillColor(NAVY)
    c.rect(0, 0, WIDTH, HEIGHT, fill=1, stroke=0)
    c.setFillColor(CORAL)
    c.rect(0, HEIGHT - 12, WIDTH, 12, fill=1, stroke=0)
    c.setFillColor(MINT)
    c.circle(WIDTH - 1.45 * inch, HEIGHT - 1.25 * inch, 0.72 * inch, fill=1, stroke=0)
    c.setFillColor(CORAL)
    c.circle(WIDTH - 2.05 * inch, HEIGHT - 1.85 * inch, 0.25 * inch, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 13)
    c.drawString(0.78 * inch, HEIGHT - 1.1 * inch, "FUNDAMENTOS DE PYTHON")
    c.setFont("Helvetica-Bold", 40)
    c.drawString(0.78 * inch, HEIGHT - 2.15 * inch, "Sistema de Gestão")
    c.drawString(0.78 * inch, HEIGHT - 2.75 * inch, "de Produtos")
    paragraph(c, "Como o código foi organizado, quais decisões sustentam a solução e onde ela pode evoluir.", 0.82 * inch, HEIGHT - 3.15 * inch, 6.1 * inch, ParagraphStyle(
        "Intro", parent=BODY, fontSize=18, leading=26, textColor=MINT,
    ))
    pill(c, "PYTHON 3.10+", 0.82 * inch, 1.2 * inch, 1.45 * inch, CORAL)
    pill(c, "CLI + CSV", 2.42 * inch, 1.2 * inch, 1.18 * inch, BLUE)
    c.setFillColor(MINT)
    c.setFont("Helvetica", 11)
    c.drawString(0.82 * inch, 0.72 * inch, "Apresentação do projeto  •  2026")


def build_pdf():
    c = canvas.Canvas(OUTPUT, pagesize=(WIDTH, HEIGHT))

    slide_title(c)
    c.showPage()

    header(c, 2, "01  •  Visão geral", "O problema que o sistema resolve", "Uma aplicação de terminal para manter um catálogo pequeno, local e persistente.")
    bullet_list(c, [
        "Autenticar o operador antes de liberar o acesso.",
        "Cadastrar produtos com identificação, preço, quantidade e categoria.",
        "Consultar, alterar parcialmente e remover registros.",
        "Manter os dados entre execuções usando um arquivo CSV.",
    ], 0.82 * inch, 4.9 * inch, 6.3 * inch)
    card(c, 7.55 * inch, 2.05 * inch, 4.75 * inch, 2.8 * inch, "Escopo escolhido", "Uma solução simples e didática: poucos módulos, biblioteca padrão e armazenamento sem banco de dados.", CORAL)
    card(c, 7.55 * inch, 0.82 * inch, 4.75 * inch, 0.95 * inch, "Entrada", "python main.py", BLUE)
    c.showPage()

    header(c, 3, "02  •  Arquitetura", "Cada módulo tem uma responsabilidade", "A separação reduz acoplamento e torna o fluxo mais fácil de entender e testar.")
    boxes = [
        ("main.py", "inicia o programa", 0.75 * inch, 3.55 * inch, BLUE),
        ("login.py", "autentica o usuário", 3.2 * inch, 3.55 * inch, CORAL),
        ("menu.py", "coordena escolhas", 5.65 * inch, 3.55 * inch, BLUE),
        ("produto_service.py", "aplica operações", 8.1 * inch, 3.55 * inch, CORAL),
        ("produto_repository.py", "persiste no CSV", 10.55 * inch, 3.55 * inch, BLUE),
    ]
    for name, desc, x, y, accent in boxes:
        c.setFillColor(WHITE)
        c.roundRect(x, y, 1.95 * inch, 1.0 * inch, 8, fill=1, stroke=0)
        c.setFillColor(accent)
        c.circle(x + 0.26 * inch, y + 0.72 * inch, 0.08 * inch, fill=1, stroke=0)
        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 11)
        c.drawString(x + 0.42 * inch, y + 0.64 * inch, name)
        c.setFillColor(MUTED)
        c.setFont("Helvetica", 10)
        c.drawString(x + 0.18 * inch, y + 0.28 * inch, desc)
    c.setStrokeColor(CORAL)
    c.setLineWidth(2)
    for x in [2.72, 5.17, 7.62, 10.07]:
        c.line(x * inch, 4.05 * inch, (x + 0.38) * inch, 4.05 * inch)
        c.line((x + 0.32) * inch, 4.12 * inch, (x + 0.38) * inch, 4.05 * inch)
        c.line((x + 0.32) * inch, 3.98 * inch, (x + 0.38) * inch, 4.05 * inch)
    paragraph(c, "A entidade Produto fica no centro: representa o dado e protege regras como categoria válida e atualização de timestamps.", 1.25 * inch, 2.6 * inch, 10.8 * inch, ParagraphStyle("Center", parent=BODY, fontSize=18, leading=26, alignment=1))
    c.showPage()

    header(c, 4, "03  •  Execução", "Do login à operação escolhida", "O programa permanece em um laço até o usuário escolher sair.")
    steps = [
        ("1", "login_app()", "até 3 tentativas"),
        ("2", "mostrar_menu()", "exibe CRUD"),
        ("3", "selecionar_opcao()", "lê entrada"),
        ("4", "executar_opcao()", "chama serviço"),
        ("5", "repository", "lê ou grava CSV"),
    ]
    for i, (number, title, desc) in enumerate(steps):
        x = 0.75 * inch + i * 2.48 * inch
        c.setFillColor(CORAL if i in (0, 4) else BLUE)
        c.circle(x + 0.38 * inch, 3.72 * inch, 0.27 * inch, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont("Helvetica-Bold", 13)
        c.drawCentredString(x + 0.38 * inch, 3.67 * inch, number)
        paragraph(c, title, x, 3.2 * inch, 1.85 * inch, CARD_TITLE)
        paragraph(c, desc, x, 2.72 * inch, 1.85 * inch, SMALL)
        if i < 4:
            c.setStrokeColor(MUTED)
            c.setLineWidth(1)
            c.line(x + 0.75 * inch, 3.72 * inch, x + 2.12 * inch, 3.72 * inch)
    code_box(c, "while True:\n    mostrar_menu()\n    opcao = selecionar_opcao()\n    if not executar_opcao(opcao):\n        break", 3.5 * inch, 0.75 * inch, 6.3 * inch, 1.45 * inch)
    c.showPage()

    header(c, 5, "04  •  Modelo", "Produto é a unidade de negócio", "A classe usa dataclass para concentrar dados e comportamento relacionado ao produto.")
    code_box(c, "@dataclass(slots=True)\nclass Produto:\n    id: int\n    nome: str\n    quantidade: int\n    preco: Decimal\n    categoria: str | Categoria\n    data_criacao: datetime\n    data_ultima_alteracao: datetime | None", 0.72 * inch, 1.18 * inch, 5.6 * inch, 3.65 * inch)
    card(c, 6.75 * inch, 3.2 * inch, 2.6 * inch, 1.65 * inch, "Decimal", "Evita tratar preço como float e deixa a representação monetária mais previsível.", CORAL)
    card(c, 9.55 * inch, 3.2 * inch, 2.6 * inch, 1.65 * inch, "Enum", "Categoria.validar() normaliza e rejeita valores fora do conjunto permitido.", BLUE)
    card(c, 6.75 * inch, 1.18 * inch, 5.4 * inch, 1.6 * inch, "Atualização parcial", "Enter mantém o valor atual; atualizar_dados() altera apenas os campos recebidos e marca a última alteração.", CORAL)
    c.showPage()

    header(c, 6, "05  •  Operações", "CRUD com regras próximas do uso", "O módulo de serviço traduz entradas do terminal em operações sobre ProdutoRepository.")
    crud = [
        ("CREATE", "cadastrar_produto", "Converte entradas, valida ID duplicado e salva."),
        ("READ", "listar_produtos", "Busca a lista e monta uma tabela textual."),
        ("UPDATE", "atualizar_produto", "Localiza por ID e permite alterar campos individualmente."),
        ("DELETE", "remover_produto", "Localiza, remove e persiste novamente."),
    ]
    for i, (label, func, desc) in enumerate(crud):
        x = 0.8 * inch + (i % 2) * 6.05 * inch
        y = 3.25 * inch - (i // 2) * 1.75 * inch
        card(c, x, y, 5.35 * inch, 1.25 * inch, f"{label}  /  {func}()", desc, CORAL if i % 2 else BLUE)
    c.setFillColor(MUTED)
    c.setFont("Helvetica-Oblique", 11)
    c.drawString(0.85 * inch, 0.95 * inch, "A camada recebe o repository por parâmetro: isso facilita trocar a persistência em testes ou em uma evolução futura.")
    c.showPage()

    header(c, 7, "06  •  Persistência", "O CSV funciona como uma pequena base local", "O repositório esconde detalhes de arquivo para o restante do sistema.")
    code_box(c, "CSV  ->  DictReader  ->  Produto\nProduto  ->  DictWriter  ->  CSV", 0.85 * inch, 3.65 * inch, 4.7 * inch, 1.25 * inch)
    bullet_list(c, [
        "Ao iniciar, carrega registros e converte tipos: int, Decimal e datetime.",
        "Ao salvar ou remover, reescreve o arquivo completo com cabeçalho e ISO dates.",
        "Cria a pasta pai automaticamente quando necessário.",
    ], 6.05 * inch, 4.75 * inch, 6.2 * inch, 15)
    c.setFillColor(MINT)
    c.roundRect(0.85 * inch, 1.25 * inch, 4.7 * inch, 1.45 * inch, 8, fill=1, stroke=0)
    paragraph(c, "Por que CSV?", 1.08 * inch, 2.38 * inch, 2 * inch, CARD_TITLE)
    paragraph(c, "Baixa complexidade, fácil inspeção manual e suficiente para um catálogo pequeno/local.", 1.08 * inch, 2.05 * inch, 4.1 * inch, SMALL)
    c.showPage()

    header(c, 8, "07  •  Exemplo", "Uma sessão típica no terminal", "O comportamento esperado pode ser entendido acompanhando uma única jornada do usuário.")
    terminal = [
        ("$ python main.py", MINT),
        ("=== LOGIN ===", WHITE),
        ("Usuário: admin", WHITE),
        ("Senha: 1234", WHITE),
        ("Acesso liberado.", MINT),
        ("1 - Cadastrar   2 - Consultar", WHITE),
        ("Escolha uma opção: 1", CORAL),
        ("Produto cadastrado com sucesso.", MINT),
    ]
    c.setFillColor(NAVY)
    c.roundRect(1.0 * inch, 1.05 * inch, 6.05 * inch, 4.65 * inch, 10, fill=1, stroke=0)
    c.setFont("Courier", 14)
    for i, (line, color) in enumerate(terminal):
        c.setFillColor(color)
        c.drawString(1.35 * inch, 5.25 * inch - i * 0.46 * inch, line)
    card(c, 7.75 * inch, 3.65 * inch, 4.4 * inch, 1.65 * inch, "O que acontece por trás", "menu.py cria o repository; o serviço coleta e valida; Produto representa; repository persiste.", CORAL)
    card(c, 7.75 * inch, 1.45 * inch, 4.4 * inch, 1.65 * inch, "Por que esse exemplo importa", "Ele conecta as funções abstratas do código ao resultado que o operador vê na tela.", BLUE)
    c.showPage()

    header(c, 9, "08  •  Racional", "Decisões que tornam o código compreensível", "A estrutura privilegia legibilidade e separação de responsabilidades para o tamanho do problema.")
    decisions = [
        ("Biblioteca padrão", "Menos dependências e instalação simples."),
        ("Repository", "Isola leitura e escrita do CSV."),
        ("Dataclass", "Declara o modelo com pouco código repetido."),
        ("Enum de categorias", "Transforma valores livres em conjunto conhecido."),
        ("Injeção do repository", "Permite substituir a persistência com baixo impacto."),
        ("Laço principal", "Mantém a interação ativa até a opção 0."),
    ]
    for i, (title, desc) in enumerate(decisions):
        x = 0.8 * inch + (i % 3) * 4.15 * inch
        y = 3.75 * inch - (i // 3) * 1.75 * inch
        card(c, x, y, 3.55 * inch, 1.25 * inch, title, desc, [BLUE, CORAL, BLUE][i % 3])
    c.showPage()

    header(c, 10, "09  •  Evolução", "O que eu melhoraria em uma próxima versão", "O projeto cumpre o escopo didático; estes são os próximos ganhos de robustez.")
    improvements = [
        ("Segurança", "Retirar credenciais do código e usar hash/variáveis de ambiente."),
        ("Validação", "Impedir ID, quantidade e preço negativos; exigir nome não vazio."),
        ("Coesão", "Transformar operações do service em métodos da classe ou remover a classe não usada."),
        ("Confiabilidade", "Tratar CSV inválido e usar escrita temporária/atômica."),
        ("Testes", "Cobrir login, categoria, CRUD e conversões do repository."),
        ("Caminho do arquivo", "Resolver o CSV relativo à raiz do projeto, não ao diretório atual."),
    ]
    for i, (title, desc) in enumerate(improvements):
        y = 4.8 * inch - i * 0.57 * inch
        c.setFillColor(CORAL if i < 2 else BLUE)
        c.circle(0.95 * inch, y - 4, 4, fill=1, stroke=0)
        c.setFillColor(NAVY)
        c.setFont("Helvetica-Bold", 14)
        c.drawString(1.2 * inch, y - 9, title)
        c.setFillColor(INK)
        c.setFont("Helvetica", 13)
        c.drawString(3.0 * inch, y - 9, desc)
    c.setFillColor(MINT)
    c.roundRect(8.85 * inch, 1.08 * inch, 3.25 * inch, 1.3 * inch, 8, fill=1, stroke=0)
    paragraph(c, "Mensagem final", 9.1 * inch, 2.1 * inch, 2.7 * inch, CARD_TITLE)
    paragraph(c, "A arquitetura já separa as decisões principais; a próxima etapa é fortalecer as bordas.", 9.1 * inch, 1.78 * inch, 2.7 * inch, SMALL)
    c.showPage()

    c.setFillColor(NAVY)
    c.rect(0, 0, WIDTH, HEIGHT, fill=1, stroke=0)
    c.setFillColor(CORAL)
    c.rect(0, HEIGHT - 12, WIDTH, 12, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont("Helvetica-Bold", 30)
    c.drawString(0.85 * inch, HEIGHT - 2.0 * inch, "Obrigado")
    paragraph(c, "Sistema de Gestão de Produtos", 0.9 * inch, HEIGHT - 2.42 * inch, 5.5 * inch, ParagraphStyle("End", parent=BODY, fontSize=20, textColor=MINT))
    c.setFillColor(MINT)
    c.setFont("Helvetica", 12)
    c.drawString(0.9 * inch, 0.85 * inch, "Código-fonte: main.py  •  Execução: python main.py")
    c.save()


if __name__ == "__main__":
    build_pdf()
    print(f"Arquivo gerado: {OUTPUT}")