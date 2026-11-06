with open("exemplo.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    conteudoPorSlide = conteudo.split("\n\n")
for i in range(0, len(conteudoPorSlide)):
    print(f"Slide {i + 1}:\n{conteudoPorSlide[i]}\n")
