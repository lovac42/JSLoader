# -*- coding: utf-8 -*-
# Copyright 2019-2020 Lovac42
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
# Support: https://github.com/lovac42/JSLoader


from .lib.com.lovac42.anki.version import POINT_VERSION

if POINT_VERSION < 22:
    from . import jsloader21A
else:
    from . import jsloader21B
