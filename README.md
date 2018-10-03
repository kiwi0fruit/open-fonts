# Open Fonts

A collection of beautiful free and open source fonts: instructions for installing, Unicode fallback chains, instructions to replace Windows ClearType and fix browser fonts.

Contents:

* [Best Sans Serif](#best-sans-serif)
* [Best Serif](#best-serif)
* [Best Monospace](#best-monospace)
* [MacType](#mactype)
* [Stylebot](#stylebot)
* [Build](#build)
* [TODO](#todo)


# Best Sans Serif

## [Noto Sans](https://fonts.google.com/specimen/Noto+Sans) LGC (by Steve Matteson and Google), [Download](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/NotoSans-hinted.7z?raw=true), [Download](https://www.google.com/get/noto/)

Fallback fonts:

* 1st Unicode fallback: [DejaVu Sans](https://fontlibrary.org/en/font/dejavu-sans), [Download](https://dejavu-fonts.github.io/Download.html),
* Math fallback: [STIX Two Math](http://www.stixfonts.org/) (by STI Pub consortium), [Download](https://sourceforge.net/projects/stixfonts/),
* Final Unicode fallback: [Symbola](https://fontlibrary.org/en/font/symbola) (by George Douros), [Download](https://fontlibrary.org/en/font/symbola),
* CJK fallback: Noto Sans CJK TC Regular (by Google), [Download](https://www.google.com/get/noto/) (search for Noto Sans CJK). TC is Traditional Chinese but it can also be SC, JP, KR.

Font fallback chain: `'Noto Sans', 'DejaVu Sans', 'STIX Two Math', Symbola, 'Noto Sans CJK TC Regular', sans-serif`.


## [Lato](https://fonts.google.com/specimen/Lato) (by Łukasz Dziedzic), [Download](http://www.latofonts.com/) (latest version here)

I think Lato better accompanies Libertinus Serif than Noto Sans does.

Font fallback chain: `Lato, 'Noto Sans', 'DejaVu Sans', 'STIX Two Math', Symbola, 'Noto Sans CJK TC Regular', sans-serif`.


## [Source Sans Pro](https://fonts.google.com/specimen/Source+Sans+Pro) (by Paul D. Hunt), [Download](https://fonts.google.com/specimen/Source+Sans+Pro), [Download](https://github.com/google/fonts/tree/master/ofl/sourcesanspro)

*My favorite!*

Fallback fonts:

* Cyrillic fallback: [PT Sans](https://fonts.google.com/specimen/PT+Sans) (by Alexandra Korolkova), [Download](https://fonts.google.com/specimen/PT+Sans), [Download](https://github.com/google/fonts/tree/master/ofl/ptsans).

Font fallback chain: `'Source Sans Pro', 'PT Sans', 'Noto Sans', 'DejaVu Sans', 'STIX Two Math', Symbola, 'Noto Sans CJK TC Regular', sans-serif`.


# Best Serif

## [Libertinus Serif](https://github.com/khaledhosny/libertinus) (by Philipp H. Poll, fork by Khaled Hosny), [Download](https://github.com/libertinus-fonts/libertinus/releases), [Preview](https://fontlibrary.org/en/font/libertinus-serif)

*My favorite!*

Libertinus Serif is poorly supported by Windows ClearType. WS Word 2007 renders it ugly. Chrome with ClearType renders it nicely though. It's really beautiful on Linux, MacOS or Windows with [MacType](#mactype).

Fallback fonts:

* Cyrillic fallback: [PT Astra Serif](https://github.com/google/fonts/issues/565) (by Alexandra Korolkova and Isabella Chaeva) - that is a nice font too, [Download](http://www.paratype.ru/uni/public/PTAstraSerif.zip) (for Cyrillic bold-italic). [Here](https://github.com/khaledhosny/libertinus/issues/74) you can see how good PT Astra Serif mixes with Linux Libertine.
* 1st Unicode fallback: [Tinos](https://fonts.google.com/specimen/Tinos) (by Steve Matteson), [Download](https://fonts.google.com/specimen/Tinos), [Download](https://github.com/google/fonts/tree/master/apache/tinos),
* 2nd Unicode fallback: [Noto Serif](https://fonts.google.com/specimen/Noto+Serif) LGC (by Steve Matteson and Google), [Download](https://github.com/kiwi0fruit/open-fonts/blob/master/Fonts/NotoSerif-hinted.7z?raw=true), [Download](https://www.google.com/get/noto/),
* Math fallback: [STIX Two Math](http://www.stixfonts.org/) (by Ross Mills and John Hudson), [Download](https://sourceforge.net/projects/stixfonts/),
* Final Unicode fallback: [Symbola](https://fontlibrary.org/en/font/symbola) (by George Douros), [Download](https://fontlibrary.org/en/font/symbola),
* CJK fallback: Noto Serif CJK TC (by Google), [Download](https://www.google.com/get/noto/) (search for Noto Serif CJK). TC is Traditional Chinese but it can also be SC, JP, KR.

Font fallback chain: `'Libertinus Serif', 'PT Astra Serif', 'Libertinus Math', Tinos, 'STIX Two Math', 'Noto Serif', Symbola, 'Noto Serif CJK TC', serif`.

Worth mentioning [Libertinus Math](https://github.com/khaledhosny/libertinus) ([Download](https://github.com/libertinus-fonts/libertinus/releases), [Preview](https://fontlibrary.org/en/font/libertinus-math)) that is a Libertinus Serif version for OpenType math-capable applications like LuaTeX, XeTeX or MS Word 2007+.


## [STIX Two Text](http://www.stixfonts.org/) (by Ross Mills and John Hudson), [Download](https://sourceforge.net/projects/stixfonts/)

Font fallback chain: `'STIX Two Text', 'STIX Two Math', 'Noto Serif', Symbola, 'Noto Serif CJK TC', serif`.

Worth mentioning [STIX Two Math](http://www.stixfonts.org/) ([Download](https://sourceforge.net/projects/stixfonts/)) that is a STIX Two version for OpenType math-capable applications like LuaTeX, XeTeX or MS Word 2007+.


# Best Monospace

## [Roboto Mono](https://fonts.google.com/specimen/Roboto+Mono) (by Christian Robertson).

Italic in Roboto Mono has different width so it's recommended to use **Open Mono** fork that is simply a renamed monospacified version of Roboto Mono.

See best fallback chain for Roboto Mono in the [SugarTeX docs](https://github.com/kiwi0fruit/sugartex#atom-editor-with-full-unicode-support).

***Additional info:*** There are also instructions for installing fallback chain for Consolas (by Luc(as) de Groot) that is the best ClearType optimized monospace font if on Windows. It looks too thick on big sizes but in Chromium based Atom editor with [MacType](#mactype) default profile it looks excellent.


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
git clone --depth=1 https://github.com/kiwi0fruit/fonts
git clone https://github.com/kiwi0fruit/monospacifier
git clone https://github.com/kiwi0fruit/open-fonts
# copy `consola.ttf` to local open-fonts repo folder
```
3. Run appropriate batch script


# TO DO

[TO DO list](to-do.md) of ideas that I have or had about font development.
