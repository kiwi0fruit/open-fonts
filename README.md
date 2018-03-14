# Open Fonts

Open Fonts is a collection of fonts and instructions for installing beautiful free and open source fonts.

Contents:

* [Best Sans Serif](#best-sans-serif)
* [Best Serif](#best-serif)
* [MacType](#mactype)
* [Stylebot](#stylebot)
* [Best Monospace](#best-monospace)
* [P.S.](#ps)


# Best Sans Serif

## [Open Sans](https://fonts.google.com/specimen/Open+Sans) (by Steve Matteson), [Download](https://github.com/google/fonts/tree/master/apache/opensans)

* 1st Unicode fallback: [Noto Sans](https://fonts.google.com/specimen/Noto+Sans) LGC (by Steve Matteson and Google), [Download](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/NotoSans-hinted.7z),
* 2nd Unicode fallback: [DejaVu Sans](https://fontlibrary.org/en/font/dejavu-sans), [Download](https://dejavu-fonts.github.io/Download.html),
* Math fallback: [STIX Two Math](http://www.stixfonts.org/) (by STI Pub consortium), [Download](https://sourceforge.net/projects/stixfonts/),
* Final Unicode fallback: [Symbola](https://fontlibrary.org/en/font/symbola) (by George Douros), [Download](https://fontlibrary.org/en/font/symbola),
* CJK fallback: Noto Sans CJK TC Regular (by Google), [Download](https://www.google.com/get/noto/) (search for Noto Sans CJK). TC is Traditional Chinese but it can also be SC, JP, KR.

Font fallback chain: `'Open Sans', 'Noto Sans', 'DejaVu Sans', 'STIX Two Math', Symbola, 'Noto Sans CJK TC Regular', sans`.


# Best Serif

## [Libertinus Serif](https://github.com/khaledhosny/libertinus) (by Philipp H. Poll, fork by Khaled Hosny), [Download](https://fontlibrary.org/en/font/libertinus-serif)

Libertinus Serif is poorly supported by Windows ClearType. WS Word 2007 renders it ugly. Chrome with ClearTpe renders it nicely though. It's really beautiful on Linux, MacOS or Windows with [MacType](#mactype).

The original version is unfinished so I recommend using:
* In case of **Chrome/Chromium only**: [Libertin Serif/Libert Serif](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/libert_serif.7z) that is a fork of Libertinus Serif. [Download](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/libert_serif.7z),
* In case of **PDF/Firefox**: [Libertinus Serif](https://github.com/khaledhosny/libertinus) that is a fork of Linux Libertine. [Download](https://fontlibrary.org/en/font/libertinus-serif).

Note that:

* Libertinus Serif has some bugfixes and perhaps new characters (in comparison with Linux Libertine),
* Libertin Serif doesn't have cyrillic characters at all. In other ways it's the same as Libertinus Serif,
* Libert Serif doesn't have bold-italic and semibold-italic styles. In other ways it's the same as Libertinus Serif. Chome/Chromium would automatically create bold style from italic on the fly,
* The best combination in case of Chrome/Chromium CSS is `Libertin Serif, Libert Serif` fallback chain. In this case you would have original Libertinus Serif bold and semibold italics for Latin and you would have Chrome-generated bold italics for Cyrillic. [Here](https://github.com/fontforge/fontforge/issues/3255) you can see the quality of Chrome's automatic bold-italic from italic generator.

Other fallback fonts:

* Cyrillic fallback: [PT Astra Serif](https://github.com/google/fonts/issues/565) (by Alexandra Korolkova and Isabella Chaeva), [Download](http://www.paratype.ru/uni/public/PTAstraSerif.zip). [Here](https://github.com/khaledhosny/libertinus/issues/74) you can see how good PT Astra Serif mixes with Linux Libertine.
* 1st Unicode fallback: [Tinos](https://fonts.google.com/specimen/Tinos) (by Steve Matteson), [Download](https://github.com/google/fonts/tree/master/apache/tinos),
* 2nd Unicode fallback: [Noto Serif](https://fonts.google.com/specimen/Noto+Serif) LGC (by Steve Matteson and Google), [Download](https://github.com/kiwi0fruit/open-fonts/tree/master/Fonts),
* Math fallback: [STIX Two Math](http://www.stixfonts.org/) (by STI Pub consortium), [Download](https://sourceforge.net/projects/stixfonts/),
* Final Unicode fallback: [Symbola](https://fontlibrary.org/en/font/symbola) (by George Douros), [Download](https://fontlibrary.org/en/font/symbola),
* CJK fallback: Noto Serif CJK TC (by Google), [Download](https://www.google.com/get/noto/) (search for Noto Serif CJK). TC is Traditional Chinese but it can also be SC, JP, KR.

Font fallback chain:

* In case of **Chrome/Chromium only** `'Libertin Serif', 'Libert Serif', 'PT Astra Serif', Tinos, 'Noto Serif', 'STIX Two Math', Symbola, 'Noto Serif CJK TC', serif`,
* In case of **PDF/Firefox**: `'Libertinus Serif', 'PT Astra Serif', Tinos, 'Noto Serif', 'STIX Two Math', Symbola, 'Noto Serif CJK TC', serif`.

Worth mentioning [Libertinus Math](https://fontlibrary.org/en/font/libertinus-math) that bring Libertinus Serif to OpenType math-capable applications like LuaTeX, XeTeX or MS Word 2007+.


## Build Libert Serif

1. [Install FontForge](https://fontforge.github.io/en-US/downloads/windows/)
2. Clone Libertinus and Open Fonts repos:
```sh
git clone --depth=1 https://github.com/kiwi0fruit/libertinus
git clone https://github.com/kiwi0fruit/open-fonts
```
3. Run appropriate batch script


# [MacType](https://github.com/snowie2000/mactype)

If on Windows it's recommended to install [MacType](http://www.mactype.net/) because Windows original ClearType is capable of rendering only fonts that were pre-optimized for ClearType - it cannot display arbitrary font in a beautiful way. MacType can do it. Now that Full HD is everywhere it's a shame for ClearType.

**Important**:

* Use Default profile but change ini setting to `NormalWeight=8` (instead of 16) (with this the [difference between Chrome and other programs](https://github.com/snowie2000/mactype/issues/402) is not so big),
* MacType can clash with cheap Antiviruses though. In my case the problem was solved by deleting AVG/Avast and installing Kaspersky Free (Kaspersky IS is also OK).
* MacType changes permissions of his folder in Program Files. I'm not sure that it's a good idea. So I recommend removing non-inherited permissions from MacType folder (apply this to subfolders also). So that the folder modification is possible only with admin privilegies.
* Some programs need special config settings. For example PyCharm:
```ini
[Experimental@pycharm64.exe]
ClipBoxFix=1
[General@pycharm64.exe]
NormalWeight=-8
BoldWeight=-4
```
See details about other programs in [this repo](https://github.com/wspl/mactype-hack).

Actually MacType can be tuned. Here is my custom part of the config:
```ini
[Experimental@pycharm64.exe]
;PyCharm fix
ClipBoxFix=1
[General@pycharm64.exe]
;PyCharm fix + Consolas
NormalWeight=-14
BoldWeight=-4
[General@notepad++.exe]
;for Consolas
NormalWeight=-4
BoldWeight=-2
[General@notepad.exe]
;for Consolas
NormalWeight=-4
BoldWeight=-2
[General@explorer.exe]
;Explorer fix
NormalWeight=12
```


# [Stylebot](https://github.com/ankit/stylebot)

Stylebot is an open source Google Chrome extension that allows users to manipulate a web page’s appearance. [Install](https://chrome.google.com/webstore/detail/stylebot/oiaejidbmkiecgbjeifoejpgmdaleoha).

1. Incrementally build custom stylesheets for Chrome.
2. Save custom CSS rules for sites. The next time they visit a site, their custom CSS is already applied.
3. Export and import creted styles.

I haven't checked if it's safe. But it looks safe.

This extesnion would help you to make internet less messy in style :-)


# Best Monospace

## [Roboto Mono](https://fonts.google.com/specimen/Roboto+Mono) (by Christian Robertson).

Italic in Roboto Mono has different width so it's recommended to use **Open Mono** fork that is simply a renamed monospacified version of Roboto Mono.

See best fallback chain for Roboto Mono in the [SugarTeX docs](https://github.com/kiwi0fruit/sugartex#atom-editor-with-full-unicode-support).


## Consolas (by Luc(as) de Groot)

It's the best ClearType optimized monospace font if on Windows. It looks too thick on big sizes but in Chromium based Atom editor with [MacType](#mactype) default profile it looks excellent.

It's also good without ClearType. See install instructions and best fallback chain for Consolas in the [SugarTeX docs](https://github.com/kiwi0fruit/sugartex#atom-editor-with-full-unicode-support).


## Build Open Mono and DejaVu Sans Mono for Consolas

1. [Install FontForge](https://fontforge.github.io/en-US/downloads/windows/)
2. Clone Google Fonts, other fonts, Monospacifier and Open Fonts repos:
```sh
git clone --depth=1 https://github.com/kiwi0fruit/fonts
git clone https://github.com/kiwi0fruit/monospacifier
git clone https://github.com/kiwi0fruit/open-fonts
# copy `consola.ttf` to local open-fonts repo folder
```
3. Run appropriate batch script


# TODO:

## Inconsolata S spec

Inconsolata S is a font for [SugarTeX](https://github.com/kiwi0fruit/sugartex) that would be based on [Inconsolata LGC](https://github.com/kiwi0fruit/Inconsolata-LGC) (by Raph Levien, Dimosthenis Kaponis, MihailJP).

Actually Inconsolata is prettie than Roboto Mono but Roboto Mono has better unicode support and some other better characters.

1. Replace:
  * I, IB `a` (lat/cyr) - **make** from Inconsolata `d` looking at Open Sans italic `a`,
  * I, IB `y` (lat/cyr) - from Noto Mono (I, IB make via FontForge). Or take from Noto Sans,
  * I, IB `д` (cyr) - from Noto Sans,
  * R, I, B, IB "\`" take from <...> (also take all modifier letter and combining accents - for style consistency),
  * Also see characters in "Roboto Mono fork spec" (they should be adapted),
2. Inconsolata S should be of the same thickness as Inconsolata LGC For Powerline,
3. Use Noto Sans Mono (OFL), Noto Sans (OFL).


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


## Archive Open Mono spec

Font Fallback chain:

Roboto Mono, Fira Mono, Cousine, DejaVu Sans Mono, STIX Two Math, Symbola, Noto Sans Symbols

This fallback chain would be used for generating Open Mono.

Characters that should be taken from particular fonts ignoring fallback chain:

* Cousine: `ˎˏˌαχνᵦᵩₐₑₒᵤᵥₓᵅᵝᵟᵋᶿᶲᵠᵃᵇᶜᵈᵉᶠʰʲᵏˡᵐᵒᵖˢᵘᵛʷˣʸᶻᴬᴮᴰᴱᴳᴴᴶᴷᴸᶫᴹᴺᶰᴼᴾᴿᵀᵁᶸⱽᵂ`, `ₗ` - copy and move `ˡ`, `⁄` (fraction slash),
* Symbola: `ᵨᵧᵪᵞᵡ`,
* DejaVu Sans Mono: `˳ᴵᶦⁱⁿᵗᶥʳₕᵢⱼₖₘₙₚᵣₛₜ₀₂₃₄₅₆₇₈₉⁰²³⁴⁵⁶⁷⁸⁹`, `∕` (division slash).
* Source Code Pro: `ᵍ`,
* Fira Mono: `γ@®<>[]%^‘’“”"',;.:‚„!?`, (add Fira Mono italic via FontForge),
* DejaVu Sans Mono: `⅟ ½ ⅓ ¼ ⅕ ⅙ ⅛ ⅔ ⅖ ¾ ⅗ ⅜ ⅘ ⅚ ⅝ ⅞ ↉ ⅐ ⅑ ⅒ ↉ ⅐ ⅑ `
* **either** Open Sans: `g` (adjust weight by 17 for regular and italic first),
* **or** Droid Sans Mono: `g` (check weight and Look on Windows since Droid Sans Mono looks badly on Windows),
* Roboto Mono: `₁` - copy and move `¹`,
* Make narrower like in TeX Gyre Schola Math: `⎴⎵`.

Note that for now `⅒` are present in DejaVu Sans or Symbola.


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

* another [test text](https://github.com/kiwi0fruit/sugartex/blob/master/sugartex.md).


# P.S.

* [Font fallback app via FontForge Python](https://github.com/cpitclaudel/monospacifier/issues/15) may be written in order to use mentioned fallback chains in TeX or MS Word conveniently.
