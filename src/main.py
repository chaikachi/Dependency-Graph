import argparse
import sys
import urllib.request
import json

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

def get_dependencies(arg):
    c_url = arg.url.rstrip("/")
    full_url = f"{c_url}/api/v1/crates/{arg.name}/{arg.version}/dependencies"
    req = urllib.request.Request(full_url)
    with urllib.request.urlopen(req) as req:
        b_tx = req.read().decode("utf-8")
        loaded_file = json.loads(b_tx)
        for dep in loaded_file.get('dependencies',[]):
            print(dep['crate_id'])

def start():
    args=parser()
    verify(args)
    get_dependencies(args)

if __name__ == "__main__":
    start()
