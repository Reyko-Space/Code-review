# Code-review
## Temas abordados
- Python
- API REST
- Requisições GET e POST (testes com Thunder Client)
- Docker

## Como rodar
Para rodar a aplicação, seguir os seguintes passos:
- Se já não tiver, baixar o Docker Desktop para rodar o container (https://www.docker.com/products/docker-desktop/);
- Baixar/Dar pull no projeto;
- Abrir a pasta baixada e selecionar o arquivo "code.dockerfile";
- Abrir um terminal;
- Utilizar o comando "docker build -t [nome_da_sua_imagem] . -f code.dockerfile" para criar a imagem;
- Depois utilizar "docker run -d --name [nome_do_seu_container] -p 8000:8000 [nome_da_sua_imagem]";
- Pronto! Agora você pode testar as requisições GET pelo browser "localhost:8000" e "localhost:8000/health", para testar a requisição POST use um REST API Client, como Thunder Client (https://www.thunderclient.com) ou Postman (https://www.postman.com).
