import argparse
import sys
import urllib.request
import json
import webbrowser

visited = set()
traversal_order = []
res_graph = {}

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

def get_dependencies(arg, name, version = None):
    c_url = arg.url.rstrip("/")
    if not version:
        n_url = f"{c_url}/api/v1/crates/{name}"
        res = urllib.request.Request(n_url)
        with urllib.request.urlopen(res) as req:
            b_tx = req.read().decode("utf-8")
            loaded_file = json.loads(b_tx)
            version = loaded_file['crate']['max_version']
    full_url = f"{c_url}/api/v1/crates/{name}/{version}/dependencies"
    res = urllib.request.Request(full_url)
    with urllib.request.urlopen(res) as req:
        b_tx = req.read().decode("utf-8")
        loaded_file = json.loads(b_tx)
        deps = []
        for dep in loaded_file.get('dependencies',[]):
            deps.append((dep['crate_id'], dep['req']))
        return deps

def reverse_dependencies(arg, name, version = None):
    c_url = arg.url.rstrip("/")
    full_url = f"{c_url}/api/v1/crates/{name}/reverse_dependencies"
    res = urllib.request.Request(full_url)
    with urllib.request.urlopen(res) as req:
        b_tx = req.read().decode("utf-8")
        loaded_file = json.loads(b_tx)
        deps = []
        for dep in loaded_file.get('versions',[]):
            deps.append((dep['crate'], dep['req']))
        return deps

def test_mode(args):
    graph = {}
    with open(args.url, "r") as r:
        for line in r:
            c_line = line.strip()
            cols = [col.strip() for col in c_line.split(":")]
            name = cols[0]
            if cols[1] == "":
                deps = []
            else:
                deps = []
                n_deps = cols[1].split(",")
                for s in n_deps:
                    s = s.strip()
                    deps.append(s)
            graph[name] = deps
    return graph

def reverse_graph(graph):
    rev_graph = {}
    for parent, children in graph.items():
        for child in children:
            if child not in rev_graph:
                rev_graph[child] = []
            rev_graph[child].append(parent)
    return rev_graph

def dfs(node, graph, depth, args, version = None):
    if depth >= args.depth:
        return
    if node in visited:
        return
    res_graph[node] = []
    visited.add(node)
    traversal_order.append(node)
    if args.test:
        neighbors = graph.get(node, [])
    else:
        neighbors = get_dependencies(args, node, version)
    for name, req in neighbors:
        if args.filter and args.filter in name:
            continue
        res_graph[node].append((name, req))
        dfs(name, graph, depth+1, args)

def print_graph():
    for pkg, deps in res_graph.items():
        if deps:
            print(f"{pkg} -> {', '.join(deps)}")
        else:
            print(f"{pkg} ->")

def plantuml():
    lines = ["@startuml"]
    for parent, deps in res_graph.items():
        if deps:
            deps = set(deps)
            for name, req in deps:
                lines.append(f'[{parent}] --> [{name}] : "{req}"')
        else:
            lines.append(f"[{parent}]")
    lines.append("@enduml")
    plantuml_text = "\n".join(lines)
    print(plantuml_text)
    e_tx = plantuml_text.encode('utf-8').hex()
    url = f"http://plantuml.com/plantuml/png/~h{e_tx}"
    webbrowser.open(url)

def start():
    args=parser()
    verify(args)
    if args.test:
        graph = test_mode(args)
    else:
        graph = {}
    dfs(args.name, graph, 0, args, args.version)
    plantuml()

if __name__ == "__main__":
    start()
