# -*- coding: utf-8 -*-
# Copyright 2019-2020 Lovac42
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Support: https://github.com/lovac42/JSLoader


from anki.hooks import wrap
from aqt.webview import AnkiWebView
from aqt import mw

from .utils import *
from .const import MOD_DIR, BYPASS_TAG_PROTECTION


def getHeads(tags):
    js=[]
    if BYPASS_TAG_PROTECTION or "pgnchess" in tags:
        js.append( bundledScript(MOD_DIR+"/pgnchess/pgnyui.js") )
        js.append( bundledScript(MOD_DIR+"/pgnchess/pgnviewer.js") )
        js.append( bundledCSS(MOD_DIR+"/pgnchess/board-min.css") )

    # List other head jobs here:
    # ===================================
    # if BYPASS_TAG_PROTECTION or "xxxxx" in tags:
        # js.append( bundledScript(MOD_DIR+"/xxxxx/script.js") )

    return "".join(js)


def head_buffer(webview, *args, **kwargs):
    old = kwargs.pop('_old')
    card=mw.reviewer.card
    if card:
        head = kwargs.get("head",'')
        head += getHeads(card.note().tags)
        kwargs["head"] = head
    return old(webview, *args[:-1], **kwargs)


# ===== EXEC ===========

AnkiWebView.stdHtml=wrap(
    AnkiWebView.stdHtml,
    head_buffer,
    "around"
)
