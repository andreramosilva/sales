Created By: Andre Ramos da Silva

Docker compose com version 5.7 do MySQL e o Adminer

startging, creating img and etc: docker-compose up -d

confirming a network  mysql: docker network ls

confirming activation mysql (porta 3306) and Adminer (porta 8080): docker-compose ps

preparing  mysql server

Via Adminer

Go to http://localhost:8080 or http://127.0.0.1:8080 and fill the credential. User: root


password: rootpassword

on the left go to import (importar), select the file o arquivo "bd.sql" and click on excute (executar).

your database will be ready with the 5 sellers already in there.

you can just run the main file and use the instructions on the screen to navegate.

we have a couple basic functions(show ranking of sales and register new sale)
