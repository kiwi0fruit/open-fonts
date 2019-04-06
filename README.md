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


# Best Sans Serif

## [Noto Sans](https://en.wikipedia.org/wiki/Noto_fonts) LGC

### (by Steve Matteson and Google), [Preview](https://fonts.google.com/specimen/Noto+Sans), [Download latest version](https://www.google.com/get/noto/#sans-lgc), [Backup](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/NotoSans-hinted.zip?raw=true)

Fallback fonts:

* 1st Unicode fallback: [DejaVu Sans](https://dejavu-fonts.github.io/) (by Jim Lyles and others), [Preview](https://fontlibrary.org/en/font/dejavu-sans), [Download](https://github.com/dejavu-fonts/dejavu-fonts/releases),  [Backup](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/DejaVu), [Backup2](https://github.com/kiwi0fruit/dejavu-fonts),
* Math fallback: STIX Two Math (see below),
* Final Unicode fallback: [Symbola](http://users.teilar.gr/~g1951d/) (by George Douros), [Preview](https://fontlibrary.org/en/font/symbola), [Download latest version](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/hintedSymbola.ttf?raw=true), [Backup](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/hintedSymbola.ttf?raw=true),
* CJK fallback: Noto Sans CJK TC Regular (by Google), [Download](https://www.google.com/get/noto/) (search for Noto Sans CJK). TC is Traditional Chinese but it can also be SC, JP, KR.

Font fallback chain: `'Noto Sans', 'DejaVu Sans', 'STIX Two Math', Symbola, 'Noto Sans CJK TC Regular', sans-serif`.


## [Lato](http://www.latofonts.com)

### (by Łukasz Dziedzic), [Preview](https://localfonts.eu/freefonts/traditional-cyrillic-free-fonts/lato/), [Download latest version](http://www.latofonts.com/lato-free-fonts/#download), [Backup](https://github.com/kiwi0fruit/open-fonts/tree/master/Fonts/Lato), [Backup2](https://github.com/kiwi0fruit/lato-source)

Font fallback chain: `Lato, 'Noto Sans', 'DejaVu Sans', 'STIX Two Math', Symbola, 'Noto Sans CJK TC Regular', sans-serif`.


## [Source Sans Pro](https://github.com/adobe-fonts/source-sans-pro)

### (by Paul D. Hunt), [Preview](https://fonts.google.com/specimen/Source+Sans+Pro), [Download latest version](https://github.com/adobe-fonts/source-sans-pro/releases), [Backup](https://github.com/kiwi0fruit/source-sans-pro)

*My favorite!*

Fallback fonts:

* Cyrillic fallback: [PT Sans](https://en.wikipedia.org/wiki/PT_Fonts) (by Alexandra Korolkova), [Preview](https://fonts.google.com/specimen/PT+Sans), [Download](https://fonts.google.com/specimen/PT+Sans), [Download2](https://github.com/google/fonts/tree/master/ofl/ptsans), [Backup](https://github.com/kiwi0fruit/fonts/tree/master/ofl/ptsans)

Font fallback chain: `'Source Sans Pro', 'PT Sans', 'Noto Sans', 'DejaVu Sans', 'STIX Two Math', Symbola, 'Noto Sans CJK TC Regular', sans-serif`.


# Best Serif

## [STIX Two Text](http://www.stixfonts.org/)

### (by Ross Mills and John Hudson), [Preview](https://localfonts.eu/freefonts/traditional-cyrillic-free-fonts/stix/), [Download](https://github.com/stipub/stixfonts), [Backup](https://github.com/kiwi0fruit/stixfonts)

Fallback fonts:

* 1st Unicode fallback: [Noto Serif](https://en.wikipedia.org/wiki/Noto_fonts) LGC (by Steve Matteson and Google), [Preview](https://fonts.google.com/specimen/Noto+Serif), [Download latest version](https://www.google.com/get/noto/#serif-lgc), [Backup](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/NotoSerif-hinted.zip?raw=true)
* Math fallback: STIX Two Math (see below),
* Final Unicode fallback: [Symbola](http://users.teilar.gr/~g1951d/) (by George Douros), [Preview](https://fontlibrary.org/en/font/symbola), [Download latest version](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/hintedSymbola.ttf?raw=true), [Backup](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/hintedSymbola.ttf?raw=true),
* CJK fallback: Noto Serif CJK TC (by Google), [Download](https://www.google.com/get/noto/) (search for Noto Serif CJK). TC is Traditional Chinese but it can also be SC, JP, KR.

Font fallback chain: `'STIX Two Text', 'STIX Two Math', 'Noto Serif', Symbola, 'Noto Serif CJK TC', serif`.


## [STIX Two Math](http://www.stixfonts.org/)

### (by Ross Mills and John Hudson), [Download](https://github.com/stipub/stixfonts/releases), [Backup](https://github.com/kiwi0fruit/stixfonts)

Worth mentioning [STIX Two Math](http://www.stixfonts.org/) that is a STIX Two version for OpenType math-capable applications like LuaTeX, XeTeX or MS Word 2007+.


## [Source Serif Pro](https://github.com/adobe-fonts/source-serif-pro)

### (by Frank Grießhammer), [Preview](https://fonts.google.com/specimen/Source+Serif+Pro), [Download latest version](https://github.com/adobe-fonts/source-serif-pro/releases), [Backup](https://github.com/kiwi0fruit/source-serif-pro)

It's not finished yet. But it is very promising. Latin italic [**was released**](https://blog.typekit.com/2018/08/16/source-serif-italics/) and

> The Italics have Adobe Latin-3 support today, just like the first release of the Roman did. Naturally, the plan is to align the character support across all styles, so that there are Greek and Cyrillic italics as well as AL-4 support for it. With Google’s support, we’ve been able to enlist the help of Irene Vlachou and Emilios Theofanous to help draw the Greek Italic.


## [Vollkorn](http://vollkorn-typeface.com)

### (by Friedrich Althausen), [Preview](https://fonts.google.com/specimen/Vollkorn), [Download latest version](http://vollkorn-typeface.com/#download), [Backup](https://github.com/kiwi0fruit/Vollkorn-Typeface)

Font fallback chain: `Vollkorn, 'STIX Two Text', 'STIX Two Math', 'Noto Serif', Symbola, 'Noto Serif CJK TC', serif`.


## [Linux Libertine](http://libertine-fonts.org/)

### (by Philipp H. Poll and others), [Preview](https://localfonts.eu/freefonts/traditional-cyrillic-free-fonts/linux-libertine/), [Download Linus Libertini](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/LinusLibertini.zip?raw=true), [Backup](https://github.com/kiwi0fruit/libertinus)

Semibold italic Cyrillics are terrible in Linux Libertine. So it's recommended to use [**Linus Libertini**](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/LinusLibertini.zip?raw=true) fork that is simply a renamed Libertinus Serif without semibolds (Libertinus Serif is a bugfixed fork of Linux Libertine).

Font fallback chain: `'Linus Libertini', 'STIX Two Text', 'STIX Two Math', 'Noto Serif', Symbola, 'Noto Serif CJK TC', serif`.

There is also [Libertinus Math](https://github.com/libertinus-fonts/libertinus) font but I find it to be of lower quality than STIX Two Math (Libertinus Math has MS Word issues. Greek italics are of suboptimal quality. I never tested for LaTeX issues).


# Best Monospace

## [Roboto Mono](https://en.wikipedia.org/wiki/Roboto#Roboto_Mono)

## (by Christian Robertson), [Preview](https://fonts.google.com/specimen/Roboto+Mono), [Download Open Mono](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/OpenMono.zip?raw=true), [Backup](https://github.com/kiwi0fruit/fonts/tree/master/apache/robotomono)

Italic in Roboto Mono has different width so it's recommended to use [**Open Mono**](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/OpenMono.zip?raw=true) fork that is simply a renamed monospacified version of Roboto Mono.

Best fallback chain for Roboto Mono: `'Open Mono', 'Noto Sans Mono', 'IBM Plex Mono', 'DejaVu Sans Mono', 'STI0 Two Mat0 monospacified for Robot0 Mono', 'Symbola monospacified for DejaVu Sans Mono', 'Noto Sans CJK TC', monospace`.

Fallback fonts:

* [Noto Sans Mono](https://en.wikipedia.org/wiki/Noto_fonts) (by Steve Matteson and Google), [Preview](https://www.google.com/get/noto/#sans-mono), [Download](https://www.google.com/get/noto/#sans-mono), [Backup](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/NotoSansMono-hinted.zip?raw=true),
* [IBM Plex Mono](https://github.com/IBM/plex) (by Mike Abbink), [Preview](https://fonts.google.com/specimen/IBM+Plex+Mono), [Download latest version](https://github.com/IBM/plex/releases), [Backup](https://github.com/kiwi0fruit/plex/tree/master/IBM-Plex-Mono/fonts/complete/otf),
* [DejaVu Sans Mono](https://dejavu-fonts.github.io/) (by Jim Lyles and others), [Preview](https://fontlibrary.org/ru/font/dejavu-sans-mono), [Download](https://github.com/dejavu-fonts/dejavu-fonts/releases),  [Backup](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/DejaVu), [Backup2](https://github.com/kiwi0fruit/dejavu-fonts),
* [STIX Two Math monospacified for Roboto Mono](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/STI0TwoMat0_monospacified_for_Robot0Mono.ttf?raw=true),
* [Symbola monospacified for DejaVu Sans Mono](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/Symbola_monospacified_for_DejaVuSansMono.ttf?raw=true),
* CJK fallback: Noto Sans CJK TC (by Google), [Download](https://www.google.com/get/noto/) (search for Noto Sans CJK). TC is Traditional Chinese but it can also be SC, JP, KR.

I used monospacified fonts obtained with the help of [monospacifier.py](https://github.com/cpitclaudel/monospacifier) ([Backup](https://github.com/kiwi0fruit/monospacifier)).


# [MacType](https://github.com/snowie2000/mactype)

If on Windows it's recommended to install [MacType](http://www.mactype.net/) because Windows original ClearType is capable of rendering only fonts that were pre-optimized for ClearType - it cannot display arbitrary font in a beautiful way. MacType can do it. Now that Full HD is everywhere it's a shame for ClearType.

**Important**:

* Use Default profile but change ini setting to `NormalWeight=8` (or even `NormalWeight=0` instead of 16) (with this the [difference between Chrome and other programs](https://github.com/snowie2000/mactype/issues/402) is not so big). Also launch Chrome using the `--disable-directwrite-for-ui` command switch,
* In case of Firefox you should fix some settings: open `about:config` then:
    * change `gfx.content.azure.backends` from `direct2d1.1,skia,cairo` to `direct2d1.1,cairo`,
    * change `gfx.canvas.azure.backends` from `direct2d1.1,skia,cairo` to `direct2d1.1,cairo`,
    * change `gfx.direct2d.disabled` to `true` (unfortunately FF can't use non-standard font weights with this setting...),
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

Actually MacType can be tuned. Here is my custom part of the config that tunes Consolas font to look thinner and also makes fonts in Explorer look thicker:
```ini
[General]
NormalWeight=0
BoldWeight=0
[Individual]
Times New Roman=0,,4,,,
Segoe UI=0,,4,,,
Tahoma=0,,4,,,
;...
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
  src: local("Libertinus Serif");
  font-weight: normal;
  font-style: normal;
}
@font-face {
  font-family: 'Times New Roman';
  src: local("Libertinus Serif BBold");
  font-weight: bold;
  font-style: normal;
}
@font-face {
  font-family: 'Times New Roman';
  src: local("Libertinus Serif IItalic");
  font-weight: normal;
  font-style: italic;
}
@font-face {
  font-family: 'Times New Roman';
  src: local("Libertinus Serif BBoldIt");
  font-weight: bold;
  font-style: italic;
}
```
You need to install Libertinus Serif to make it work. And in order to fix [Chrome bug](https://bugs.chromium.org/p/chromium/issues/detail?id=627143) you need to install special font families from [this archive](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/libertinus_serif_font_swap_chrome_bugfix.7z?raw=true) that were easily renamed via FontForge.


# Build

## Build Open Mono and DejaVu Sans Mono for Consolas

1. [Install FontForge](https://fontforge.github.io/en-US/downloads/windows/)
2. Clone Google Fonts, other fonts, Monospacifier and Open Fonts repos:
```sh
git clone --depth=1 https://github.com/google/fonts
git clone https://github.com/kiwi0fruit/monospacifier
git clone https://github.com/kiwi0fruit/open-fonts
# copy `consola.ttf` to local open-fonts repo folder
```
3. Run appropriate batch script


# TO DO

[TO DO list](to-do.md) of ideas that I have or had about font development.

Backup repos:

* [DejaVu](https://github.com/kiwi0fruit/dejavu-fonts),
* [STIX](https://github.com/kiwi0fruit/stixfonts),
* [Lato](https://github.com/kiwi0fruit/lato-source),
* [Source Sans Pro](https://github.com/kiwi0fruit/source-sans-pro),
* [Roboto Mono, PT Sans](https://github.com/kiwi0fruit/fonts),
* [Source Serif Pro](https://github.com/kiwi0fruit/source-serif-pro),
* [IBM Plex Mono](https://github.com/kiwi0fruit/plex),
* [Vollkorn](https://github.com/kiwi0fruit/Vollkorn-Typeface),
* [Libertinus](https://github.com/libertinus-fonts/libertinus),
* [Monospacifier](https://github.com/kiwi0fruit/monospacifier).
