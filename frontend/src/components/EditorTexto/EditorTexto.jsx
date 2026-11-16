import styles from './EditorTexto.module.css';


function EditorTexto(props) {
    function aoDigitar(event) {
        props.setTexto(event.target.value);
    }
    return (
        <textarea
            className={styles.editor}
            value={props.texto}
            onChange={aoDigitar}
            placeholder="Cole o texto aqui. Deixe uma linha em branco entre cada slide."
        />
    );
}

export default EditorTexto;

