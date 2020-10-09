# Language variants and Math support

Browsers, Pandoc, MS Word and LibreOffice support language variants inside single font and math formulas. For details on language variants see example of Cyrillic variants in Source Sans Pro [preview](https://localfonts.eu/freefonts/traditional-cyrillic-free-fonts/source-sans-pro/).

Worth mentioning that LibreOffice math support is not ideal. See LibreOffice section below for details. Only paid version of MS Word supports math formulas.

* **Browsers** support language variants via `lang="bg-BG"` (`"zh-CN"`, `"zh-TW"`, `"zh-HK"`, `"ja-JP"`, `"ko-KR"`) HTML property. Browsers support math via MathJax and KaTeX (Chromium still [doesn't support MathML](https://mathml.igalia.com/)).
* **Microsoft Word** desktop (paid) since some version supports language variants (2007 version does **not** support it). And it supports nice math formulas since 2007 version. Free [Microsoft 365](https://www.office.com) online supports it too (I wasn't able to change/add language there but already set language is rendered correctly) but it doesn't support math formulas editing (but they are rendered nicely).
* **LibreOffice** since some version supports language variants (v.7.0.1 does support it). For CJK first enable `Tools / Options / Language Settings / Languages / Default languages for documents / Asian`. See [CJK document example](./cjk-test). But the built-in LO math renderer is very bad (not the math editor that is somewhat OK). Hence you have options:
  * Use `.otd` format only and try TexMaths extension for LaTeX support. And optionally install WYSIWYM editor LyX and copypaste back and forth TeX formulas for easy WYSIWYM editing. But mind that TexMaths is buggy (I wasn't able to get it working on Windows 7 at all). See LyX quick templates [in this dir](./math_formulas) (`*.lyx` files) to speed up copypasting a bit.
  * Use `.docx` format only and write math in LibreOffice built-in math editor. It's not great but OK. Math would be saved in Microsoft Word compatible format. But to preview the document as it **should** be rendered you would need use some version of Microsoft Word. If you purchaised modern MS Word it's better to use it instead of LibreOffice. But in addition to paid options you can use:
    1. [Microsoft 365](https://www.office.com) online. But you would need to upload files to view and edit them (no math editing though). [OneDrive](https://onedrive.live.com/) sync application would make it more convenient. Edit mode would even use fonts from you computer and have language variants (I wasn't able to change/add language there but already set language is rendered correctly). Math would be rendered in different font than in desktop and mobile apps though. But both preview mode and to PDF conversion would not be able to use your local fonts and **would not** be able to use font language variants. You can still embed fonts to the document but the server will only use regular style. To overcome this severe limit you may use special fonts like [Embed Serif](./Fonts/EmbedSerif) that is 6 different font families collection made from Source Serif Pro where each font is a renamed single style. If you need language variant you would have to create a special font for it. Not a conveniet workflow unless you would stick to standard fonts provided by Microsoft.
    2. Install Android's [Microsoft Word](https://play.google.com/store/apps/details?id=com.microsoft.office.word&hl=en_US&gl=US). You can install it inside some runtime environment. I use [BlueStacks](https://www.bluestacks.com/) as it installs and works out of the box. Android's Microsoft Word to PDF conversion would have all flaws of Microsoft 365 online mentioned above and in addition it reqiures internet and buggy (PDF preview is OK but Android saves PDF to empty file for some reason). App's preview/edit mode would display math in right font and use font language variants (albeight buggy - I wasn't able to figure out why it doensn't work sometimes). But preview/edit mode cannot use your custom fonts hence you would need to embed fonts and use workarounds like [Embed Serif](./Fonts/EmbedSerif). If you stick to standard fonts provided by Microsoft then it would be OK though.
* **Pandoc** supports language variants for inline text via `[inline text]{lang="ru-RU"}` (span). And for paragraphs (div):
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
  I only tested that this would work when exporting to html. It should work for docx too. As about math support:
  * Math would work when exporting to html just like it would work in browsers.
  * When exporting to LaTeX/LaTeX+PDF math would surely work.
