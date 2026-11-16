from io import BytesIO
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel, Field

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


def dividir_blocos(texto):
    # Lê linha por linha: uma linha vazia (ou só com espaços) separa os slides.
    # splitlines() também entende a quebra de linha do Windows (\r\n).
    blocos = []
    linhas_do_bloco = []

    for linha in texto.splitlines():
        if linha.strip() == "":
            if len(linhas_do_bloco) > 0:
                blocos.append("\n".join(linhas_do_bloco))
                linhas_do_bloco = []
        else:
            linhas_do_bloco.append(linha.strip())

    # o último bloco não tem linha vazia depois dele
    if len(linhas_do_bloco) > 0:
        blocos.append("\n".join(linhas_do_bloco))

    return blocos


def gerar_slides(texto, cor_fundo, cor_texto):
    conteudo_por_slide = dividir_blocos(texto)

    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    for bloco in conteudo_por_slide:
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

app = FastAPI()

# Cor no formato "#RRGGBB" (o "#" é opcional). Ex.: "#000000", "ffd700"
PADRAO_COR = r"^#?[0-9A-Fa-f]{6}$"


class Pedido(BaseModel):
    texto: str
    cor_fundo: str = Field(pattern=PADRAO_COR)
    cor_texto: str = Field(pattern=PADRAO_COR)


@app.post("/api/gerar_slides")
def gerar(pedido: Pedido):
    if len(dividir_blocos(pedido.texto)) == 0:
        raise HTTPException(status_code=400, detail="O texto está vazio.")

    fundo = RGBColor.from_string(pedido.cor_fundo.replace("#", ""))
    letra = RGBColor.from_string(pedido.cor_texto.replace("#", ""))

    dados = gerar_slides(pedido.texto, fundo, letra)

    return Response(
        content=dados,
        media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation",
        headers={"Content-Disposition": "attachment; filename=slides.pptx"},
    )