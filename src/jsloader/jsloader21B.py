# -*- coding: utf-8 -*-
# Copyright 2019-2020 Lovac42
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Support: https://github.com/lovac42/JSLoader


import aqt
from aqt import gui_hooks
from aqt import mw

from .const import MOD_DIR, BYPASS_TAG_PROTECTION
from .utils import addonBundlePath


def injector(web_content, context):
    if not isinstance(context, aqt.reviewer.Reviewer):
        return
    tags=mw.reviewer.card.note().tags
    if BYPASS_TAG_PROTECTION or "pgnchess" in tags:
        web_content.js.append( addonBundlePath(MOD_DIR, "/pgnchess/pgnyui.js") )
        web_content.js.append( addonBundlePath(MOD_DIR, "/pgnchess/pgnviewer.js") )
        web_content.css.append( addonBundlePath(MOD_DIR, "/pgnchess/board-min.css") )


    # List other injections here:
    # ===================================
    # if BYPASS_TAG_PROTECTION or "xxxxx" in tags:
        # web_content.js.append( addonBundlePath(MOD_DIR, "/xxxxx/script.js") )


# ===== EXEC ===========
gui_hooks.webview_will_set_content.append(injector)
