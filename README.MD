# ZenStock API

Sistema de Controle de Estoque desenvolvido para facilitar o gerenciamento de produtos, entradas e saídas, reduzindo perdas, otimizando recursos e melhorando a experiência dos usuários em diferentes tipos de negócios.

## Sobre o Projeto

O ZenStock é um sistema web minimalista e responsivo que permite o controle eficiente de estoque para pequenas e médias empresas. Ele resolve problemas como desorganização, perdas, excesso ou falta de produtos, e melhora o fluxo de caixa por meio da automação e visibilidade em tempo real do inventário.

---

## Tecnologias Utilizadas
- **Python** (linguagem de programação principal)
- **Flask** (framework web para Python)
- **MySQL** (sistema de gerenciamento de banco de dados relacional)
- **Docker** (plataforma de contêineres)

### Outras Ferramentas
- **Postman** (para testes e exploração da API)
- **Flasgger (Flask+Swagger)** (para documentação interativa da API)
- **Git & GitHub** (para controle de versão e colaboração)
- **Trello** (para gerenciamento de projetos e metodologia ágil)

---

## Funcionalidades Principais

- **Cadastro e autenticação de usuários**: Gerenciamento de acessos ao sistema.
- **Cadastro, edição, exclusão e pesquisa de produtos, fornecedores, etc**: Controle completo dos itens do estoque e seus parceiros.
- **Gerenciamento de cargos e atividades de funcionários no sistema** (em desenvolvimento): Controle de permissões e auditoria de ações.
- **Geração de relatórios de movimentação** (em desenvolvimento): Análises sobre entradas e saídas de produtos.
- **Alertas para produtos com baixo estoque e vencimento próximo** (em desenvolvimento): Notificações para evitar perdas e rupturas de estoque.
- **Interface responsiva** para acesso por desktop ou mobile (em desenvolvimento): Acesso flexível de qualquer dispositivo.
- **Backup automático diário** (em desenvolvimento): Segurança dos dados.
- **Histórico de alterações e rastreabilidade de ações** (em desenvolvimento): Auditoria completa das modificações no sistema.

---

### Rodar a API Localmente (para Desenvolvimento: usar Docker se não for desenvolver)

Se você preferir rodar a API diretamente em sua máquina para desenvolvimento, sem usar o `Docker` para a API em si:

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/YgorMartinsXx/ZenStock-Project.git](https://github.com/YgorMartinsXx/ZenStock-Project.git)
    cd Zenstock-Project
    ```

2.  **Instale as Dependências Python:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure as Variáveis de Ambiente:**
    Edite o arquivo `.env` na raiz do projeto com as informações de conexão ao MySQL.
    ```dotenv
    USUARIO=root
    SENHA=senha_segura
    HOST=127.0.0.1 # Se o MySQL estiver localmente, use 127.0.0.1 ou localhost, ou docker.host.internal para container Docker
    PORTA_MYSQL=3306
    BANCO_DE_DADOS=ZenStock
    ```
    **Importante**: `SENHA=senha_segura` deve ser a senha real do seu MySQL.

4.  **Inicie a Aplicação Flask:**
    ```bash
    flask run
    ```
    A API estará disponível em `http://127.0.0.1:5000/`.
    A documentação Flask + Swagger estará em `http://127.0.0.1:5000/apidocs/`

---

## Como Instalar e Rodar na sua Máquina (Docker: Altamente recomendável)

### Pré-requisitos

Certifique-se de ter o **Docker** instalado em sua máquina. Para instruções de instalação, visite o [site oficial do Docker](https://docs.docker.com/get-docker/).

### Configuração do Banco de Dados MySQL

A API ZenStock precisa de um banco de dados MySQL para funcionar. Você deve ter uma instância do MySQL rodando e acessível antes de iniciar a API.

Você pode:

1.  **Rodar um container MySQL com Docker (Recomendado):**
    Esta é a forma mais simples de garantir que o banco de dados esteja disponível e configurado corretamente.
    ```bash
    docker run -d \
      --name zenstock_mysql \
      -p 3306:3306 \
      -e MYSQL_ROOT_PASSWORD=senha_segura \
      -e MYSQL_DATABASE=ZenStock \
      mysql:8.0 # Ou a versão que você prefere, como mysql:latest
    ```
    * **`--name zenstock_mysql`**: Define um nome fácil de identificar para o container do MySQL.
    * **`-p 3306:3306`**: Mapeia a porta 3306 do seu host para a porta 3306 dentro do container MySQL.
    * **`-e MYSQL_ROOT_PASSWORD=senha_segura`**: Define a senha para o usuário `root` do MySQL. **Altere `senha_segura` para uma senha forte e segura!**
    * **`-e MYSQL_DATABASE=ZenStock`**: Cria um banco de dados chamado `ZenStock` automaticamente na inicialização.
    
    **Observação**: O comando acima só funcionará no bash do `Linux`, porém se você estiver utilizando o Docker pelo `Windows`, é possível escrever o comando por extenso, mantendo a mesma lógica:

    ```shell
    docker run -d --name zenstock_mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=senha_segura -e MYSQL_DATABASE=ZenStock mysql:8.0 # escolha a versão pela tag, recomendável utilizar mysql:latest
    ```

2.  **Usar um MySQL local:**
    Se você já tem o MySQL instalado e rodando diretamente na sua máquina, certifique-se de que ele está acessível na porta 3306 e que o banco de dados `ZenStock` (ou o que você escolheu) exista, com um usuário (como `root`) e senha (`senha_segura`) configurados conforme os parâmetros do comando da API.

**Observação**: Se você estiver usando um servidor MySQL em nuvem, pule para a próxima etapa, e, além disso, certifique-se de que o mesmo está corretamente configurado para receber requisições de APIs externas.

### Iniciando a API ZenStock

Depois de garantir que o MySQL esteja rodando e acessível, você pode iniciar o container da API.

1.  **Execute o comando `docker run`:**
    ```bash
    docker run -d \
      -p 5000:5000 \
      --name zenstock-api-1.0.0 \
      -e USUARIO=root \
      -e SENHA=senha_segura \
      -e HOST=host.docker.internal \
      -e PORTA_MYSQL=3306 \
      -e BANCO_DE_DADOS=ZenStock \
      gabrielventurini/zenstock-project:1.0.0
    ```
    * **`-d`**: Roda o container em modo *detached* (em segundo plano).
    * **`-p 5000:5000`**: Mapeia a porta 5000 do seu host para a porta 5000 dentro do container da API, onde a API está rodando.
    * **`--name zenstock-api-1.0.0`**: Atribui um nome para o seu container da API, facilitando o gerenciamento.
    * **`-e USUARIO=root`, `-e SENHA=senha_segura`, `-e HOST=host.docker.internal`, `-e PORTA_MYSQL=3306`, `-e BANCO_DE_DADOS=ZenStock`**: Essas são as variáveis de ambiente que a API usa para se conectar ao banco de dados MySQL.
        * **IMPORTANTE**: O `HOST=host.docker.internal` permite que o container Docker acesse o MySQL rodando diretamente no seu *host* (máquina local). Se você rodou o MySQL em **outro container Docker** (como no passo 1 acima), o valor de `HOST` deve ser o nome do container do MySQL, por exemplo, `HOST=zenstock_mysql`.
        * **Atenção**: Certifique-se de que `SENHA=senha_segura` corresponda à senha real do seu usuário MySQL (`root` neste exemplo).
        * **Docker no Windows**: O comando acima não funcionará no terminal padrão do `Windows`, portanto será necessário utilizar a versão dele por extenso:
        ```shell
        docker run -d -p 5000:5000 --name zenstock-api-1.0.0 -e USUARIO=root -e SENHA=senha_segura -e HOST=host.docker.internal -e PORTA_MYSQL=3306 -e BANCO_DE_DADOS=ZenStock gabrielventurini/zenstock-project:1.0.0
        ```

2.  **Verifique se o container da API está rodando:**
    ```bash
    docker ps
    ```
    Você deve ver o container `zenstock-api-1.0.0` listado com o status `Up`.

3.  **Acesse a API:**
    A API estará disponível em `http://localhost:5000`.

---

## Acessando a Documentação Interativa (Swagger UI)

Após iniciar a API, você pode explorar todos os endpoints, modelos de dados e testar as requisições diretamente pela interface do Swagger (Ainda incompleto). Acesse a documentação em:

`http://localhost:5000/apidocs/`

---

## Endpoints da API

Para uma lista completa e detalhada de todos os endpoints, com suas requisições, respostas e exemplos, consulte a **Documentação Interativa (Flask + Swagger)** no link `http://localhost:5000/apidocs/`.

Abaixo, um resumo dos principais recursos e suas operações básicas:

### Usuários (`/usuarios`)

| Método | Endpoint           | Descrição                                                                       | Requer Autenticação |
| :----- | :----------------- | :------------------------------------------------------------------------------ | :------------------ |
| `GET`  | `/{login_usuario}` | Obtém detalhes de um usuário específico pelo login (ex: `/usuarios/meu_login`). | Futuramente         |
| `POST` | `/`                | Cria um novo usuário.                                                           | Futuramente         |
| `DELETE`|`/{login_usuario}` | Exclui um usuário pelo login.                                                   | Futuramente         |
| `PUT`  | `/alterar_senha`   | Altera a senha de um usuário.                                                   | Futuramente         |
| `POST` | `/login`           | Realiza o login de um usuário e retorna tokens de autenticação.                 | Não                 |

### Produtos (`/produtos`)

| Método | Endpoint           | Descrição                                                                                                                                           | Requer Autenticação |
| :----- | :----------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| `GET`  | `/produtos`        | Busca produtos por categoria, ID (`cod_produto`), nome, preço (mínimo/máximo) ou retorna todos se `completo=true`. | Futuramente         |
| `DELETE`|`/produtos/{cod_produto}`| Deleta um produto pelo código.                                                                                                                      | Futuramente         |
| `PUT`  | `/produtos/{cod_produto}`| Edita informações de um produto existente (nome, categoria, descrição, preço unitário). | Futuramente         |
| `POST` | `/produtos`        | Cadastra um novo produto, incluindo código, nome, categoria, descrição, preço e quantidade. | Futuramente         |

### Pedidos (`/pedidos`)

| Método | Endpoint           | Descrição                                           | Requer Autenticação |
| :----- | :----------------- | :-------------------------------------------------- | :------------------ |
| `GET`  | `/`                | Lista todos os pedidos registrados.                 | Futuramente         |
| `GET`  | `/{id_pedido}`     | Obtém detalhes de um pedido específico por ID.      | Futuramente         |
| `POST` | `/`                | Cria um novo pedido, associando fornecedor, produto, quantidade e usuário. | Futuramente         |
| `DELETE`|`/excluir/{id_pedido}`| Exclui um pedido por ID.                            | Futuramente         |

### Movimentações (`/movimentacoes`)

| Método | Endpoint               | Descrição                                              | Requer Autenticação |
| :----- | :--------------------- | :----------------------------------------------------- | :------------------ |
| `GET`  | `/`                    | Lista todas as movimentações de estoque.               | Futuramente         |
| `GET`  | `/{id_movimentacao}`   | Obtém detalhes de uma movimentação específica por ID.  | Futuramente         |
| `GET`  | `/produto/{cod_produto}`| Lista movimentações associadas a um produto específico.| Futuramente         |
| `GET`  | `/usuario/{usuario}`   | Lista movimentações realizadas por um usuário específico.| Futuramente         |
| `POST` | `/`                    | Registra uma nova movimentação de estoque.             | Futuramente         |
| `PUT`  | `/{id_movimentacao}`   | Atualiza as informações de uma movimentação existente. | Futuramente         |
| `DELETE`|`/{id_movimentacao}`   | Exclui uma movimentação por ID.                        | Futuramente         |

### Fornecedores (`/fornecedores`)

| Método | Endpoint           | Descrição                                          | Requer Autenticação |
| :----- | :----------------- | :------------------------------------------------- | :------------------ |
| `GET`  | `/`                | Lista todos os fornecedores cadastrados.           | Futuramente         |
| `GET`  | `/{cnpj}`          | Obtém detalhes de um fornecedor específico por CNPJ. | Futuramente         |
| `POST` | `/`                | Cria um novo fornecedor.                           | Futuramente         |
| `PUT`  | `/{cnpj}`          | Atualiza as informações de um fornecedor existente por CNPJ.| Futuramente         |
| `DELETE`|`/{cnpj}`          | Exclui um fornecedor por CNPJ.                     | Futuramente         |

### Fornece (`/fornecimento`)

| Método | Endpoint                 | Descrição                                                      | Requer Autenticação |
| :----- | :----------------------- | :------------------------------------------------------------- | :------------------ |
| `GET`  | `/`                      | Lista todas as relações de fornecimento (pedidos de fornecimento). | Futuramente         |
| `GET`  | `/{id_pedido}`           | Obtém detalhes de uma relação de fornecimento específica por ID de pedido. | Futuramente         |
| `GET`  | `/produto/{codigo_produto}`| Lista relações de fornecimento associadas a um produto específico. | Futuramente         |
| `GET`  | `/fornecedor/{cnpj_fornecedor}`| Lista relações de fornecimento associadas a um fornecedor específico. | Futuramente         |
| `DELETE`|`/{id_pedido}`           | Exclui uma relação de fornecimento por ID de pedido.         | Futuramente         |
| `PUT`  | `/{id_pedido}`           | Edita uma relação de fornecimento existente.                   | Futuramente         |


---

## Créditos

* [Bruno Almeida](https://github.com/Brunoalmeida-alt)
* [Gabriel Venturini](https://github.com/Gabriel-Venturini)
* [Ygor Martins](https://github.com/YgorMartinsXx)

<h3 align="center"><a href="https://www.impacta.edu.br">Faculdade Impacta de Tecnologia</a></h3>