Структура данных.

Таблица серверов: servers, состоит из полей (srv_id, srv_name).

Таблица накопителей серверов: server_hdd, состоит из полей (hdd_id (integer), srv_id (integer),
hdd_name, hdd_capacity (Общая емкость диска - number)).

Таблица использования накопителей серверов hdd_monitoring (hdd_id, used_space (занятая емкость -
number), formatted_space (Форматированная емкость - number), monitoring_date (date)).
Накопителей может быть больше одного.

Таблицы (servers и server_hdd) связаны посредством foreign_key по полю srv_id.

Таблицы (server_hdd и hdd_monitoring) связаны посредством foreign_key по полю hdd_id.
Задания.


1
Вывести серверы, суммарная емкость накопителей которых больше 110 ТБ и менее 130 ТБ. Без
использования подзапросов.

2
Вследствие ошибки в таблице server_hdd появились дубли строк.
Предложите вариант удаления дубликатов, оставив только уникальные строки.

3
Какими средствами СУБД Oracle Вы в дальнейшем предотвратили бы появления дубликатов строк?

4
Вывести изменение занятой емкости на самых больших дисках каждого сервера в формате:
Имя сервера, Имя диска, Общая емкость диска, Предыдущая занятая емкость, Текущая емкость диска,
Дата мониторинга.
Не более 10 строк на каждый диск.


Тестовое задание python:

Написать скрипт получения температуры по городам.
Для получения температуры использовать https://openweathermap.org/api
В файле city.json должен содержаться список городов (5-10).
Результатом работы скрипта должны быть 2 выходных файла:
- файл с данными температуры по городам в формате Excel.
- файл с логами работы скрипта.
Данные должны содержать:
текущую температуру, минимальную температуру, максимальную температуру, давление,
влажность, скорость ветра.
температура должна быть в градусах по Цельсию.
