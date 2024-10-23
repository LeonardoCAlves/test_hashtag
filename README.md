# 🚀 Projeto de Automação para Cadastro de Produtos

Este [Projeto](https://github.com/LeonardoCAlves/test_hashtag/blob/upstream/doc/desafio.md) utiliza **Selenium** para automatizar o cadastro de produtos em um formulário web a partir de um arquivo CSV. O arquivo CSV contém os dados dos produtos a serem cadastrados, e o script faz login na página, preenche os campos do formulário e submete os dados automaticamente.

## 📑 Descrição

- A automação realiza o login na página do desafio:
  [Hashtag Treinamentos](https://dlp.hashtagtreinamentos.com/python/intensivao/login?ps=incompany)
  
- Lê os dados de produtos de um arquivo `produtos.csv` na pasta `base`.
  
- Preenche os seguintes campos do formulário:
  - **Código**
  - **Marca**
  - **Tipo**
  - **Categoria**
  - **Preço Unitário**
  - **Custo**
  - **Observações**

- Submete o formulário após preencher os campos.

## 🛠️ Tecnologias Utilizadas

- **Python**
- **Selenium**: Automação de navegação web.
- **webdriver-manager**: Para gerenciamento automático do `ChromeDriver`.
- **CSV**: Leitura de arquivos CSV para obter os dados dos produtos.

## 📂 Estrutura de Pastas

```bash
📦TEST_HASHTAG
 ┣ 📂base
 ┃ ┗ 📄produtos.csv   # Arquivo contendo os dados dos produtos
 ┣ 📂doc
 ┃ ┗ 📄desafio.csv    # Detalhes sobre o desafio.
 ┣ 📂venv             # Ambiente virtual
 ┣ 📜main.py          # Script principal da automação
```

## 🚀 Como Rodar o Projeto (Comandos devem ser executados no terminal)

- Clonar o Repositório
```bash
git clone https://github.com/LeonardoCAlves/test_hashtag
cd ProjetoAutomacao
```
- Criar um Ambiente Virtual (Windows)
```bash
python -m venv venv
source venv/bin/activate
```
- Configurar Variável de Ambiente 
```bash
setx EMAIL_PASS 'sua_senha_aqui'
```

### 🚀 Como Rodar o Projeto (Arquivo executável)

> Importe ressaltar que o arquivo executável precisa encontrar a pasta 'Base' e o arquivo 'produtos.csv', de forma que, é necessário que a pasta 'Base' esteja na mesma pasta na qual vc guardou o arquivo main.exe

## 🔗 Download do Executável

Baixe o arquivo executável → [Download](https://drive.google.com/drive/folders/1ert0GBn8gJ1JVfLb2qkZkGrzOpQ6XqzP?usp=sharing).

