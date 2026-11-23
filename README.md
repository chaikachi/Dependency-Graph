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
[rand] --> [rand_core] : "^0.10.0"
[rand] --> [getrandom] : "^0.4.0"
[rand] --> [postcard] : "^1.1.3"
[rand] --> [chacha20] : "^0.10.0"
[rand] --> [serde_json] : "^1.0.140"
[rand] --> [rayon] : "^1.7"
[rand] --> [serde] : "^1.0.103"
[rand] --> [rand_pcg] : "^0.10"
@enduml
```
Визуализация в формате PNG:

<img width="1079" height="189" alt="rand_dependencies_w_version" src="https://github.com/user-attachments/assets/503dbddf-dc2f-4e38-b4e1-c4a0764009e0" />

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
[anstyle] --> [snapbox] : "^0.6.23"
[anstyle] --> [lexopt] : "^0.3.1"
[lexopt]
[snapbox] --> [document-features] : "^0.2.12"
[snapbox] --> [similar] : "^3.0.0"
[snapbox] --> [backtrace] : "^0.3"
[snapbox] --> [anstyle-svg] : "^1.1.0"
[snapbox] --> [anstream] : "^1.0.0"
[snapbox] --> [walkdir] : "^2.5.0"
[snapbox] --> [normalize-line-endings] : "^0.3.0"
[snapbox] --> [serde_json] : "^1.0.149"
[snapbox] --> [tempfile] : "^3.27"
[snapbox] --> [regex] : "^1.12.3"
[snapbox] --> [snapbox-macros] : "^1.1.0"
[snapbox] --> [wait-timeout] : "^0.2.1"
[snapbox] --> [serde] : "^1.0.228"
[snapbox] --> [dunce] : "^1.0"
[snapbox] --> [automod] : "^1.0.16"
[snapbox] --> [content_inspector] : "^0.2.4"
[snapbox] --> [os_pipe] : "^1.2"
[snapbox] --> [libc] : "^0.2.183"
[snapbox] --> [filetime] : "^0.2.27"
[snapbox] --> [windows-sys] : "^0.61.2"
[snapbox] --> [escargot] : "^0.5.15"
[snapbox] --> [anstyle] : "^1.0.14"
@enduml
```
Визуализация в формате PNG:
<img width="3095" height="312" alt="anstyle_dependencies_w_versions" src="https://github.com/user-attachments/assets/7a1372de-26d9-4310-b120-7efeebf39a00" />
