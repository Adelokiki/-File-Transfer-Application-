# -File-Transfer-Application-
Клиент-серверное приложение для передачи файлов
Обзор
Этот проект реализует клиент-серверное приложение для передачи файлов с использованием протоколов TCP и UDP. Приложение позволяет пользователям отправлять и получать файлы любого типа, демонстрируя принципы клиент-серверной архитектуры и различия между протоколами TCP и UDP.
Содержание
•	Функции      
•	Используемые технологии
•	Установка
•	Использование
•	Протоколы передачи файлов
•	Тестирование
•	Участники
•	Лицензия
Функции
•	Передача файлов по TCP:
•	Клиент инициирует соединение с сервером и отправляет файлы.
•	Сервер принимает файлы, отображает информацию и сохраняет их локально.
•	Передача файлов по UDP:
•	Как клиент, так и сервер могут отправлять и получать файлы.
•	Информация о полученных файлах отображается, и файлы сохраняются локально.
•	Графический пользовательский интерфейс:
•	Простой GUI для взаимодействия с пользователем.
•	Асинхронные сокеты:
•	Использует неблокирующие сокеты для эффективной передачи файлов.
Используемые технологии
•	Python
•	Программирование сокетов
•	Tkinter (для GUI)
•	Git (для контроля версий)
Установка
1.	Клонируйте репозиторий:
bash
VerifyOpen In EditorRunCopy code
1git clone https://github.com/yourusername/file-transfer-app.git
2cd file-transfer-app
2.	Установите необходимые зависимости (если применимо):
bash
VerifyOpen In EditorRunCopy code
1pip install -r requirements.txt
Использование
Запуск TCP-сервера
1.	Откройте терминал и перейдите в каталог проекта.
2.	Запустите TCP-сервер:
bash
VerifyOpen In EditorRunCopy code
1python tcp_server.py
Запуск TCP-клиента
1.	Откройте другой терминал и перейдите в каталог проекта.
2.	Запустите TCP-клиента, указав файл для отправки:
bash
VerifyOpen In EditorRunCopy code
1python tcp_client.py path/to/your/file.txt
Запуск UDP-сервера
1.	Откройте терминал и перейдите в каталог проекта.
2.	Запустите UDP-сервер:
bash
VerifyOpen In EditorRunCopy code
1python udp_server.py
Запуск UDP-клиента
1.	Откройте другой терминал и перейдите в каталог проекта.
2.	Запустите UDP-клиента, указав файл для отправки:
bash
VerifyOpen In EditorRunCopy code
1python udp_client.py path/to/your/file.txt
Протоколы передачи файлов
Протокол TCP
•	Надежный, ориентированный на соединение протокол.
•	Гарантирует доставку пакетов в порядке их отправки.
•	Подходит для передачи файлов, где важна целостность данных.
Протокол UDP
•	Протокол без соединения.
•	Быстрее, чем TCP, но не гарантирует доставку или порядок.
•	Подходит для приложений, где скорость важнее надежности.
Тестирование
•	Убедитесь, что как сервер, так и клиентские приложения работают перед попыткой передачи файлов.
•	Протестируйте с различными типами и размерами файлов для проверки функциональности.
