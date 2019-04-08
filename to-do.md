

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


## Archive Inconsolata S spec

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
4. Monospacify Inconsolata LGC as it's has wrong spaces.


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


## Fallbacker

* [Font fallback app via FontForge Python](https://github.com/cpitclaudel/monospacifier/issues/15) may be written in order to use mentioned fallback chains in TeX or MS Word conveniently.
