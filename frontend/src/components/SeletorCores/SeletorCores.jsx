import styles from "./SeletorCores.module.css";

function SeletorCores({ corFundo, setCorFundo, corTexto, setCorTexto }) {
  function aoMudarFundo(e) {
    // chame setCorFundo com o valor escolhido
    setCorFundo(e.target.value);
  }

  function aoMudarTexto(e) {
    // chame setCorTexto com o valor escolhido
    setCorTexto(e.target.value);
  }

  return (
    <div className={styles.seletores}>
      <label className={styles.opcao}>
        Cor de fundo
        <input type="color" value={corFundo} onChange={aoMudarFundo} />
      </label>

      <label className={styles.opcao}>
        Cor do texto
        <input type="color" value={corTexto} onChange={aoMudarTexto} />
      </label>
    </div>
  );
}

export default SeletorCores;