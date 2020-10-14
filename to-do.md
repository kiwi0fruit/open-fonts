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


## Test Serif

Α Β Γ Δ Ε Ζ Η Θ Ι Κ Λ Μ Ν Ξ Ο Π Ρ Σ Τ Υ Φ Χ Ψ Ω α β γ δ ε ζ η θ ι κ λ μ ν ξ ο π ρ σ ς τ υ φ χ ψ ω  
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z

Apparently we had reached a great height in the atmosphere, for the sky was a dead black, and the stars had ceased to twinkle. By the same illusion which lifts the horizon of the sea to the level of the spectator on a hillside, the sable cloud beneath was dished out, and the car seemed to float in the middle of an immense dark sphere, whose upper half was strewn with silver. Looking down into the dark gulf below, I could see a ruddy light streaming through a rift in the clouds.

(EN) The quick brown fox jumps over the lazy dog. (NL) Op brute wijze ving de schooljuf de quasi-kalme lynx. (CS) Nechť již hříšné saxofony ďáblů rozezvučí síň úděsnými tóny waltzu, tanga a quickstepu. (HU) Jó foxim és don Quijote húszwattos lámpánál ülve egy pár bűvös cipőt készít. (RO) Înjurând pițigăiat, zoofobul comandă vexat whisky și tequila. (RU) Разъяренный чтец эгоистично бьёт пятью жердями шустрого фехтовальщика. (BG) Огньове изгаряха с блуждаещи пламъци любовта човешка на Орфей. (SR) Фијуче ветар у шибљу, леди пасаже и куће иза њих и гунђа у оџацима. (EL) Ταχίστηn your αλώπηξ βαφής ψημuένvη γη, δραaσκελίζει υπέρp νωθρού κkυνός. Type your own text to test the font!


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
