# FastAPI Bandas API

Esta é uma API simples construída com o framework FastAPI para gerenciar informações sobre bandas. A API oferece operações básicas, como visualizar bandas existentes e adicionar novas bandas ao "banco de dados".

## Endpoints

### 1. Hello World

- **Endpoint**: `/api/hello`
- **Método**: GET
- **Descrição**: Retorna a mensagem mais famosa da programação.
- **Exemplo de Resposta**:
    ```json
    {"hello": "world"}
    ```

### 2. Saudação por Nome

- **Endpoint**: `/api/sayhi/{nome}`
- **Método**: GET
- **Descrição**: Retorna uma saudação personalizada com base no nome fornecido.
- **Exemplo de Resposta**:
    ```json
    {"Oi": "nome"}
    ```

### 3. Listar Bandas

- **Endpoint**: `/api/bandas`
- **Método**: GET
- **Descrição**: Retorna a lista de todas as bandas no "banco de dados".
- **Exemplo de Resposta**:
    ```json
    [{"banda": "Nome da Banda 1", "genero": "Gênero 1"}, {"banda": "Nome da Banda 2", "genero": "Gênero 2"}, ...]
    ```

### 4. Adicionar Nova Banda

- **Endpoint**: `/api/bandas`
- **Método**: POST
- **Descrição**: Adiciona uma nova banda ao "banco de dados".
- **Parâmetros de Corpo (Body)**: Um objeto JSON representando os detalhes da nova banda.
- **Exemplo de Requisição**:
    ```json
    {"banda": "Nova Banda", "genero": "Novo Gênero"}
    ```
- **Exemplo de Resposta**:
    ```json
    {"message": "Banda adicionada com sucesso!"}
    ```

## Executando Localmente

1. Instale as dependências:
    ```bash
    pip install fastapi uvicorn
    ```

2. Execute o aplicativo:
    ```bash
    uvicorn nome_do_arquivo:app --reload
    ```
    Substitua `nome_do_arquivo` pelo nome do arquivo que contém o código da API.

3. Acesse a documentação interativa da API em `http://127.0.0.1:8000/docs` para explorar e testar os endpoints.

Lembre-se de adaptar o código conforme necessário para atender aos requisitos específicos do seu projeto.
