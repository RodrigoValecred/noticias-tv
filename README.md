# Painel de Conteúdo - TV Corporativa

Este projeto é um painel de conteúdo digital, projetado para ser exibido em uma TV corporativa. Ele exibe informações úteis e atualizadas, com foco na aplicação de notícias.

## Aplicações

O painel é composto por várias aplicações, com destaque para:

-   **Notícias (`noticias_app.html`):** Exibe as últimas notícias de forma automática e com suporte a múltiplos temas visuais.
-   **Outras Aplicações:** O projeto também inclui placeholders para previsão do tempo, cotações de câmbio, etc.

## Como Funciona a Aplicação de Notícias

A aplicação de notícias foi completamente modernizada para ser automática, robusta e visualmente flexível.

### 1. Atualização Automática de Conteúdo

As notícias são buscadas e atualizadas de forma 100% automática, sem necessidade de qualquer intervenção manual.

-   **Como funciona?** Um fluxo de trabalho do **GitHub Actions** é executado **a cada hora**.
-   **O que ele faz?** A automação executa o script `fetch_news.py`, que busca as notícias mais recentes do Google Notícias Brasil.
-   **Onde ficam as notícias?** O script processa e salva as notícias no arquivo `news.json`. A página da TV lê este arquivo para exibir o conteúdo.

Isso garante que as notícias estejam sempre atualizadas sem sobrecarregar a página de exibição.

### 2. Temas Visuais Dinâmicos

A aparência da página de notícias pode ser alterada dinamicamente através de um parâmetro na URL, permitindo adaptar o visual para diferentes ambientes ou preferências.

Para selecionar um tema, adicione `?theme=NOME_DO_TEMA` ao final da URL.

**Temas Disponíveis:**

| Nome do Tema | Parâmetro na URL                                       | Descrição                                         |
| :----------- | :----------------------------------------------------- | :-------------------------------------------------- |
| **Finance**  | *(Nenhum, é o padrão)*                                 | Tema personalizado da marca (fundo verde, detalhes em amarelo). |
| **Dark**     | `noticias_app.html?theme=dark`                         | Tema escuro genérico (fundo cinza-escuro, detalhes em azul). |
| **Light**    | `noticias_app.html?theme=light`                        | Tema claro para ambientes bem iluminados.           |

## Detalhes Técnicos

O projeto utiliza as seguintes tecnologias:

-   **Frontend (`noticias_app.html`):**
    -   **HTML:** Para a estrutura da página.
    -   **Tailwind CSS (via CDN):** Para um design moderno e responsivo.
    -   **JavaScript:** Para buscar o `news.json` e renderizar o conteúdo e os temas dinamicamente.

-   **Automação (Backend):**
    -   **Python:** O script `fetch_news.py` é responsável pela lógica de busca.
    -   **feedparser:** Biblioteca Python utilizada para processar o feed RSS de notícias.
    -   **GitHub Actions:** Orquestra a execução automática do script e atualiza o `news.json` no repositório.