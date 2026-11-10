from io import BytesIO
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


def gerar_slides(texto, cor_fundo, cor_texto):
    conteudo_por_slide = texto.split("\n\n")

    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    for i in range(len(conteudo_por_slide)):
        bloco = conteudo_por_slide[i].strip()
        if bloco == "":
            continue

        slide = prs.slides.add_slide(prs.slide_layouts[6])

        fundo = slide.background.fill
        fundo.solid()
        fundo.fore_color.rgb = cor_fundo

        caixa = slide.shapes.add_textbox(Inches(0), Inches(0), prs.slide_width, prs.slide_height)
        quadro = caixa.text_frame
        quadro.word_wrap = True
        quadro.vertical_anchor = MSO_ANCHOR.MIDDLE
        quadro.text = bloco

        for paragrafo in quadro.paragraphs:
            paragrafo.alignment = PP_ALIGN.CENTER
            paragrafo.font.size = Pt(54)
            paragrafo.font.bold = True
            paragrafo.font.color.rgb = cor_texto

    arquivo = BytesIO()
    prs.save(arquivo)
    return arquivo.getvalue()      # ← fim da função


# ---------- teste (fora da função) ----------
with open("exemplo.txt", "r", encoding="utf-8") as f:
    texto = f.read()

dados = gerar_slides(texto, cores[0], cores[1])

with open("slides.pptx", "wb") as f:
    f.write(dados)

print("slides.pptx criado!")