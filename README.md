# Open Fonts

A collection of beautiful free and open source fonts: instructions for installing, Unicode fallback chains, instructions to replace Windows ClearType and fix browser fonts.

Contents:

* [Best Sans Serif](#best-sans-serif)
* [Best Serif](#best-serif)
* [Best Monospace](#best-monospace)
* [MacType](#mactype)
* [Stylebot](#stylebot)
* [Build](#build)
* [TO DO](#to-do)


# Install

* All non-CJK fonts in one [**archive**](https://github.com/kiwi0fruit/open-fonts/releases) ([**list**](https://github.com/kiwi0fruit/open-fonts/tree/master/open-fonts/css) of all non-CJK fonts).
* All CJK fonts in one [**archive**](https://github.com/kiwi0fruit/open-fonts/releases) ([**list**](https://github.com/kiwi0fruit/open-fonts/tree/master/open-fonts-cjk/css) of all CJK fonts).
* [Install Open Fonts in pip and conda (non-CJK only)](https://github.com/kiwi0fruit/py-open-fonts/tree/master/pypi/py-open-fonts).


# Best Sans Serif

First of all OTF and TTF versions of **every** font have different display weight on Windows on small sizes for some reason (see [this](https://github.com/adobe-fonts/source-sans-pro/issues/170) and [that](https://github.com/adobe-fonts/source-sans-pro/issues/200)) hence use TTF version as it looks closer to original design.

Sans serif fonts used for main fonts and fallbacks do support:

* LGC (Latin, Greek, Cyrillic): **Source Sans Pro, Open Sans, Roboto**, Sourcing Sans Pro, Noto Sans, DejaVu Sans, Lato.
* CJK variants\*\* (Chinese, Japanese, Korean): Source Han Sans.
* Cyrillic variants\*\*: Source Sans Pro ([see more](https://localfonts.eu/freefonts/bulgarian-cyrillic/)).
* Hebrew: Noto Sans Hebrew, DejaVu Sans.
* Devanagari (Hindi and others): Noto Sans Devanagari.
* Arabic: Noto Sans Arabic.
* Math: DejaVu Sans.

Only 3 fonts are maintained for Hebrew, Arabic, Devanagari stylistic fit: Source Sans Pro, Open Sans, Roboto.

\*\* Browsers, Pandoc and LibreOffice support language variants inside single font:

* Browsers support language variants via `lang="bg-BG"` (`"zh-CN"`, `"zh-TW"`, `"zh-HK"`, `"ja-JP"`, `"ko-KR"`) HTML property.
* LibreOffice v.7.0.1 supports language variants. For CJK first enable `Tools / Options / Language Settings / Languages / Default languages for documents / Asian`. See document example [here](./cjk-test). TexMaths extension is recommended for LibreOffice together with installing WYSIWYM editor LyX and copypasting back and forth TeX formulas for easy editing (as built-in math editor in LibreOffice is rather dissapointing). LyX [quick templates](./lyx).
* Pandoc supports language variants via `[text]{lang="ru-RU"}` or setting global document language:
  ```yaml
  ---
  lang: bg
  ---
  ```


## [Source Sans Pro](https://fonts.google.com/specimen/Source+Sans+Pro)

#### (by Paul D. Hunt), [Preview](https://fonts.google.com/specimen/Source+Sans+Pro), [Preview](https://localfonts.eu/freefonts/traditional-cyrillic-free-fonts/source-sans-pro/), [Preview](https://adobe-fonts.github.io/source-sans-pro/), [Download](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/SourceSansPro.tar.xz?raw=true), [Download original](https://github.com/adobe-fonts/source-sans-pro/releases), [Backup](https://github.com/kiwi0fruit/source-sans-pro)

*My favorite!*

In the latest version the "Source Sans Pro" name was changed to "Source Sans 3". I hope that it would be [reverted](https://github.com/adobe-fonts/source-sans-pro/issues/192) but for now I recommend to use `'Sourcing Sans Pro'` (that is simply a renamed `'Source Sans 3'`) and use both fonts in the fallback chain:

Font fallback chain: `'Source Sans Pro', 'Sourcing Sans Pro', 'Noto Sans', 'Noto Sans Devanagari', 'Noto Sans Arabic', 'DejaVu Sans', 'STIX Two Math', Symbola, 'Source Han Sans', sans-serif`.

I had a bug when `'Source Sans Pro'` did not work properly in LibreOffice with language variations. But `'Sourcing Sans Pro'` worked fine. But this might be some re-installation bug. Check yourself.

**Noto Sans Hebrew might be a better Hebrew fallback than DejaVu Sans if you need to use semibolds (600):**  
`'Source Sans Pro', 'Sourcing Sans Pro', 'Noto Sans Hebrew', ...`

Fallback fonts:

* Hebrew fallback: [Noto Sans Hebrew](https://www.google.com/get/noto/#sans-hebr) (by Google), [Preview](https://www.google.com/get/noto/#sans-hebr), [Download](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/NotoSansHebrew-hinted.zip?raw=true), [Download original](https://www.google.com/get/noto/#sans-hebr).
* Hindi fallback: [Noto Sans Devanagari](https://www.google.com/get/noto/#sans-deva) (by Google), [Preview](https://www.google.com/get/noto/#sans-deva), [Download](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/NotoSansDevanagari-hinted.zip?raw=true), [Download original](https://www.google.com/get/noto/#sans-deva).
* Arabic fallback: [Noto Sans Arabic](https://www.google.com/get/noto/#sans-arab) (by Google), [Preview](https://www.google.com/get/noto/#sans-arab), [Download](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/NotoSansArabic-hinted.zip?raw=true), [Download original](https://www.google.com/get/noto/#sans-arab).
* 1st Unicode fallback: Noto Sans (see below),
* 2nd Unicode fallback and Hebrew fallback: [DejaVu Sans](https://dejavu-fonts.github.io/) (by Jim Lyles and others), [Preview](https://fontlibrary.org/en/font/dejavu-sans), [Download](https://github.com/dejavu-fonts/dejavu-fonts/releases),  [Backup](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/DejaVu), [Backup2](https://github.com/kiwi0fruit/dejavu-fonts),
* Math fallback: STIX Two Math (see below),
* Final Unicode fallback: [Symbola](http://users.teilar.gr/~g1951d/) (by George Douros), [Preview](https://fontlibrary.org/en/font/symbola), [Download latest version](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/hintedSymbola.ttf?raw=true), [Backup](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/hintedSymbola.ttf?raw=true),
* CJK fallback: Source Han Sans (by Adobe and Google), **Preview**: [JP](https://fonts.adobe.com/fonts/source-han-sans-japanese), [CN](https://fonts.adobe.com/fonts/source-han-sans-simplified-chinese), [KR](https://fonts.adobe.com/fonts/source-han-sans-korean), [HK](https://fonts.adobe.com/fonts/source-han-sans-hong-kong), [TW](https://fonts.adobe.com/fonts/source-han-sans-traditional-chinese), [Download Language-specific OTFs (Japanese is default)](https://github.com/adobe-fonts/source-han-sans/tree/release#language-specific-otfs), [Download other options](https://github.com/adobe-fonts/source-han-sans/tree/release), [Source code](https://github.com/adobe-fonts/source-han-sans), [Backup](https://github.com/kiwi0fruit/source-han-sans).


## [Open Sans](https://fonts.google.com/specimen/Open+Sans) and [Noto Sans](https://en.wikipedia.org/wiki/Noto_fonts)

#### (*Open Sans* by Steve Matteson), [Preview](https://fonts.google.com/specimen/Open+Sans), [Download](https://fonts.google.com/specimen/Open+Sans), [Download2](https://github.com/google/fonts/tree/master/apache/opensans), [Backup](https://github.com/kiwi0fruit/fonts/tree/master/apache/opensans)

#### (*Noto Sans* by Steve Matteson and Google), [Preview](https://www.google.com/get/noto/#sans-lgc), [Preview](https://fonts.google.com/specimen/Noto+Sans), [Download](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/NotoSans-hinted.zip?raw=true), [Download original latest version](https://www.google.com/get/noto/#sans-lgc).

They are almost the same font.

* Noto Sans is a bit heavier than Open Sans,
* Noto Sans has much wider Unicode coverage,
* Open Sans has gouble-story g when Noto Sans has singe-story g.

**Mind that Noto Sans has more font weghts than Open Sans so if using them together as here do not use 100, 200, 500, 800 (use 900 instead).**

Font fallback chain: `'Open Sans', 'Noto Sans', 'Noto Sans Devanagari', 'Noto Sans Arabic', 'Noto Sans Hebrew', 'DejaVu Sans', 'STIX Two Math', Symbola, 'Source Han Sans', sans-serif`.


## [Roboto](https://en.wikipedia.org/wiki/Roboto)

#### (by Christian Robertson), [Preview](https://fonts.google.com/specimen/Roboto), [Download](https://fonts.google.com/specimen/Roboto), [Download2](https://github.com/google/fonts/tree/master/apache/roboto), [Backup](https://github.com/kiwi0fruit/fonts/tree/master/apache/roboto)

Font fallback chain: `Roboto, 'Noto Sans', 'Noto Sans Devanagari', 'Noto Sans Arabic', 'Noto Sans Hebrew', 'DejaVu Sans', 'STIX Two Math', Symbola, 'Source Han Sans', sans-serif`.


## LGC only

### [Lato](http://www.latofonts.com)

#### (by Łukasz Dziedzic), [Preview](https://localfonts.eu/freefonts/traditional-cyrillic-free-fonts/lato/), [Preview](https://fonts.google.com/specimen/Lato), [Download latest version](http://www.latofonts.com/lato-free-fonts/#download), [Backup](https://github.com/kiwi0fruit/open-fonts/tree/master/Fonts/Lato), [Backup2](https://github.com/kiwi0fruit/lato-source)

Font fallback chain: `Lato, 'Noto Sans', 'DejaVu Sans', 'STIX Two Math', Symbola, sans-serif`.


# Best Serif

First of all OTF and TTF versions of **every** font have different display weight on Windows on small sizes for some reason (see [this](https://github.com/adobe-fonts/source-sans-pro/issues/170) and [that](https://github.com/adobe-fonts/source-sans-pro/issues/200)) hence use TTF version as it looks closer to original design.

Serif fonts used for main fonts and fallbacks do support:

* LGC (Latin, Greek, Cyrillic): **STIX Two Text, Source Serif Pro, Vollkorn**, ST1X Two Text, Noto Serif, DejaVu Serif, Linus Libertini.
* CJK variants (Chinese, Japanese, Korean): Source Han Serif.
* Cyrillic variants: Source Serif Pro, Vollkorn ([see more](https://localfonts.eu/freefonts/bulgarian-cyrillic/)).
* Hebrew: David Libre, DejaVu Serif, Linus Libertini.
* Devanagari (Hindi and others): Noto Serif Devanagari, Halant.
* Arabic: Amiri.
* Math: STIX Two Math, ST1X Two Math, Symbola, Linus Libertini, Amiri.

Only 3 fonts are maintained for Hebrew, Arabic, Devanagari stylistic fit: STIX Two Text, Source Serif Pro, Vollkorn.


## [STIX Two Text](http://www.stixfonts.org/) and [STIX Two Math](http://www.stixfonts.org/)

#### (by Ross Mills and others), [Preview](https://localfonts.eu/freefonts/traditional-cyrillic-free-fonts/stix/), [Download STIX Two OTF (thickening distortion on Windows)](https://github.com/stipub/stixfonts), [Backup](https://github.com/kiwi0fruit/stixfonts)

*My favorite math font!*

Font fallback chain: `'STIX Two Text', 'STIX Two Math', 'Noto Serif Devanagari', 'David Libre', Amiri, 'Noto Serif', 'DejaVu Serif', Symbola, 'Source Han Serif', serif`.

Note that STIX Two is OTF only font. Hence it would look heavier on Windows that it's original design (that's not necessary a bad thing). But you can use `'ST1X Two Text'` and `'ST1X Two Math'` that is simply STIX Two converted to TTF. [**Download ST1X Two TTF**](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/ST1XTwo.zip?raw=true).

Fallback fonts:

* 1st Unicode fallback: [Noto Serif](https://en.wikipedia.org/wiki/Noto_fonts) LGC (by Steve Matteson and Google), [Preview](https://www.google.com/get/noto/#serif-lgc), [Preview](https://fonts.google.com/specimen/Noto+Serif), [Backup](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/NotoSerif-hinted.zip?raw=true), [Download original latest version](https://www.google.com/get/noto/#serif-lgc).
* Math fallback: STIX Two Math,
* Hebrew fallback: [David Libre](https://fonts.google.com/specimen/David+Libre?subset=hebrew) (by Ismar David, Monotype Corporation, Google, Meir Sadan), [Preview](https://fonts.google.com/specimen/David+Libre?subset=hebrew), [Download](https://fonts.google.com/specimen/David+Libre?subset=hebrew), [Backup](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/David_Libre.zip?raw=true),
* Hindi fallback: [Noto Serif Devanagari](https://www.google.com/get/noto/#serif-deva) (by Google), [Preview](https://www.google.com/get/noto/#serif-deva), [Download](https://www.google.com/get/noto/#serif-deva), [Backup](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/NotoSerifDevanagari-hinted.zip?raw=true),
* Arabic fallback: [Amiri](https://fonts.google.com/specimen/Amiri?subset=arabic) (by Khaled Hosny, Sebastian Kosch), [Preview](https://fonts.google.com/specimen/Amiri?subset=arabic), [Download](https://fonts.google.com/specimen/Amiri?subset=arabic), [Download](https://github.com/google/fonts/tree/master/ofl/amiri),  [Backup](https://github.com/kiwi0fruit/fonts/tree/master/ofl/amiri),
* Alt. Hindi fallback: [Halant](https://fonts.google.com/specimen/Halant?subset=devanagari) (by Vivek Sadamate, Ninad Kale, Jonny Pinhorn), [Preview](https://fonts.google.com/specimen/Halant?subset=devanagari), [Download](https://fonts.google.com/specimen/Halant?subset=devanagari), [Download2](https://github.com/google/fonts/tree/master/ofl/halant), [Backup](https://github.com/kiwi0fruit/fonts/tree/master/ofl/halant),
* 2nd Unicode fallback and Hebrew fallback: [DejaVu Serif](https://dejavu-fonts.github.io/) (by Jim Lyles and others), [Preview](https://fontlibrary.org/en/font/dejavu-sans), [Download](https://github.com/dejavu-fonts/dejavu-fonts/releases),  [Backup](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/DejaVu), [Backup2](https://github.com/kiwi0fruit/dejavu-fonts), Hebrew glyphs look like from David Libre but a bit heavier.
* Final Unicode fallback: [Symbola](http://users.teilar.gr/~g1951d/) (by George Douros), [Preview](https://fontlibrary.org/en/font/symbola), [Download latest version](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/hintedSymbola.ttf?raw=true), [Backup](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/hintedSymbola.ttf?raw=true),
* CJK fallback: Source Han Serif (by Adobe and Google). **Preview**: [JP](https://fonts.adobe.com/fonts/source-han-serif-japanese), [CN](https://fonts.adobe.com/fonts/source-han-serif-simplified-chinese), [KR](https://fonts.adobe.com/fonts/source-han-serif-korean), [TW](https://fonts.adobe.com/fonts/source-han-serif-traditional-chinese), [Download Language-specific OTFs (Japanese is default)](https://github.com/adobe-fonts/source-han-serif/tree/release#language-specific-otfs), [Download other options](https://github.com/adobe-fonts/source-han-serif/tree/release), [Source code](https://github.com/adobe-fonts/source-han-serif), [Backup](https://github.com/kiwi0fruit/source-han-serif).

Worth mentioning [STIX Two Math](http://www.stixfonts.org/) that is a STIX Two version for OpenType math-capable applications like LuaTeX, XeTeX or MS Word 2007+.


## [Source Serif Pro](https://github.com/adobe-fonts/source-serif-pro)

#### (by Frank Grießhammer), [Preview](https://adobe-fonts.github.io/source-serif-pro/), [Preview](https://fonts.google.com/specimen/Source+Serif+Pro), [Download](https://github.com/adobe-fonts/source-serif-pro/releases), [Backup](https://github.com/kiwi0fruit/source-serif-pro)

*My favorite text body font!*

Font fallback chain: `'Source Serif Pro', 'STIX Two Text', 'STIX Two Math', Halant, 'David Libre', Amiri, 'Noto Serif', 'DejaVu Serif', Symbola, 'Source Han Serif', serif`.


## [Vollkorn](https://fonts.google.com/specimen/Vollkorn?category=Serif)

#### (by Friedrich Althausen), [Preview](https://fonts.google.com/specimen/Vollkorn?category=Serif), [Download](https://fonts.google.com/specimen/Vollkorn?category=Serif), [Backup](https://github.com/kiwi0fruit/Vollkorn-Typeface)

Font fallback chain: `Vollkorn, 'STIX Two Text', 'STIX Two Math', Halant, Amiri, 'Noto Serif', 'DejaVu Serif', Symbola, 'Source Han Serif', serif`.

Recommended CSS features: `font-feature-settings: 'tnum' 1, 'lnum' 1;` See all features [here](http://vollkorn-typeface.com/#features).  
To select right Hindi fallback weight use `font-weight: 420;`


## LGC only

### [Linux Libertine](http://libertine-fonts.org/)

#### (by Philipp H. Poll and others), [Preview](https://localfonts.eu/freefonts/traditional-cyrillic-free-fonts/linux-libertine/), [Download Linus Libertini TTF](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/LinusLibertini.zip?raw=true), [Backup](https://github.com/kiwi0fruit/libertinus)

Semibold italic Cyrillics are terrible in Linux Libertine. So it's recommended to use [**Linus Libertini**](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/LinusLibertini.zip?raw=true) fork that is simply a renamed Libertinus Serif without semibolds (Libertinus Serif is a bugfixed fork of Linux Libertine by Khaled Hosny with Cyrillic bold itallics by Stefan Peev).

There is also OTF version of the font that is a bit heavier on Windows display. [**Download Linus Libertini OTF (thickening distortion on Windows)**](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/LinusLibertiniO.zip?raw=true). This can be useful on small sizes. `'Linus Libertini O'`

Font fallback chain: `'Linus Libertini', 'STIX Two Text', 'STIX Two Math', 'Noto Serif', Symbola, serif`.

There is also [Libertinus Math](https://github.com/libertinus-fonts/libertinus) font but I find it to be of [lower quality](https://github.com/kiwi0fruit/open-fonts/issues/5#issuecomment-480476163) than STIX Two Math (Libertinus Math has MS Word issues and Greek italics are of suboptimal quality. I never tested for LaTeX issues).


# Best Monospace

First of all OTF and TTF versions of **every** font have different display weight on Windows on small sizes for some reason (see [this](https://github.com/adobe-fonts/source-sans-pro/issues/170) and [that](https://github.com/adobe-fonts/source-sans-pro/issues/200)) hence use TTF version as it looks closer to original design.

Monospace fonts used for main fonts and fallbacks do support:

* LGC (Latin, Greek, Cyrillic): Robotization Mono, Inconsolata Sugar, Sourcing Code Pro, Noto Sans Mono, IBM Plex Mono, DejaVu Sans Mono, Cousine.
* CJK variants (Chinese, Japanese, Korean): Source Han Sans (Not monospace but of width 1.5. E.g. 2 Source Han Sans == 3 Robotization Mono)
* Hebrew: Cousine.
* Math fallbacks: ST1X Two Math For Robot0 Mono, Symbola For Robot0 Mono, Noto Sans Mono, IBM Plex Mono, DejaVu Sans Mono.
  * for Consolas: DejaVu Sans Mono For Conso1as, ST1X Two Math For Conso1as, Symbola For Conso1as

Main fonts and fallback chains were optimized for [SugarTeX](https://github.com/kiwi0fruit/sugartex).


## [Roboto Mono](https://en.wikipedia.org/wiki/Roboto#Roboto_Mono)

#### (by Steve Matteson and Christian Robertson), [Preview](https://fonts.google.com/specimen/Roboto+Mono), [Download Robotization Mono](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/RobotizationMono.zip?raw=true), [Backup](https://github.com/kiwi0fruit/fonts/tree/master/apache/robotomono)

*My favorite!*

Italic in Roboto Mono has different width so it's recommended to use [**Robotization Mono**](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/RobotizationMono.zip?raw=true) fork that is simply a renamed monospacified version of Roboto Mono (but also without light and thin styles).

Font fallback chain: `'Robotization Mono', 'Noto Sans Mono', 'IBM Plex Mono', 'DejaVu Sans Mono', Cousine, 'ST1X Two Math For Robot0 Mono', 'Symbola For Robot0 Mono', 'Source Han Sans', monospace`.

Fallback fonts:

* 1st Unicode fallback: [Noto Sans Mono](https://en.wikipedia.org/wiki/Noto_fonts) (by Steve Matteson and Google), [Preview](https://www.google.com/get/noto/#sans-mono), [Download](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/NotoSansMono-hinted.zip?raw=true), [Download original latest version](https://www.google.com/get/noto/#sans-mono).
* Some arrows fallback: [IBM Plex Mono](https://github.com/IBM/plex) (by Mike Abbink), [Preview](https://fonts.google.com/specimen/IBM+Plex+Mono), [Download](https://fonts.google.com/specimen/IBM+Plex+Mono), [Download latest version](https://github.com/IBM/plex/releases), [Backup](https://github.com/kiwi0fruit/plex/tree/master/IBM-Plex-Mono/fonts/complete/otf),
* 2nd Unicode fallback: [DejaVu Sans Mono](https://dejavu-fonts.github.io/) (by Jim Lyles and others), [Preview](https://fontlibrary.org/ru/font/dejavu-sans-mono), [Download](https://github.com/dejavu-fonts/dejavu-fonts/releases),  [Backup](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/DejaVu), [Backup2](https://github.com/kiwi0fruit/dejavu-fonts),
* Hebrew and 3rd Unicode fallback: [Cousine](https://fonts.google.com/specimen/Cousine) (by Steve Matteson), [Preview](https://fonts.google.com/specimen/Cousine), [Download](https://fonts.google.com/specimen/Cousine), [Download2](https://github.com/google/fonts/tree/master/apache/cousine), [Backup](https://github.com/kiwi0fruit/fonts/tree/master/apache/cousine),
* Math fallback, Final Unicode fallback: [STIX Two Math and Symbola for Roboto Mono](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/fallback_roboto_mono.zip?raw=true),
* CJK fallback: Source Han Sans (by Adobe and Google), **Preview**: [JP](https://fonts.adobe.com/fonts/source-han-sans-japanese), [CN](https://fonts.adobe.com/fonts/source-han-sans-simplified-chinese), [KR](https://fonts.adobe.com/fonts/source-han-sans-korean), [HK](https://fonts.adobe.com/fonts/source-han-sans-hong-kong), [TW](https://fonts.adobe.com/fonts/source-han-sans-traditional-chinese), [Download Language-specific OTFs (Japanese is default)](https://github.com/adobe-fonts/source-han-sans/tree/release#language-specific-otfs), [Download other options](https://github.com/adobe-fonts/source-han-sans/tree/release), [Source code](https://github.com/adobe-fonts/source-han-sans), [Backup](https://github.com/kiwi0fruit/source-han-sans).


## [Inconsolata](https://en.wikipedia.org/wiki/Inconsolata)

#### (by Raph Levien and others), [Preview](https://fontlibrary.org/en/font/inconsolata-lgc), [Preview2](https://fonts.google.com/specimen/Inconsolata), [Download Inconsolata Sugar](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/InconsolataSugar.zip?raw=true), [Backup](https://github.com/kiwi0fruit/Inconsolata-LGC)

Inconsolata lacks italics, Cyrillic and Greek. Inconsolata LGC lacks some whitespace characters, has off-style backtick, italic Latin a and Cyrillic д are controversial design decisions. For SugarTeX it's recommended to use [**Inconsolata Sugar**](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/InconsolataSugar.zip?raw=true) fork that is simply a renamed Inconsolata LGC with these issues fixed (backtick was simply removed so one from fallback would be used).

Font fallback chain: `'Inconsolata Sugar', 'Robotization Mono', 'Noto Sans Mono', 'IBM Plex Mono', 'DejaVu Sans Mono', Cousine, 'ST1X Two Math For Robot0 Mono', 'Symbola For Robot0 Mono', 'Source Han Sans', monospace`.


## [Source Code Pro](https://github.com/adobe-fonts/source-code-pro)

#### (by Paul D. Hunt and Teo Tuominen), [Preview](https://adobe-fonts.github.io/source-code-pro/), [Download Sourcing Code Pro](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/SourcingCodePro.zip?raw=true), [Backup](https://github.com/kiwi0fruit/source-code-pro)

Source Code Pro lacks some whitespace characters and has broken division slash. For SugarTeX it's recommended to use [**Sourcing Code Pro**](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/SourcingCodePro.zip?raw=true) fork that is simply a renamed Source Code Pro with these issues fixed.

Font fallback chain: `'Sourcing Code Pro', 'Noto Sans Mono', 'IBM Plex Mono', 'DejaVu Sans Mono', Cousine, 'ST1X Two Math For Robot0 Mono', 'Symbola For Robot0 Mono', 'Source Han Sans', monospace`.


## Proprietary

### [Consolas](https://en.wikipedia.org/wiki/Consolas)

#### (by Lucas de Groot)

This is a **proprietary** font but included here for [SugarTeX](https://github.com/kiwi0fruit/sugartex) installation instruction.

It's preinstalled with Windows. Consolas can also be installed together with [Microsoft PowerPoint Viewer](https://www.microsoft.com/en-us/download/details.aspx?id=13) till April, 2018. SHA256: 249473568EBA7A1E4F95498ACBA594E0F42E6581ADD4DEAD70C1DFB908A09423. But note that it's license says that "You may use the software only to view and print files created with Microsoft Office software. You may not use the software for any other purpose." so you *might* not be even allowed to print Consolas font text from LibreOffice. But at the same time if you incorporate Microsoft Word into your pipeline (for example even if postprocessing .docx files by other software as a next step) you *might* satisfy "created with Microsoft Office software". And printing to PDF via Chrome browser *might* also be printing.

Font fallback chain: `Consolas, 'DejaVu Sans Mono For Conso1as', 'ST1X Two Math For Conso1as', 'Symbola For Conso1as', 'Source Han Sans', monospace`

Fallback fonts:

* [DejaVu Sans Mono, STIX Two Math and Symbola for Consolas](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/fallback_consolas.zip?raw=true).


## Other fonts
Font fallback chains contain fonts monospacified via [monospacifier.py](https://github.com/cpitclaudel/monospacifier) ([Backup](https://github.com/kiwi0fruit/monospacifier)). If you don't like Consolas, Roboto Mono,  Source Code Pro or Inconsolata that much you can pick [there](https://github.com/cpitclaudel/monospacifier) monospacified fallbacks for other monospace fonts.


# [MacType](https://github.com/snowie2000/mactype)

If on Windows it's recommended to install [MacType](http://www.mactype.net/) because Windows original ClearType is capable of rendering only fonts that were pre-optimized for ClearType - it cannot display arbitrary font in a beautiful way (or capable but for some reason doesn't do that on default settings!). MacType can do it (and does with default settings). Now that Full HD is everywhere it's a shame for ClearType.

**Important**:

* Use Default profile but change ini setting to `NormalWeight=8` (or even `NormalWeight=0` instead of 16) (with this the [difference between Chrome and other programs](https://github.com/snowie2000/mactype/issues/402) is not so big). Also launch Chrome using the `--disable-directwrite-for-ui` command switch,
* In case of Firefox you should fix some settings: open `about:config` then:
    * change `gfx.content.azure.backends` from `direct2d1.1,skia,cairo` to `direct2d1.1,cairo`,
    * change `gfx.canvas.azure.backends` from `direct2d1.1,skia,cairo` to `direct2d1.1,cairo`,
    * change `gfx.direct2d.disabled` to `true` (unfortunately FF can't use non-standard font weights with this setting...),
* MacType can clash with cheap Antiviruses though. In my case the problem was solved by deleting AVG/Avast and installing Kaspersky Free (Kaspersky IS is also OK).
* Some programs need special config settings. For example PyCharm:
```ini
[Experimental@pycharm64.exe]
ClipBoxFix=1
[General@pycharm64.exe]
;PyCharm fix + Consolas
NormalWeight=-14
BoldWeight=-4
```
See details about other programs in [this repo](https://github.com/wspl/mactype-hack).

Actually MacType can be tuned. Here is my custom part of the config that tunes Consolas font to look thinner and also makes fonts in Explorer look thicker:
```ini
;Update appropriate sections:
[General]
NormalWeight=0
BoldWeight=0
[Individual]
Times New Roman=0,,4,,,
Segoe UI=0,,4,,,
Tahoma=0,,4,,,

;Paste to the end:
[Experimental@pycharm64.exe]
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
NormalWeight=16
```


# [Stylebot](https://github.com/ankit/stylebot)

**UPD:** *You can also try [Stylus](https://github.com/openstyles/stylus) (GPL) or [Stylish](https://en.wikipedia.org/wiki/Stylish) (Freeware)*

Stylebot is an open source Google Chrome extension that allows users to manipulate a web page’s appearance. [Install](https://chrome.google.com/webstore/detail/stylebot/oiaejidbmkiecgbjeifoejpgmdaleoha).

1. Incrementally build custom stylesheets for Chrome.
2. Save custom CSS rules for sites. The next time they visit a site, their custom CSS is already applied.
3. Export and import created styles.

I haven't checked if it's safe. But it looks safe.

This extesnion would help you to make internet less messy in style :-)

And even more! Stylebot can fix issues that arise from thinner fonts in Chrome with [MacType](#mactype): swap badly looking fonts. For example add this to the Global Stylesheet:


```css
@font-face {
  font-family: 'Times New Roman';
  src: local("Linus Libertini O RRegular");
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'Times New Roman';
  src: local("Linus Libertini O BBold");
  font-weight: bold;
  font-style: normal;
}
@font-face {
  font-family: 'Times New Roman';
  src: local("Linus Libertini O IItalic");
  font-weight: normal;
  font-style: italic;
}
@font-face {
  font-family: 'Times New Roman';
  src: local("Linus Libertini O BBoldIItalic");
  font-weight: bold;
  font-style: italic;
}
```
You need to install Linus Libertini to make it work. And in order to fix [Chrome bug](https://bugs.chromium.org/p/chromium/issues/detail?id=627143) you need to install special font families from [this OTF archive](https://github.com/kiwi0fruit/open-fonts/raw/master/Fonts/linus_libertini_o_font_swap_chrome_bugfix.zip) (or [this TTF archive](https://github.com/kiwi0fruit/open-fonts/raw/master/Fonts/linus_libertini_font_swap_chrome_bugfix.zip)) that were easily renamed via FontForge (TTF is heavier on small sizes).

Or you can use online fonts:

```css
@font-face {
  font-family: 'Times New Roman';
  src: url("https://github.com/kiwi0fruit/open-fonts/raw/master/Fonts/LibertinusSerif/LibertinusSerif-Regular.otf") format("opentype");
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'Times New Roman';
  src: url("https://github.com/kiwi0fruit/open-fonts/raw/master/Fonts/LibertinusSerif/LibertinusSerif-Bold.otf") format("opentype");
  font-weight: bold;
  font-style: normal;
}
@font-face {
  font-family: 'Times New Roman';
  src: url("https://github.com/kiwi0fruit/open-fonts/raw/master/Fonts/LibertinusSerif/LibertinusSerif-Italic.otf") format("opentype");
  font-weight: normal;
  font-style: italic;
}
@font-face {
  font-family: 'Times New Roman';
  src: url("https://github.com/kiwi0fruit/open-fonts/raw/master/Fonts/LibertinusSerif/LibertinusSerif-BoldItalic.otf") format("opentype");
  font-weight: bold;
  font-style: italic;
}
```


# Build

1. [Install FontForge](https://fontforge.github.io/en-US/downloads/)
2. Run `update_deps.bat` from repo's directory,
3. Run appropriate batch script from repo's directly.


# TO DO

[TO DO list](to-do.md) of ideas that I have or had about font development.

Backup repos:

* [DejaVu](https://github.com/kiwi0fruit/dejavu-fonts),
* [STIX](https://github.com/kiwi0fruit/stixfonts),
* [Lato](https://github.com/kiwi0fruit/lato-source),
* [Source Sans Pro](https://github.com/kiwi0fruit/source-sans-pro),
* [Roboto, Roboto Mono, PT Sans, Open Sans](https://github.com/kiwi0fruit/fonts),
* [Source Serif Pro](https://github.com/kiwi0fruit/source-serif-pro),
* [Source Code Pro](https://github.com/kiwi0fruit/source-code-pro),
* [IBM Plex Mono](https://github.com/kiwi0fruit/plex),
* [Vollkorn](https://github.com/kiwi0fruit/Vollkorn-Typeface),
* [Libertinus](https://github.com/kiwi0fruit/libertinus),
* [Inconsolata LGC](https://github.com/kiwi0fruit/Inconsolata-LGC),
* [Monospacifier](https://github.com/kiwi0fruit/monospacifier).
