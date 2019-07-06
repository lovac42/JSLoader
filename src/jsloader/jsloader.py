# -*- coding: utf-8 -*-
# Copyright 2019 Lovac42
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Support: https://github.com/lovac42/JSLoader
# Version: 0.0.1; Prototype version made for PGN Chess

# Card must be tagged as "pgnchess" to activate


import os
import json
from anki.hooks import wrap
from aqt.webview import AnkiWebView
from aqt import mw


def getHeads():
    head=""
    note=mw.reviewer.card.note()

    if "pgnchess" in note.tags:
        head+=bundledScript(MOD_DIR+"/pgnchess/pgnyui.js")
        head+=bundledScript(MOD_DIR+"/pgnchess/pgnviewer.js")
        head+=bundledCSS(MOD_DIR+"/pgnchess/board-min.css")

    # List other head jobs here:
    # ===================================
    # if "xxxxx" in note.tags:
        # head+=bundledScript(MOD_DIR+"/xxxxx/script.js")

    return head


def head_buffer(self, body, css=None, js=None, head="", _old=None):
    if not head and mw.state=="review":
        head=getHeads()
    return _old(self,body,css,js,head)


# === UTILS ===

def bundledScript(fname):
    return '<script src="%s"></script>' % webBundlePath(fname)

def bundledCSS(fname):
    return '<link rel="stylesheet" type="text/css" href="%s">' % webBundlePath(fname)

def webBundlePath(path):
    return "http://127.0.0.1:%d/_addons/%s" % (mw.mediaServer.getPort(), path)

def setWebExports():
    MOD_ABS,_ = os.path.split(__file__)
    MOD_DIR = os.path.basename(MOD_ABS)
    mw.addonManager._webExports[MOD_DIR] = '.*\.(js|css)$'
    return MOD_DIR


# ===== EXEC ===========
MOD_DIR=setWebExports()
AnkiWebView.stdHtml=wrap(AnkiWebView.stdHtml,head_buffer,"around")

