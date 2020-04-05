# -*- coding: utf-8 -*-
# Copyright 2019-2020 Lovac42
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Support: https://github.com/lovac42/JSLoader


import aqt
from aqt import gui_hooks
from aqt import mw

from .const import MOD_DIR, ADDON_NAME
from .config import Config
from .utils import addonBundlePath


conf = Config(ADDON_NAME)


def injector(web_content, context):
    if not isinstance(context, aqt.reviewer.Reviewer):
        return
    tags=mw.reviewer.card.note().tags
    bypass = conf.get("bypass_tag_protection", False)
    if bypass or "pgnchess" in tags:
        web_content.js.append( addonBundlePath(MOD_DIR, "/pgnchess/pgnyui.js") )
        web_content.js.append( addonBundlePath(MOD_DIR, "/pgnchess/pgnviewer.js") )
        web_content.css.append( addonBundlePath(MOD_DIR, "/pgnchess/board-min.css") )


    # List other injections here:
    # ===================================
    # if bypass or "xxxxx" in tags:
        # web_content.js.append( addonBundlePath(MOD_DIR, "/xxxxx/script.js") )


# ===== EXEC ===========
gui_hooks.webview_will_set_content.append(injector)
