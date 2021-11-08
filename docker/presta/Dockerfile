FROM prestashop/prestashop:1.7

COPY ./ssl/localhost.crt /etc/ssl/certs/localhost.crt
COPY ./ssl/localhost.key /etc/ssl/private/localhost.key
ADD ./sites-available /etc/apache2/sites-available

RUN a2enmod rewrite
RUN a2enmod ssl
RUN a2ensite 001-ssl.conf

EXPOSE 80
EXPOSE 443
