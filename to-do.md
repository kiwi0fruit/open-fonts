# TODO

## Useful FontForge python methods

`copy`, `paste`, `removeGlyph`, `select`, `invert`, `italicize`, `changeWeight`, `translate`. Taken from [this manual](https://fontforge.github.io/python.html).

```py
import fontforge
import psMat

fontforge.open("font.ttf")
font = fontforge.activeFont()
font.selection.all()
for glyph in font.selection.byGlyphs:
    bbox = glyph.boundingBox()
    if bbox[1] < 0:
        mat = psMat.translate(0, -bbox[1])
        glyph.transform(mat)
font.generate("font.ttf")
```

Useful [stackoverflow answer](https://stackoverflow.com/questions/14557944/downsizing-an-otf-font-by-removing-glyphs/34132900#34132900).


## Test Monospace

* test text:

```
ₐₑₕᵢⱼₖₗₘₙₒₚᵣₛₜᵤᵥₓᵦᵧᵨᵩᵪ₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎
aehijklmnoprstuvxβγρφχ0123456789+-=()
⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ᴬᴮᴰᴱᴳᴴᴵᶦᴶᴷᴸᶫᴹᴺᶰᴼᴾᴿᵀᵁᶸⱽᵂᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻᵅᵝᵞᵟᵋᶿᶥᶲᵠᵡ
0123456789+-=()ABDEGHIIJKLLMNNOPRTUUVWabcdefghijklmnoprstuvwxyzαβγδεθιϕφχ
Αα Ββ Γγ Δδ Εε Ζζ Ηη Θθ Ιι Κκ Λλ Μμ Νν Ξξ Οο Ππ Ρρ Σσς Ττ Υυ Φφϕ Χχ Ψψ Ωω
Aa B   y    Ee Zz Hn O0 Ii Kk    Mu Nv    Oo    Pp     Tt Yu     Xx      
0⁰₀Oᴼoᵒₒ1¹₁lˡₗiⁱᵢIᴵᶦLᴸᶫ˳ˌ
↕→←↑↓⇩⇧
```

* `ˎˏˌαχνᵦᵩₐₑₒᵤᵥₓᵅᵝᵟᵋᶿᶲᵠᵃᵇᶜᵈᵉᶠʰʲᵏˡᵐᵒᵖˢᵘᵛʷˣʸᶻᴬᴮᴰᴱᴳᴴᴶᴷᴸᶫᴹᴺᶰᴼᴾᴿᵀᵁᶸⱽᵂ` `ₗ` `ˡ` `⁄` (fraction slash)
* `ᵨᵧᵪᵞᵡ`
* `˳ᴵᶦⁱⁿᵗᶥʳₕᵢⱼₖₘₙₚᵣₛₜ₀₂₃₄₅₆₇₈₉⁰²³⁴⁵⁶⁷⁸⁹` `∕` (division slash).
* `ᵍ`
* `γ@®<>[]%^‘’“”"',;.:‚„!?`
* `⅟ ½ ⅓ ¼ ⅕ ⅙ ⅛ ⅔ ⅖ ¾ ⅗ ⅜ ⅘ ⅚ ⅝ ⅞ ↉ ⅐ ⅑ ⅒ ↉ ⅐ ⅑`
* `₁` `¹`
* `⎴⎵`
* `` ` ˋ ˎ ˏ a̖ à a̗ á ``
* another [test text](https://github.com/kiwi0fruit/sugartex/blob/master/sugartex.md).
*ԀԁԂԃԄԅԆԇԈԉԊԋԌԍԎԏԚԛ  даo*
```
cyr_pt = u"ЁЂЃЄЅІЇЈЉЊЋЌЎЏАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюяёђѓєѕіїјљњћќўџѢѣѲѳѴѵҊҋҌҍҎҏҐґҒғҔҕҖҗҘҙҚқҜҝҞҟҠҡҢңҤҥҦҧҨҩҪҫҬҭҮүҰұҲҳҴҵҶҷҸҹҺһҼҽҾҿӀӃӄӅӆӇӈӉӊӋӌӍӎӏӐӑӒӓӔӕӖӗӘәӚӛӜӝӞӟӠӡӢӣӤӥӦӧӨөӪӫӬӭӮӯӰӱӲӳӴӵӶӷӸӹӼӽ" + u"ԐԑԒԓԜԝԤԥԦԧԮԯ"  # Cyrillic in PT Astra Serif
cyr_tinos = u"ЀЍѐѝѠѡѤѥѦѧѨѩѪѫѬѭѮѯѰѱѶѷѸѹѺѻѼѽѾѿҀҁ҂҃҄҅҆҇҈҉ӁӂӺӻӾӿ" + u"ԀԁԂԃԄԅԆԇԈԉԊԋԌԍԎԏԚԛ"  # Cyrillic in Tinos (Noto Serif also has them)
cyr_noto = u"" + u"ԔԕԖԗԘԙԞԟԠԡԢԣ"  # Cyrillic in Noto Serif
cyr_other = u"" + u"ԨԩԪԫԬԭ"  # Cyrillic in Symbola that has only regular style

```

```py
import re
import sys
l = [chr(i) for i in range(sys.maxunicode)
     if re.match(r'^[\s]$', chr(i)) and (chr(i) not in ('\t', '\n', '\r', ' '))]

o = ''.join(
    ('[' + ']['.join(['x' for i in range(10)]) + ']\n' +
     '[' + ']['.join([c for i in range(10)]) + ']\n')
    for c in l
)
print(o)
```

```
[x][x][x][x][x][x][x][x][x][x]
[][][][][][][][][][]
[x][x][x][x][x][x][x][x][x][x]
[][][][][][][][][][]
[x][x][x][x][x][x][x][x][x][x]
[][][][][][][][][][]
[x][x][x][x][x][x][x][x][x][x]
[][][][][][][][][][]
[x][x][x][x][x][x][x][x][x][x]
[][][][][][][][][][]
[x][x][x][x][x][x][x][x][x][x]
[][][][][][][][][][]
[x][x][x][x][x][x][x][x][x][x]
[][][][][][][][][][]
[x][x][x][x][x][x][x][x][x][x]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[x][x][x][x][x][x][x][x][x][x]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]

[x][x][x][x][x][x][x][x][x][x]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[x][x][x][x][x][x][x][x][x][x]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[x][x][x][x][x][x][x][x][x][x]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[x][x][x][x][x][x][x][x][x][x]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[x][x][x][x][x][x][x][x][x][x]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[x][x][x][x][x][x][x][x][x][x]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[x][x][x][x][x][x][x][x][x][x]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[x][x][x][x][x][x][x][x][x][x]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[x][x][x][x][x][x][x][x][x][x]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[x][x][x][x][x][x][x][x][x][x]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[x][x][x][x][x][x][x][x][x][x]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[x][x][x][x][x][x][x][x][x][x]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[x][x][x][x][x][x][x][x][x][x]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[x][x][x][x][x][x][x][x][x][x]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[x][x][x][x][x][x][x][x][x][x]
[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
[x][x][x][x][x][x][x][x][x][x]
[　][　][　][　][　][　][　][　][　][　]
```

```py
sp = [
   "\xad", # soft hyphen U+00AD
   "\u058a", # armenian hyphen
   "\u1806", # mongolian todo soft hyphen
   "\ufe63", # small hyphen-minus
   "\uff0d", # fullwidth hyphen-minus
   "\u2043", # hyphen bullet
   "\u2010", # hyphen
   "\u2011", # non-breaking hyphen
   "\u2212", # minus sign
   "\u23af", # horizontal line extension
   "\u23e4", # straightness
   "\u2500", # box drawings light horizontal
   "\u2796", # heavy minus sign
   "\u2e3a", # two-em dash
   "\u2e3b", # three-em dash
   "\U00010191", # roman uncia sign
   "\u2012", # figure dash
   "\u2013", # en dash
   "\u2014", # em dash
   "\u2015", # horizontal bar
]
o = ''.join(
    ('[' + ']['.join(['x' for i in range(10)]) + ']\n' +
     '[' + ']['.join([c for i in range(10)]) + ']\n')
    for c in sp
)
print(o)
```

```
[x][x][x][x][x][x][x][x][x][x]
[­][­][­][­][­][­][­][­][­][­]
[x][x][x][x][x][x][x][x][x][x]
[֊][֊][֊][֊][֊][֊][֊][֊][֊][֊]
[x][x][x][x][x][x][x][x][x][x]
[᠆][᠆][᠆][᠆][᠆][᠆][᠆][᠆][᠆][᠆]
[x][x][x][x][x][x][x][x][x][x]
[﹣][﹣][﹣][﹣][﹣][﹣][﹣][﹣][﹣][﹣]
[x][x][x][x][x][x][x][x][x][x]
[－][－][－][－][－][－][－][－][－][－]
[x][x][x][x][x][x][x][x][x][x]
[⁃][⁃][⁃][⁃][⁃][⁃][⁃][⁃][⁃][⁃]
[x][x][x][x][x][x][x][x][x][x]
[‐][‐][‐][‐][‐][‐][‐][‐][‐][‐]
[x][x][x][x][x][x][x][x][x][x]
[‑][‑][‑][‑][‑][‑][‑][‑][‑][‑]
[x][x][x][x][x][x][x][x][x][x]
[−][−][−][−][−][−][−][−][−][−]
[x][x][x][x][x][x][x][x][x][x]
[⎯][⎯][⎯][⎯][⎯][⎯][⎯][⎯][⎯][⎯]
[x][x][x][x][x][x][x][x][x][x]
[⏤][⏤][⏤][⏤][⏤][⏤][⏤][⏤][⏤][⏤]
[x][x][x][x][x][x][x][x][x][x]
[─][─][─][─][─][─][─][─][─][─]
[x][x][x][x][x][x][x][x][x][x]
[➖][➖][➖][➖][➖][➖][➖][➖][➖][➖]
[x][x][x][x][x][x][x][x][x][x]
[⸺][⸺][⸺][⸺][⸺][⸺][⸺][⸺][⸺][⸺]
[x][x][x][x][x][x][x][x][x][x]
[⸻][⸻][⸻][⸻][⸻][⸻][⸻][⸻][⸻][⸻]
[x][x][x][x][x][x][x][x][x][x]
[𐆑][𐆑][𐆑][𐆑][𐆑][𐆑][𐆑][𐆑][𐆑][𐆑]
[x][x][x][x][x][x][x][x][x][x]
[‒][‒][‒][‒][‒][‒][‒][‒][‒][‒]
[x][x][x][x][x][x][x][x][x][x]
[–][–][–][–][–][–][–][–][–][–]
[x][x][x][x][x][x][x][x][x][x]
[—][—][—][—][—][—][—][—][—][—]
[x][x][x][x][x][x][x][x][x][x]
[―][―][―][―][―][―][―][―][―][―]
```

## Fallbacker

* [Font fallback app via FontForge Python](https://github.com/cpitclaudel/monospacifier/issues/15) may be written in order to use mentioned fallback chains in TeX or MS Word conveniently.
