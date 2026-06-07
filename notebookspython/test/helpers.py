import importlib.util
import pathlib


ROOT = pathlib.Path(__file__).resolve().parents[1]


def load_py(filename: str, module_name: str):
    path = ROOT / filename
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def linked_values(head):
    values = []
    while head:
        values.append(head.val)
        head = head.next
    return values
