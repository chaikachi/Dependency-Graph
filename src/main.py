import argparse
import sys

def verify(args):
    if args.name.strip()=="":
        sys.exit("Пустое имя")
    if args.url.strip()=="":
        sys.exit("Пустой адрес")
    if args.depth<=0:
        sys.exit("Недопустимая глубина")
        
def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', type=str)
    parser.add_argument('url', type=str)
    parser.add_argument('test', type=str)
    parser.add_argument('version', type=str)
    parser.add_argument('depth', type=int)
    parser.add_argument('filter', type=str)
    return parser.parse_args()

def start():
    args=parser()
    verify(args)
    print(f"Имя пакета: {args.name}")
    print(f"Адрес/путь пакета: {args.url}")
    print(f"Тестовый режим: {args.test}")
    print(f"Версия пакета: {args.version}")
    print(f"Глубина анализа зависимостей: {args.depth}")
    print(f"Подстрока для фильтрации: {args.filter}")

if __name__ == "__main__":
    start()
