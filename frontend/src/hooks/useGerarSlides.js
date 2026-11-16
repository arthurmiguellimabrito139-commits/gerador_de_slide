import { useState } from "react";

function useGerarSlides() {
  const [carregando, setCarregando] = useState(false);

  async function gerar(texto, corFundo, corTexto) {
    setCarregando(true);
   
    try {
    const resposta = await fetch("/api/gerar_slides", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        texto: texto,
        cor_fundo: corFundo,
        cor_texto: corTexto
      }),
    });

    if (!resposta.ok) {
      alert("Erro ao gerar os slides");
      return;
    }

    // 1. transformar a resposta em blob
    const blob = await resposta.blob();
    // 2. criar a URL com URL.createObjectURL
    const url = URL.createObjectURL(blob);
    // 3. criar o <a>, colocar href e download, e clicar
    const a = document.createElement("a");
    a.href = url;
    a.download = "slides.pptx";
    document.body.appendChild(a);
    a.click();
    // 4. liberar a URL com URL.revokeObjectURL
    URL.revokeObjectURL(url);
} finally {
    setCarregando(false);
}
  }

  return { carregando, gerar };
}

export default useGerarSlides;