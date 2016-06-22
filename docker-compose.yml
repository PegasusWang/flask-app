web:
    restart: always
    build: .
    command: /usr/local/bin/gunicorn -w4 -b0.0.0.0:5000 webapp.app:app --chdir /flask-app/webapp
    ports:
        - "5000:5000"
    volumes:
        - .:/flask-app
    links:
        - mongo
        - redis
        - mysql
    hostname: myappserver

mongo:
    image: mongo:3.0.2

redis:
    image: redis

mysql:
  hostname: mysqlserver
  image: orchardup/mysql
  environment:
     MYSQL_ROOT_PASSWORD: p@ssw0rd123
     MYSQL_DATABASE: wordpress
