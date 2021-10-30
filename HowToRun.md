Zeby odpalic projekt trzeba najpierw zrobic:
Miec folder db-dump i w nim plik backup.sql, pozniej w terminalu:
sudo docker-compose up
i odpalic polecenia z "Stworzenie db dumpa"


Stworzenie db dumpa:

sudo cat db-dumps/backup.sql | sudo docker exec -i presta_lamps_db_1 /usr/bin/mysql -u root --password=prestashop prestashop


Inicjacja obecnego db dumpa:

sudo docker exec presta_lamps_db_1 /usr/bin/mysqldump -u root --password=prestashop prestashop > db-dumps/backup.sql

MOZE DA SIE TO ROBIC AUTOMATYCZNIE ALE NWM NA RAZIE JAK

