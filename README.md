# Gerador de Slides

Aplicação web que transforma um texto (letras de música, liturgia, avisos) em uma apresentação **PowerPoint (.pptx)** no estilo Holyrics: fundo escuro, letra grande, em negrito e centralizada, pronta para projetar.

Você cola o texto, escolhe as cores, confere a prévia e baixa o arquivo.

## Funcionalidades

- **Um slide por bloco:** cada parte do texto separada por uma linha em branco vira um slide.
- **Prévia ao vivo** dos slides em 16:9, com as cores escolhidas.
- **Cor de fundo e cor do texto** escolhidas no seletor de cor.
- **Download direto** do `.pptx` (16:9, fonte 54 em negrito, texto centralizado).
- **Validação na API:** recusa cores fora do formato `#RRGGBB` e texto vazio, com uma mensagem de erro clara.

## Tecnologias

| Camada | Tecnologias |
|---|---|
| Back-end | Python, [FastAPI](https://fastapi.tiangolo.com/), [python-pptx](https://python-pptx.readthedocs.io/), Pydantic |
| Front-end | [React](https://react.dev/), [Vite](https://vite.dev/), CSS Modules |
| Deploy | Vercel (front-end estático + função Python em `api/`) |

## Estrutura

```
gerador-slides/
├── api/
│   └── index.py              # API FastAPI + geração do .pptx
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── EditorTexto/  # área de texto
│   │   │   ├── SeletorCores/ # cores de fundo e de texto
│   │   │   ├── PreviaSlides/ # prévia 16:9 dos slides
│   │   │   └── Botao/        # botão (com variação "perigo")
│   │   ├── hooks/
│   │   │   └── useGerarSlides.js  # chama a API e faz o download
│   │   ├── App.jsx
│   │   └── main.jsx
│   └── vite.config.js        # proxy /api -> http://127.0.0.1:8000
└── requirements.txt
```

## Como rodar localmente

Pré-requisitos: **Python 3.10+** e **Node.js 20+**.

### 1. API (na raiz do projeto)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn api.index:app --reload
```

A API sobe em `http://127.0.0.1:8000`. A documentação interativa (Swagger) fica em `http://127.0.0.1:8000/docs`.

### 2. Front-end (em outro terminal)

```powershell
cd frontend
npm install
npm run dev
```

Abra o endereço que o Vite mostrar (normalmente `http://localhost:5173`). O Vite repassa as chamadas para `/api` à API local.

## Como usar

Separe cada slide com **uma linha em branco**:

```
Grande é o Senhor
e mui digno de louvor

Na cidade do nosso Deus
no seu santo monte
```

Esse texto gera **2 slides**. As quebras de linha dentro de um bloco são mantidas no slide.

## API

### `POST /api/gerar_slides`

**Corpo (JSON):**

```json
{
  "texto": "Primeiro slide\n\nSegundo slide",
  "cor_fundo": "#000000",
  "cor_texto": "#FFFFFF"
}
```

| Campo | Tipo | Regra |
|---|---|---|
| `texto` | string | precisa ter pelo menos um bloco com conteúdo |
| `cor_fundo` | string | hexadecimal `#RRGGBB` (o `#` é opcional) |
| `cor_texto` | string | hexadecimal `#RRGGBB` (o `#` é opcional) |

**Respostas:**

| Status | Quando |
|---|---|
| `200` | devolve o arquivo `slides.pptx` |
| `400` | texto vazio |
| `422` | campo faltando, tipo errado ou cor em formato inválido |

## Próximos passos

- [ ] Deploy na Vercel
- [ ] Diminuir a fonte automaticamente quando o bloco for muito grande
- [ ] Mostrar no front a mensagem de erro que a API devolve
- [ ] Testes automatizados com `pytest`

## Autor

Feito por **Arthur**, estudante de Ciência da Computação na UFG.
