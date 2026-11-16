import styles from './PreviaSlides.module.css';
import Slides from "./Slide";

function PreviaSlides({ corFundo, corTexto, texto }) {
    
    // Mesma regra da API (dividir_blocos): linha vazia ou só com espaços separa os slides
    const linhas = texto.split(/\r?\n/);
    const blocos = [];
    let linhasDoBloco = [];

    for (let i = 0; i < linhas.length; i++) {
        const linha = linhas[i].trim();
        if (linha === "") {
            if (linhasDoBloco.length > 0) {
                blocos.push(linhasDoBloco.join("\n"));
                linhasDoBloco = [];
            }
        } else {
            linhasDoBloco.push(linha);
        }
    }

    // o último bloco não tem linha vazia depois dele
    if (linhasDoBloco.length > 0) {
        blocos.push(linhasDoBloco.join("\n"));
    }

    return (
        <div className={styles.previaSlides}>
            {blocos.map((slideTexto, index) => (
                <Slides key={index} texto={slideTexto} corFundo={corFundo} corTexto={corTexto} />
            ))}
        </div>
    );

}

export default PreviaSlides;