FROM prestashop/prestashop:1.7

# WORKDIR /var/www/html

RUN rm -rf *

COPY volumes/presta/var/www/html/ ./

COPY ./docker/presta/ssl/localhost.crt /etc/ssl/certs/localhost.crt
COPY ./docker/presta/ssl/localhost.key /etc/ssl/private/localhost.key
ADD ./docker/presta/sites-available /etc/apache2/sites-available

RUN a2enmod rewrite
RUN a2enmod ssl
RUN a2ensite 001-ssl.conf

EXPOSE 80
EXPOSE 443
