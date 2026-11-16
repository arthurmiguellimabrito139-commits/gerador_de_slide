import styles from './PreviaSlides.module.css';

function Slides({ corFundo, corTexto , texto }) { 
   
return (
    <div className={styles.slide} style={{ backgroundColor: corFundo, color: corTexto }}>
        <p>{texto}</p>
    </div>
);
}

export default Slides;