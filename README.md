# Sobre o Desafio parte 2
Diferente do desenvolvimento do Front-end, na implementação do Back-end, encontrei sim dificuldades, porém não foram tantas, pois como já tenho um certo conhecimento em porgramação em Python e as tentativas e erros feitas no desenvolvimento do Front me ajudarão a ter conhecimento sobre dependêcias e entender um pouco melhor como um framework funciona. Com certeza me interessou muito mais a parte do Back-end, como dito antes, caso não consiga a bolsa, me interesso por ser voluntário.

# Portal Patrimônio
Implementação do Desafio do LCCV baseado no Backlog Desafio disponibilizado no Google Classroom, logo abaixo segue o que foi 
possivel ser realizado(e também o que não foi possivel) no back-end, tendo em vista que não foi possivel fazer a integração de ambos.

# Implementação do Back-End
Seguindo o que foi disposto no DER - DIAGRAMA ENTIDADE-RELACIONAMENTO e no BACKLOG, a implementação do back-end utilizando Django foi realizada de forma completa
todas as funcionaliades para o back-end tanto a configuração das entidades através de models,como tambem a cconfiguração dos mesmo pelo Django REST FRAMEWORK

Foram implementadas de forma complementar: Swagger, authentication(JSON Web Token) e um encapsulamento de dados sensiveis.
# Swagger
Configurou-se a biblioteca do swagger para o django-restframework, que nos ajuda na testagem das APIs, essa ferramenta pode ser utilizada usando a url /swagger.

# JSON Web Token
Configurou-se a biblioteca do JSON Web Token para o django-restframework, onde é gerado um token a partir do login de um usuario já cadastrado, confirmando a veracidade desse usuario logado, podendo interagir com ela através do Swagger.

# Encapsulamento de dados sensiveis
Algumas informaçoes sensiveis foram encapsuladas.
# Como executar
No terminal digite:
```
docker-compose --build
```
Após criado, digite:
```
docker-compose up
```
