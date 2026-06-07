import importlib.util
import json
import pathlib
import types


ROOT = pathlib.Path(__file__).resolve().parents[1]


def load_py(filename: str, module_name: str):
    path = ROOT / filename
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_ipynb(filename: str, module_name: str):
    path = ROOT / filename
    module = types.ModuleType(module_name)
    module.__file__ = str(path)
    data = json.loads(path.read_text(encoding="utf-8"))

    for cell in data["cells"]:
        if cell.get("cell_type") == "code":
            exec("".join(cell.get("source", [])), module.__dict__)

    return module


def linked_values(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values
