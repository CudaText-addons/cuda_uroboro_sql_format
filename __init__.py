import sys
import os
import re
import json
from . import format_proc

sys.path.append(os.path.dirname(__file__))
import uroborosqlfmt
from uroborosqlfmt.config import LocalConfig
from uroborosqlfmt.commentsyntax import Doma2CommentSyntax

format_proc.MSG = '[uroboroSQL Format] '
format_proc.INI = 'cuda_uroboro_sql_format.json'

def get_ops():
    fn = format_proc.ini_filename()
    if os.path.isfile(fn):
        s = open(fn, 'r').read()
        #del // comments
        s = re.sub(r'(^|[^:])//.*'  , r'\1', s)
        d = json.loads(s)
    else:
        d = {}

    config = LocalConfig()
    config.set_uppercase(d.get("uf_uppercase", True))
    uroborosqlfmt.config.glb.escape_sequence_u005c = d.get("uf_escapesequence_u005c", False)
    if d.get("uf_comment_syntax", "uroboroSQL").upper() == "DOMA2":
        config.set_commentsyntax(Doma2CommentSyntax())

    tab_config = {}
    tab_config["size"] = d.get("uf_tab_size", 4)
    tab_config["spaces"] = d.get("uf_translate_tabs_to_spaces", True)

    return config, tab_config


def do_format(text):
    op, op_tab = get_ops()
    text = uroborosqlfmt.format_sql(text, op)
    if op_tab["spaces"]:
        text = text.replace('\t', ' ' * op_tab["size"])
    return text


class Command:
    def config_global(self):
        format_proc.config_global()

    def config_local(self):
        format_proc.config_local()

    def run(self):
        format_proc.run(do_format)
