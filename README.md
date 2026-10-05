# Loja Virtual - Django

Projeto simples de uma loja virtual desenvolvido durante meus estudos de **Django e desenvolvimento web com Python**.

O projeto tem como objetivo praticar os principais conceitos do framework, incluindo criação de modelos, formulários, templates, rotas, integração com banco de dados e gerenciamento de arquivos.

## Tecnologias

* Python
* Django 4.2
* MySQL
* Bootstrap
* Pillow
* django-stdimage

## Funcionalidades

* Cadastro e gerenciamento de produtos
* Controle de preço e estoque
* Upload de imagens dos produtos
* Geração automática de thumbnails
* Geração automática de slug para produtos
* Formulário de contato
* Envio de mensagens por e-mail
* Integração com Django Admin

## Estrutura

O projeto utiliza a estrutura padrão do Django, com separação entre:

* **Models:** definição dos produtos e seus dados
* **Views:** lógica das páginas
* **Forms:** formulário de contato e validação dos dados
* **Templates:** páginas HTML
* **URLs:** configuração das rotas
* **Admin:** gerenciamento dos produtos

## Como executar

Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
cd NOME_DO_REPOSITORIO
```

Crie e ative um ambiente virtual:

```bash
python -m venv venv
```

No Windows:

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure o banco de dados MySQL no arquivo `settings.py` e execute as migrações:

```bash
python manage.py migrate
```

Inicie o servidor:

```bash
python manage.py runserver
```

O projeto estará disponível em:

```text
http://127.0.0.1:8000/
```

## Observação

Este é um projeto desenvolvido durante meus estudos iniciais com Django, com foco na prática dos conceitos fundamentais do framework.
