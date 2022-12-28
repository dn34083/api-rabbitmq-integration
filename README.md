#Api para envio de objetos para filas do rabbitMQ.



**Executar o projeto**

  - docker build -t api-rabbitmq-integration:tag
  - run --name api-rabbitmq-integration -p 5000:5000 -d api-rabbitmq-integration:tag



**Exemplo de curl:** 
``` 
curl --location --request POST 'http://127.0.0.1:5000/rabbit/post/nome_arquivo' \
--header 'host: $hostRabbitMQ' \
--header 'user: $Usuario' \
--header 'password: $Senha' \
--header 'vh: $VirtualHost' \
--header 'queue: $NomeDaFila' \
--header 'Content-Type: text/plain' \
--data-binary '$arquivoComObjetos' 
```

![Postman print headers](/anexos/postman2.png)

![Postman print body file](/anexos/postman1.png)

