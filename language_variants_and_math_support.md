# Language variants and Math support

Browsers, Pandoc, MS Word and LibreOffice support language variants inside single font and math formulas. For details on language variants see example of Cyrillic variants in Source Sans Pro [preview](https://localfonts.eu/freefonts/traditional-cyrillic-free-fonts/source-sans-pro/).

Worth mentioning that LibreOffice math support is not ideal. See LibreOffice section below for details. Only paid version of MS Word supports math formulas.


### Browsers

**Browsers** support language variants via `lang="bg-BG"` (`"zh-CN"`, `"zh-TW"`, `"zh-HK"`, `"ja-JP"`, `"ko-KR"`) HTML property. Browsers support math via MathJax and KaTeX (Chromium still [doesn't support MathML](https://mathml.igalia.com/)).


### Microsoft Word

**Microsoft Word desktop** (paid) since some version supports language variants (2007 version does **not** support it). And it supports nice math formulas since 2007 version. Free [Microsoft 365](https://www.office.com) online supports language variants too (I wasn't able to change/add language there but already set language is rendered correctly) but it doesn't support math formulas editing (but they are rendered nicely).


### LibreOffice

**LibreOffice** since some version supports language variants (v.7.0.1 does support it). For CJK first enable `Tools / Options / Language Settings / Languages / Default languages for documents / Asian`. See [CJK document example](./cjk-test). But the built-in LO math renderer is very bad (not the math editor that is somewhat OK). Hence you have options:

* Use `.otd` format only and try TexMaths extension for LaTeX support. And optionally install WYSIWYM editor LyX and copypaste back and forth TeX formulas for easy WYSIWYM editing. But mind that TexMaths is buggy (I wasn't able to get it working on Windows 7 at all). See LyX quick templates [in this dir](./math_formulas) (`*.lyx` files) to speed up copypasting a bit.
* Use `.docx` format only and write math in LibreOffice built-in math editor. It's not great but OK. Math would be saved in Microsoft Word compatible format. But to preview the document as it **should** be rendered you would need use some version of Microsoft Word. If you purchaised modern MS Word it's better to use it instead of LibreOffice. But in addition to paid options you can use:
  1. [Microsoft 365](https://www.office.com) online. But you would need to upload files to view and edit them (no math editing though). [OneDrive](https://onedrive.live.com/) sync application would make it more convenient. Edit mode would even use fonts from you computer and have language variants (I wasn't able to change/add language there but already set language is rendered correctly). Math would be rendered in different font than in desktop and mobile apps though. But both preview mode and to PDF conversion would not be able to use your local fonts and **would not** be able to use font language variants. You can still embed fonts to the document but the server will only use regular style (I only tested embedding made by LibreOffice). To overcome this severe limit you may use special fonts like [Embed Serif](./Fonts/EmbedSerif) that is 6 different font families collection made from Source Serif Pro where each font is a renamed single style. If you need language variant you would have to create a special font for it. Not a conveniet workflow unless you would stick to standard fonts provided by Microsoft (there is no Noto CJK fonts support - embedding them would be inconvenient).
  2. Install Android's [Microsoft Word](https://play.google.com/store/apps/details?id=com.microsoft.office.word&hl=en_US&gl=US). You can install it inside some runtime environment. I use [BlueStacks](https://www.bluestacks.com/) as it installs and works out of the box. Android's Microsoft Word to PDF conversion would have all flaws of Microsoft 365 online mentioned above and in addition it reqiures internet and buggy (PDF preview is OK but occasionally Android saves PDF to empty file for some reason). App's preview/edit mode would display math in right font and use font language variants (albeight buggy - I wasn't able to figure out why it doensn't work sometimes). But preview/edit mode cannot use your custom fonts hence you would need to embed fonts and use workarounds like [Embed Serif](./Fonts/EmbedSerif). If you stick to standard fonts provided by Microsoft then it would be OK though (there is no Noto CJK fonts support - embedding them would be inconvenient).


### Pandoc

**Pandoc** supports language variants for inline text via `[inline text]{lang="ru-RU"}` (span). And for paragraphs (div):

```md
::: {lang="bg-BG"}
Paragraph text.
:::
```
Or setting global document language:
```yaml
---
lang: bg
---
```
I only tested that this would work when exporting to HTML. It should work for docx too. As about math support:

* Math would work when exporting to HTML just like it would work in browsers. Though on Linux HTML+PDF export may have kerning issues (that might be related to using TrueType ttf fonts). See [pandoctools](https://github.com/kiwi0fruit/pandoctools) and [pyppdf](https://github.com/kiwi0fruit/pyppdf) for more about HTML+PDF export.
* Math would surely work when exporting to LaTeX/LaTeX+PDF.
* Math would work with caveats when exporting to docx/docx+PDF. First problem arise from the fact that Pandoc stores math in LaTeX when MS Word and LibreOffice use their own formats that don't match perfectly. Second problem is that when Pandoc exports to docx document it applies styles to formulas too. Hence when Word opens the documents it tries to apply general text styles to math. That looks bad. In order to fix this you would need to open Pandoc output docx file via LibreOffice and save it. This would erase any styles on formulas - even the intended ones. But default Cambria Math is quite nice hence there is little point in changing it. You can also embed fonts on this step as you [can not embed](https://github.com/jgm/pandoc/issues/6728) fonts to the pandoc template. Surely you can open and fix formulas in MS Word too. But in case of free software only (LO) you get the following math transform: Pandoc's LaTeX => MS Word's format => LibreOffice format compatible with MS Word. Pandoc's LaTeX doesn't support functions operators from MS Word but it still looks OK as it can still use math roman (non italic) symbols that would give the same result. But math roman words would lose style and be split into separate symbols by LibreOffice.
* Hence for `sin x` you would need to use `\textrm{sin }x` (LaTeX) or `‹sin ›x` ([SugarTeX](https://github.com/kiwi0fruit/sugartex)). And for all math roman you would need to use text roman instead (`\sin x` would also give text roman but without space between sin and x). Bold italic and bold regular would turn into simple italic too. Hence using `𝒙` and `𝐱` (that are bold italic x and bold regular x from Unicode math section) is the only option left. But using them would break LyX.
