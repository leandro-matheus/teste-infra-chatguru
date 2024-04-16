# teste-infra-chatguru
Teste de Infra passado pelo Eduardo Azevedo.

Aplicar conhecimentos de git e docker executando o código de app anexado. 

[app.zip](https://prod-files-secure.s3.us-west-2.amazonaws.com/b30e4ae0-077c-402e-a461-1e9261713f91/62538a82-13fe-4e13-ab00-dfa2dcbdc34d/app.zip)

1ª etapa

- Iniciar um repositório git.
- Setar duas branches, main(default) e development.
- Na branch development, iniciar a dockerização da aplicação.

2ª etapa

- Para dockerização da aplicação, criar dois arquivos: Dockerfile e docker-compose.yml
- Os arquivos da app devem ser mantidos em um diretório, fora da raiz onde estão os arquivos docker.
- Os arquivos da app devem ser copiados para a imagem docker.
- A app é executada com o comando: `flask --app server run --host=0.0.0.0`
- A app precisa que a porta 5000 seja exposta na configuração do docker.
- A app precisa de três bibliotecas python, que devem ser descobertas e instaladas no arquivo Dockerfile.
- Para execução da app, dever ser necessário apenas executar: `docker-compose up`

3ª etapa

- Após a dockerização da app na branch development, a variável "message" deve ser alterada e o código commitado e mergeado para a branch main.
- Depois, na branch development a variável deve ser alterada e commitada novamente.
- A variável "message" deve estar diferente nas branches main e development.
