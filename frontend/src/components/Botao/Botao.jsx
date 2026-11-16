import styles from "./Botao.module.css";

function Botao({ children, onClick, disabled, perigo }) {
    let classes = styles.botao;
    if (perigo) {
        classes += ` ${styles.perigo}`;
    }

    return (
        <button className={classes} onClick={onClick} disabled={disabled}>
            {children}
        </button>
    );
}

export default Botao;