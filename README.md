# Dependency-Graph
Практическая работа 2, вариант 29 ИКБО-23-25

## Общее описание

Программа для визуализации графа зависимостей на языке диаграмм PlantUML для менеджера пакетов с форматом Rust (Cargo).

## Описание функций и настроек

Для запуска программы необходимо передать следующие параметры:
* имя пакета.
* URL-адрес в формате https:// или путь к тестовому скрипту.
* тестовый режим для работы с текстовым файлом (если не требуется - "").
* версия пакета.
* глубина анализа зависимостей (целое число, не может быть меньше 1).
* фильтр для исключения пакетов из анализа (название исключаемого пакета).

## Описание команд для сборки проекта и запуска тестов

Структура текстового файла:
```text
A: B, C, D, E
B: D, E
C: D
D: E
E:
```
Команда запуска тестового режима:
```bash
python ../src/main.py A script1.txt 1 "" 1 ""
```
## Примеры использования
1. Визуализация графа зависимостей пакета rand

Запуск программы:
```bash
python ../src/main.py rand https://crates.io "" 0.10.3 1 ""
```
Результат работы программы:
```plantuml
@startuml
[rand] --> [rand_pcg]
[rand] --> [chacha20]
[rand] --> [rayon]
[rand] --> [serde]
[rand] --> [serde_json]
[rand] --> [getrandom]
[rand] --> [postcard]
[rand] --> [rand_core]
@enduml
```
Визуализация в формате PNG:

<img width="1079" height="172" alt="rand_dependencies" src="https://github.com/user-attachments/assets/05ec25a2-4b78-471c-b8f7-411f8cdbf6fc" />
<br>

2. Визуализация графа зависимостей из текстового файла с исключением пакета

Содержимое текстового файла:
```text
A: B, C, D, E
B: D, E
C: D
D: E
E:
```
Запуск программы:
```bash
python ../src/main.py A script2.txt 1 0 3 E
```
Результат работы программы:
```plantuml
@startuml
[A] --> [D]
[A] --> [C]
[A] --> [B]
[B] --> [D]
[D]
[C] --> [D]
@enduml
```
Визуализация в формате PNG:
<br>
<img width="175" height="278" alt="test_dependencies" src="https://github.com/user-attachments/assets/de862269-7fbd-43a0-a0bd-10ef1382b3ea" />
<br>
3. Визуализация графа зависимостей пакета anstyle

Запуск программы:
```bash
python ../src/main.py anstyle https://crates.io/ "" 1.0.14 2 ""
```
Результат работы программы:
```plantuml
@startuml
[anstyle] --> [snapbox]
[anstyle] --> [lexopt]
[lexopt]
[snapbox] --> [escargot]
[snapbox] --> [walkdir]
[snapbox] --> [os_pipe]
[snapbox] --> [serde]
[snapbox] --> [automod]
[snapbox] --> [anstyle]
[snapbox] --> [snapbox-macros]
[snapbox] --> [wait-timeout]
[snapbox] --> [anstream]
[snapbox] --> [document-features]
[snapbox] --> [anstyle-svg]
[snapbox] --> [regex]
[snapbox] --> [windows-sys]
[snapbox] --> [backtrace]
[snapbox] --> [content_inspector]
[snapbox] --> [similar]
[snapbox] --> [filetime]
[snapbox] --> [serde_json]
[snapbox] --> [libc]
[snapbox] --> [normalize-line-endings]
[snapbox] --> [dunce]
[snapbox] --> [tempfile]
@enduml
```
Визуализация в формате PNG:
<img width="3094" height="280" alt="anstyle_dependencies" src="https://github.com/user-attachments/assets/abbdde43-15a0-43ce-9fac-591eb6c0ae39" />
