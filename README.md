# Painel de Conteúdo - TV Corporativa

Este projeto é um painel de conteúdo digital, projetado para ser exibido em uma TV corporativa. Ele exibe informações úteis e atualizadas de diversas fontes, como notícias, previsão do tempo, cotações de câmbio e muito mais.

## Como Usar

Para utilizar o painel, basta abrir o arquivo `index.html` em um navegador de internet. O painel foi projetado para ser executado localmente, sem a necessidade de um servidor web.

O menu principal (`index.html`) permite navegar entre os diferentes painéis de conteúdo.

## Aplicações

O painel é composto pelas seguintes aplicações:

- **Notícias:** Exibe as últimas notícias de diversas fontes de RSS, como Google Notícias, G1, Investing.com, etc. É possível adicionar novas fontes de notícias facilmente.
- **Previsão do Tempo:** Mostra a previsão do tempo para uma localidade específica.
- **Cotação do Câmbio:** Apresenta as cotações de moedas estrangeiras.
- **Tráfego:** Exibe informações de tráfego para uma região pré-definida.
- **Pensamento do Dia:** Mostra uma citação ou pensamento inspirador.

## Detalhes Técnicos

O projeto é construído utilizando tecnologias web padrão:

- **HTML:** Para a estrutura das páginas.
- **CSS:** Para a estilização e aparência do painel.
- **JavaScript:** Para a lógica de busca e exibição dos dados.

A aplicação de notícias utiliza a biblioteca [rss-parser](https://github.com/rbren/rss-parser) para processar os feeds RSS. Para contornar as restrições de CORS (Cross-Origin Resource Sharing) dos navegadores, a aplicação utiliza um proxy CORS (`https://corsproxy.io/`).

## Adicionando Novas Fontes de Notícias

Para adicionar uma nova fonte de notícias, siga os passos abaixo:

1.  Abra o arquivo `index.html` em um editor de texto.
2.  Encontre a seção com a classe `menu-container`.
3.  Adicione um novo link `<a>` para a nova fonte de notícias, seguindo o formato abaixo:

```html
<a href="./noticias_app.html?feedUrl=URL_DO_FEED_RSS&sourceName=NOME_DA_FONTE" class="menu-button">Notícias (NOME_DA_FONTE)</a>
```

Substitua `URL_DO_FEED_RSS` pela URL do feed RSS que você deseja adicionar e `NOME_DA_FONTE` pelo nome da fonte que será exibido no botão e no título da página de notícias.

**Importante:** A URL do feed RSS deve ser codificada (URL encoded). Por exemplo, o caractere `/` deve ser substituído por `%2F`. Você pode usar uma ferramenta online para codificar a URL.
