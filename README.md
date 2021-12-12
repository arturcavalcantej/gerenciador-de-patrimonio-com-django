# Portal Patrimônio
Implementação do Desafio do LCCV baseado no Backlog Desafio disponibilizado no Google Classroom, logo abaixo segue o que foi 
possivel ser realizado(e também o que não foi possivel) no back-end, tendo em vista que não foi possivel fazer a integração de ambos.

# Implementação do Back-End
Seguindo o que foi disposto no DER - DIAGRAMA ENTIDADE-RELACIONAMENTO e no BACKLOG, a implementação do back-end utilizando Django foi realizada de forma completa
todas as funcionaliades para o back-end tanto a configuraçao das entidades através de models,como tambem a cconfiguraçao dos mesmo pelo Django REST FRAMEWORK

Foram utilizados na implementação do django rest-framework: swagger, encapsulamento de dados sensiveis e authentication(JSON Web Token).
# Swagger
Configurou-se a biblioteca do swagger para o django-restframework, que nos ajuda na testagem de api, essa ferramenta pode ser utilizada usando a url swagger.

# JSON Web Token
Configurou-se a biblioteca do JSON Web Token para o django-restframework, onde é gerado um token a partir do login de um usuario já cadastrado, confirmando a veracidade desse usuario logado, podendo interagir com ela através do Swagger.
# Encapsulamento de dados sensiveis
Algumas informaçoes sensiveis foram encapsuladas.
# Como executar
No terminal digite:
```
docker-compose up
```
