# -*- coding: utf-8 -*-
import os
from os.path import join
import fontforge
import shutil


repos = os.path.normpath(join(os.getcwd(), '../'))
libertinus = join(repos, 'libertinus')
pt = join(os.getcwd(), 'Fonts')
dir_ = join(repos, 'libert_serif')
if not os.path.exists(dir_):
    os.makedirs(dir_)


# Set characters to delete from Libertinus Serif
# ----------------------------------------------
# Cyrillic (256) + Cyrillic Supplement (48) = 304
cyr_pt = u"ЁЂЃЄЅІЇЈЉЊЋЌЎЏАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяёђѓєѕіїјљњћќўџѢѣѲѳѴѵҊҋҌҍҎҏҐґҒғҔҕҖҗҘҙҚқҜҝҞҟҠҡҢңҤҥҦҧҨҩҪҫҬҭҮүҰұҲҳҴҵҶҷҸҹҺһҼҽҾҿӀӃӄӅӆӇӈӉӊӋӌӍӎӏӐӑӒӓӔӕӖӗӘәӚӛӜӝӞӟӠӡӢӣӤӥӦӧӨөӪӫӬӭӮӯӰӱӲӳӴӵӶӷӸӹӼӽ" + u"ԐԑԒԓԜԝԤԥԦԧԮԯ"  # Cyrillic in PT Astra Serif
cyr_tinos = u"ЀЍѐѝѠѡѤѥѦѧѨѩѪѫѬѭѮѯѰѱѶѷѸѹѺѻѼѽѾѿҀҁ҂҃҄҅҆҇҈҉ӁӂӺӻӾӿ" + u"ԀԁԂԃԄԅԆԇԈԉԊԋԌԍԎԏԚԛ"  # Cyrillic in Tinos (Noto Serif also has them)
cyr_noto = u"" + u"ԔԕԖԗԘԙԞԟԠԡԢԣ"  # Cyrillic in Noto Serif
cyr_other = u"" + u"ԨԩԪԫԬԭ"  # Cyrillic in Symbola that has only regular style
cyr = cyr_pt + cyr_tinos + cyr_noto
# print(len(cyr) + len(cyr_other))


# Libert Serif
# ----------------------------------------------
# Libert Serif does not have semibold and bold italic
# (both latin and cyrillic would be in the same style)
libert_all = [
    'libertinusserif-italic.otf',
    'libertinusserif-bold.otf',
    'libertinusserifdisplay-regular.otf',
    'libertinusserifinitials-regular.otf',
    'libertinusserif-regular.otf',
    'libertinusserif-semibold.otf',
]


def rep(string):
    if isinstance(string, str):
        return string.replace('ibertinus', 'ibert')
    else:
        if isinstance(string, tuple):
            return tuple(item.replace('ibertinus', 'ibert') for item in string)
        else:
            return string

for file_ in libert_all:
    f = join(dir_, file_)
    shutil.copy(join(libertinus, file_), f)
    font = fontforge.open(f)
    font.fontname = rep(font.fontname)
    font.familyname = rep(font.familyname)
    font.fullname = rep(font.fullname)
    font.sfnt_names = [rep(item) for item in font.sfnt_names]
    font.generate(rep(f))
    os.remove(f)


# Libertine Serif
# ----------------------------------------------
# Libertine Serif does not have cyrillic at all
libertine_all = [
    'libertinusserif-regular.otf',
    'libertinusserif-italic.otf',
    'libertinusserif-bold.otf',
    'libertinusserif-bolditalic.otf',
    'libertinusserif-semibold.otf',
    'libertinusserif-semibolditalic.otf',
    'libertinusserifinitials-regular.otf',
    'libertinusserifdisplay-regular.otf',
]


def rep(string):
    if isinstance(string, str):
        return string.replace('ibertinus', 'ibertin')
    else:
        if isinstance(string, tuple):
            return tuple(item.replace('ibertinus', 'ibertin') for item in string)
        else:
            return string

for file_ in libertine_all:
    f = join(dir_, file_.replace('.otf', '2.otf'))
    shutil.copy(join(libertinus, file_), f)
    font = fontforge.open(f)
    if True:
        for c in cyr:
            font.selection[ord(c)] = True
        for i in font.selection.byGlyphs:
            font.removeGlyph(i)
    font.fontname = rep(font.fontname)
    font.familyname = rep(font.familyname)
    font.fullname = rep(font.fullname)
    font.sfnt_names = [rep(item) for item in font.sfnt_names]
    font.generate(rep(f).replace('2', ''))
    os.remove(f)


# Copy License
# ----------------------------------------------
for file_ in ['OFL.txt', 'FONTLOG.txt']:
    shutil.copy(join(libertinus, file_), join(dir_, file_))
