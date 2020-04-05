# -*- coding: utf-8 -*-
# Copyright 2019-2020 Lovac42
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Support: https://github.com/lovac42/JSLoader


import os
from aqt import mw

from .lib.com.lovac42.anki.version import ANKI21, CCBC


def getAbsolutePath(f):
    m,_ = os.path.split(f)
    return m

def setWebExports(media_types=""):
    MOD_ABS = getAbsolutePath(__file__)
    if ANKI21:
        MOD_DIR = os.path.basename(MOD_ABS)
        mw.addonManager._webExports[MOD_DIR] = media_types
        return MOD_DIR
    return MOD_ABS


def addonBundlePath(addon, path):
    return f"/_addons/{addon}/{path}"


# === UTILS for 21A ===

def bundledScript(fname):
    return '<script src="%s"></script>' % webBundlePath(fname)

def bundledCSS(fname):
    return '<link rel="stylesheet" type="text/css" href="%s">' % webBundlePath(fname)

def webBundlePath(path):
    if CCBC:
        return "file:///%s" % path.replace('\\','/')
    return "http://127.0.0.1:%d/_addons/%s" % (mw.mediaServer.getPort(), path)
