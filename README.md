# Sobre o Desafio
Diferente do desenvolvimento do Front-end, na implementação do Back-end, encontrei sim dificuldades, porém não foram tantas, pois como já tenho um certo conhecimento em porgramação em Python e as tentativas e erros feitas no desenvolvimento do Front me ajudaram a ter conhecimento sobre dependêcias e entender um pouco melhor como um framework funciona. Com certeza me interessou muito mais a parte do Back-end, como dito antes, caso não consiga a bolsa, me interesso por ser voluntário.

Link do front-end: https://github.com/arturcavalcantej/implementacao-portal-patrimonio-com-angular

# Portal Patrimônio
Implementação do Desafio do LCCV baseado no Backlog Desafio disponibilizado no Google Classroom, logo abaixo segue o que foi 
possivel ser realizado(e também o que não foi possivel) no back-end, tendo em vista que não foi possivel fazer a integração de ambos.

# Implementação do Back-End
Seguindo o que foi disposto no DER - DIAGRAMA ENTIDADE-RELACIONAMENTO e no BACKLOG, a implementação do back-end utilizando Django e Django restframework foi realizada de forma completa todas as funcionaliades para o back-end tanto a configuração das entidades através de models,serializers e views, urls etc.

Foram implementadas de forma complementar: Swagger, authentication(JSON Web Token) e um encapsulamento de dados sensíveis.
# Swagger
Configurou-se a biblioteca do swagger para o django-restframework, que nos ajuda na testagem das APIs, essa ferramenta pode ser utilizada usando a url /swagger.

# JSON Web Token
Configurou-se a biblioteca do JSON Web Token para o django-restframework, onde é gerado um token a partir do login de um usuario já cadastrado, confirmando a veracidade desse usuário logado, podendo interagir com ela através do Swagger.

# Encapsulamento de dados sensíveis
Algumas informações sensíveis foram encapsuladas.
# Como executar
No terminal digite:
```
docker-compose --build
```
Após criado, digite:
```
docker-compose up
```
