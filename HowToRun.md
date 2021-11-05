Zeby odpalic projekt trzeba najpierw pobrac projekt z githuba, nastepnie na folderze z plikami
z githuba wpisac:
sudo chmod +777 ./ -R
Co da odpowiednie prawa wszystkim plikom.
Majac folder db-dumps i w nim plik backup.sql oraz reszte mozecie wpisac:
sudo docker-compose up 
i poczekajcie az beda ostatnie komunikaty od presty wtedy powinna na localhost:8080
byc presta z polskim tlumaczeniem i polska waluta.


Stworzenie db dumpa dla basha (NIE TRZEBA TEGO WPISYWAC):

sudo docker exec presta_lamps_db_1 /usr/bin/mysqldump -u root --password=prestashop prestashop > db-dumps/backup.sql

MOZE DA SIE TO ROBIC AUTOMATYCZNIE ALE NWM NA RAZIE JAK




CHYBA NIEPOTRZEBNE

Juz nwm co to robi juz:

sudo cat db-dumps/backup.sql | sudo docker exec -i presta_lamps_db_1 /usr/bin/mysql -u root --password=prestashop prestashop
