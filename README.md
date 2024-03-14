# Code-exercise
## 🤔Sobre
Essa API demonstra o funcionamento dos métodos GET e POST a partir de uma requisição de estado de saúde e um programa em pyhton que calcula e mostra a sequência de fibonacci de duas formas:
- Um número n é dado pelo cliente, se for um valor de fibonacci, é devolvido toda a sequência até aquele número, se não for, ele devolve um erro;
- Um número n é dado pelo cliente, e são gerados os n valores da sequência.

## 📑Temas abordados
- Python;
- API REST;
- Requisições GET e POST;
- Docker.

##  🔎Sobre a imagem
A fim de utilizar o recurso em container, foi feito a seguinte imagem:
- FROM: indica uma imagem, que será utilizada como base para a aplicação;
- WORKDIR: indica um diretório para ser usado dentro do container (usr/src/myApp);
- COPY: copia determinados arquivos para dentro do container, na pasta criada no workdir;
- RUN: instalar as bibliotecas necessárias para a aplicação;
- EXPOSE: abre a porta 8000 do container;
- CMD: terminando as instalações e preparação, rodar a aplicação usando o uvicorn localmente na porta 8000;

## ⚙️Como rodar
Para rodar a aplicação, seguir os seguintes passos:
- Se já não tiver, baixar o Docker Desktop para rodar o container (https://www.docker.com/products/docker-desktop/);
- Clonar o repositório;
- Utilizar o comando "docker build -t [nome_da_sua_imagem] . -f code.dockerfile" em um terminal para criar a imagem;
- Depois utilizar "docker run -d --name [nome_do_seu_container] -p 8000:8000 [nome_da_sua_imagem]";
- Pronto! Agora você pode testar as requisições GET pelo browser "localhost:8000" e "localhost:8000/health", para testar a requisição POST use um REST API Client, como Thunder Client (https://www.thunderclient.com) ou Postman (https://www.postman.com).
