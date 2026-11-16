import { useState } from "react";
import styles from "./App.module.css";
import EditorTexto from "./components/EditorTexto/EditorTexto";
import PreviaSlides from "./components/PreviaSlides/PreviaSlides";
import SeletorCores from "./components/SeletorCores/SeletorCores";
import Botao from "./components/Botao/Botao";
import useGerarSlides from "./hooks/useGerarSlides";

function App() {
  const [texto, setTexto] = useState("");
  const [corFundo, setCorFundo] = useState("#000000");
  const [corTexto, setCorTexto] = useState("#FFFFFF");

  const { carregando, gerar } = useGerarSlides();

  function aoClicarGerar() {
    gerar(texto, corFundo, corTexto);
  }

  function apagar() {
    setTexto("");
  }

  let textoBotao = "Gerar slides";
  if (carregando) {
    textoBotao = "Gerando...";
  }

  return (
    <div className={styles.pagina}>
      <header className={styles.cabecalho}>
        <h1>Gerador de Slides</h1>
        <p>Cole o texto, escolha as cores e baixe o PowerPoint.</p>
      </header>

      <main className={styles.conteudo}>
        <section className={styles.coluna}>
          <h2>Texto</h2>
          <EditorTexto texto={texto} setTexto={setTexto} />

          <SeletorCores
            corFundo={corFundo}
            setCorFundo={setCorFundo}
            corTexto={corTexto}
            setCorTexto={setCorTexto}
          />

          <div className={styles.botoes}>
            <Botao onClick={aoClicarGerar} disabled={carregando || texto.trim() === ""}>
              {textoBotao}
            </Botao>
            <Botao perigo onClick={apagar} disabled={texto === ""}>
              Apagar
            </Botao>
          </div>
        </section>

        <section className={styles.coluna}>
          <h2>Prévia</h2>
          <div className={styles.previa}>
            {texto.trim() === "" ? (
              <p className={styles.vazio}>Os slides vão aparecer aqui.</p>
            ) : (
              <PreviaSlides texto={texto} corFundo={corFundo} corTexto={corTexto} />
            )}
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;
