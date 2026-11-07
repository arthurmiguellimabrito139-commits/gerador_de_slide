from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

cores = [
    RGBColor(0, 0, 0),        # 0 - preto
    RGBColor(255, 255, 255),  # 1 - branco
    RGBColor(0, 0, 128),      # 2 - azul-marinho
    RGBColor(20, 20, 40),     # 3 - azul quase preto
    RGBColor(40, 0, 60),      # 4 - roxo escuro
    RGBColor(0, 50, 30),      # 5 - verde escuro
    RGBColor(255, 215, 0),    # 6 - dourado
    RGBColor(240, 240, 240),  # 7 - branco suave
    RGBColor(255, 255, 0),    # 8 - amarelo
]

cor_fundo = cores[0]
cor_texto = cores[1]

# 1. Ler o arquivo e dividir em blocos
with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

conteudo_por_slide = conteudo.split("\n\n")

# 2. Criar a apresentação (uma vez só, fora do for)
prs = Presentation()
prs.slide_width = Inches(13.333)   # formato 16:9
prs.slide_height = Inches(7.5)

# 3. Um slide para cada bloco
for i in range(len(conteudo_por_slide)):
    bloco = conteudo_por_slide[i].strip()
    if bloco == "":
        continue

    slide = prs.slides.add_slide(prs.slide_layouts[6])  # slide em branco

    # Fundo
    fundo = slide.background.fill
    fundo.solid()
    fundo.fore_color.rgb = cor_fundo

    # Caixa de texto ocupando o slide inteiro
    caixa = slide.shapes.add_textbox(Inches(0), Inches(0), prs.slide_width, prs.slide_height)
    quadro = caixa.text_frame
    quadro.word_wrap = True
    quadro.vertical_anchor = MSO_ANCHOR.MIDDLE  # centraliza na vertical
    quadro.text = bloco

    # Formatar cada linha do bloco
    for paragrafo in quadro.paragraphs:
        paragrafo.alignment = PP_ALIGN.CENTER   # centraliza na horizontal
        paragrafo.font.size = Pt(54)
        paragrafo.font.bold = True
        paragrafo.font.color.rgb = cor_texto

# 4. Salvar (fora do for)
prs.save("slides.pptx")
print("slides.pptx criado!")