# WebScraping para Avaliações do e-SUS

Este projeto consiste em um extractor desenvolvido para coletar avaliações de usuários dos aplicativos do e-SUS, criados pelo Laboratório Bridge da Universidade Federal de Santa Catarina (UFSC).

## Objetivo

O extractor tem como objetivo obter informações relevantes de duas fontes principais:
- **Play Store:** Loja de aplicativos da Google, onde os aplicativos do e-SUS estão disponíveis para o público.
- **Pesquisa de Satisfação Interna:** Servidor que interage com os aplicativos e coleta feedbacks diretamente dos usuários.

A necessidade de desenvolver este extractor surgiu porque, apesar do Laboratório Bridge ser o desenvolvedor dos produtos, o Ministério da Saúde (MS) é o proprietário e detentor dos acessos às funcionalidades administrativas das plataformas. Estas plataformas são essenciais para acessar dados brutos de avaliações e feedbacks.

## Benefícios

Com este extractor, os Product Owners e Designers dos projetos no Bridge podem obter os dados de forma automatizada, economizando tempo significativo que, de outra forma, seria gasto na coleta manual dessas informações. Assim, eles podem se concentrar mais efetivamente na análise das informações recolhidas.

## Entrega e Uso

Ao final deste projeto, espera-se entregar a ferramenta aos stakeholders relevantes, permitindo que eles coletem estas informações de maneira eficiente e pronta para serem importadas em suas ferramentas de análise de dados.

## Instalação

Para instalar as dependências necessárias do projeto, execute o seguinte comando:

```bash
pip install -r requirements.txt
```

## Execução

Para rodar o projeto, utilize o comando

```bash
python3 main.py
```
