FROM mariadb:10.3

ENV MYSQL_DATABASE='web-news-adm'
ENV MYSQL_ROOT_PASSWORD='12345'
EXPOSE 3306

VOLUME [ "/data" ]