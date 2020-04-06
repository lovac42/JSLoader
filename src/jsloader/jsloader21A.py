# -*- coding: utf-8 -*-
# Copyright 2019-2020 Lovac42
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Support: https://github.com/lovac42/JSLoader


from anki.hooks import wrap
from aqt.webview import AnkiWebView
from aqt import mw

from .utils import *
from .config import Config
from .const import MOD_DIR, ADDON_NAME


conf = Config(ADDON_NAME)


def getHeads(tags):
    js=[]
    bypass = conf.get("bypass_tag_protection", False)
    if bypass or "pgnchess" in tags:
        js.append( bundledScript(MOD_DIR+"/pgnchess/pgnyui.js") )
        js.append( bundledScript(MOD_DIR+"/pgnchess/pgnviewer.js") )
        js.append( bundledCSS(MOD_DIR+"/pgnchess/board-min.css") )

    # List other head jobs here:
    # ===================================
    # if bypass or "xxxxx" in tags:
        # js.append( bundledScript(MOD_DIR+"/xxxxx/script.js") )

    return "".join(js)




def head_buffer(head):
    card=mw.reviewer.card
    if card:
        js = getHeads(card.note().tags)
        if js:
            head += js
    return head

def stdHtml21(webview, body, css=None, js=None, head="", _old=None):
    head = head_buffer(head)
    return _old(webview,body,css,js,head)

def stdHtml20(webview, body, css="", bodyClass="", loadCB=None, js=None, head="", _old=None):
    head = head_buffer(head)
    return _old(webview,body,css,bodyClass,loadCB,js,head)


# ===== EXEC ===========

from .lib.com.lovac42.anki.version import ANKI21
func = stdHtml21 if ANKI21 else stdHtml20
AnkiWebView.stdHtml = wrap(AnkiWebView.stdHtml, func, "around")
