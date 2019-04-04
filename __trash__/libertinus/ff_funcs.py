# -*- coding: utf-8 -*-
import fontforge


def ff(*args):
    """function_name: str=args[0]"""
    return globals()[args[0]](*args[1:])


def version(x):
    return fontforge.version() + ' ' + str(x)
