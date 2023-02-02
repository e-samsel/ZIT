# ZIT

System monitorowania otwartych portów z funkcją porównania z wzrocowym zestawem i systemem powiadamiania


---------Biblioteki---------
Do monitorowania portów używana jest biblioteka socket. Dokumentacja biblioteki dostępna jest pod adresem:
https://docs.python.org/3/library/socket.html
Następnie użyte są biblioteki time i pyautogui w celu utworzenia alertu wyskakującego na ekran komputera z systemem operacyjnym dystrybucji Linux. Dokumentacje tych bibliotek dostępne są tu:
https://docs.python.org/3/library/time.html
https://pypi.org/project/PyAutoGUI/

W celu instalacji odpowiednich bibliotek możemy użyć narzędzia pip:
pip install <nazwa biblioteki>

---------Zewnętrzne pliki---------
Program importuje plik "ports.txt" w celu uzyskania listy portówm które powinny zostać zamknięte. To te porty są monitorowane przez program. Plik txt można dowolnie edytować, dodając lub odejmując wpisy, każdy oddzielając nową linią.


---------Działanie---------
Skrypt działa analizując co 10 sekund porty wymienione w pliku "ports.txt". Po uruchomieniu go użytkownik zostaje zapytany o adres hosta, którego chce skanować. Należy podać go w formacie X.X.X.X, gdzie poszczególne X zamieniamy kolejnymi oktetami adresu naszego hosta.

W momencie pojawienia się "Starting scan on host: X.X.X.X" program zaczyna skan. W momencie otworzenia się portu pojawi się alert bezpieczeństwa przedstawiony na obrazku alert.jpg
