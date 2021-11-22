Zeby odpalic projekt trzeba najpierw pobrac projekt z githuba, nastepnie na folderze z plikami
z githuba zmienic permisje:
sudo chmod +322 ./ -R
Co da odpowiednie prawa wszystkim plikom.
Aby potem było to automatycznie wykonwywane zmień konfigurację tego repozytorium:
git config core.sharedRepository 0666

Majac folder db-dumps i w nim plik backup.sql oraz reszte mozecie wpisac:
sudo docker-compose up 
i poczekajcie az beda ostatnie komunikaty od presty wtedy powinna na localhost:8080
byc presta z polskim tlumaczeniem i polska waluta.


Stworzenie db dumpa dla basha:

sudo docker exec presta_lamps_db_1 /usr/bin/mysqldump -u root --password=prestashop prestashop > db-dumps/backup.sql


W install-chromedriver.sh jest pobieranie i rozpakowanie chromedrivera dla Chrome w wersji 96.0.4664.45 (jesli chcecie zainstalowac starsza wersje np. 95.0.4638.69 to zmiencie nazwe w install-chromedriver na opowiednia wersje), ktory pozwala na odpalenie skryptow importujacego i testujacego. Wystarczy po pobraniu projektu z GitHuba wykonac ./install-chromedriver.sh i sie pojawi w folderze seleniumDriver. Jesli to nie wystarczy mozliwe ze wystarczy dodac wczesniej sed -i -e 's/\r$//' install-chromedriver.sh.




Przywracanie db dumpa:

sudo cat db-dumps/backup.sql | sudo docker exec -i presta_lamps_db_1 /usr/bin/mysql -u root --password=prestashop prestashop
