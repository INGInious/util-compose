import sys
import os

from yaml import load, BaseLoader

from jinja2 import FileSystemLoader, Environment, select_autoescape

def usage() -> str:
    return """Usage: <context> <compose>
context: path to the context
compose: output path for the compose file
    """

if len(sys.argv) != 3:
    print(usage())
    exit(1)

context = sys.argv[1]
if not os.path.exists(context) or not os.path.isfile(context):
    print("Context file not found.")
    exit(1)
compose = sys.argv[2]

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape(), trim_blocks=True, lstrip_blocks=True)
template = env.get_template("compose.tmpl")

with open(context, "r") as fd:
    context = load(fd, BaseLoader)

with open(compose, "w") as fd:
    fd.write(template.render(context))
