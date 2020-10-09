# Language variants support

See example of Cyrillic variants in Source Sans Pro [preview](https://localfonts.eu/freefonts/traditional-cyrillic-free-fonts/source-sans-pro/).

Browsers, Pandoc and LibreOffice support language variants inside single font (that also support math formulas):

* Browsers support language variants via `lang="bg-BG"` (`"zh-CN"`, `"zh-TW"`, `"zh-HK"`, `"ja-JP"`, `"ko-KR"`) HTML property.
* Pandoc supports language variants for inline text via `[inline text]{lang="ru-RU"}` (span). And for paragraphs (div):
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
* Paid Microsoft Word since some version supports language variants (MS Word 2007 version does **not** support it). Free [Microsoft 365](https://www.office.com) online support it too but doesn't support math formulas editing.
* LibreOffice since some version supports language variants (v.7.0.1 does support it). For CJK first enable `Tools / Options / Language Settings / Languages / Default languages for documents / Asian`. See [CJK document example](./cjk-test). But the built-in math renderer is very bad (not the math editor that is somewhat OK). Hence you have options:
  * Use `.otd` format only and try TexMaths extension for LaTeX support. And optionally install WYSIWYM editor LyX and copypaste back and forth TeX formulas for easy WYSIWYM editing. But mind that TexMaths is buggy (I wasn't able to get it working on Windows 7 at all). See LyX quick templates [in this dir](./math_formulas) (`*.lyx` files) to speed up copypasting a bit.
  * Use `.docx` format only and write math in LibreOffice built-in math editor. It's not great but OK. Math would be saved in Microsoft Word compatible format. But to preview the document as it **should** be rendered you would need use some version of Microsoft Word. If you purchaised modern MS Word it's better to use it instead of LibreOffice. But in addition to paid options you can use:
    1. [Microsoft 365](https://www.office.com) online. But you would need to upload files to view and edit them (no math editing though). [OneDrive](https://onedrive.live.com/) sync application would make it more convenient. Edit mode would even use fonts from you computer. Math would be rendered in different font that in desktop and mobile apps though. But both preview mode and to PDF conversion would not be able to use your local fonts and **would not** be able to use font language variants. You can still embed fonts to the document but the server will only use regular style. To overcome this severe limit you may use special fonts like [Embed Serif](./Fonts/EmbedSerif) that is 6 different font families collection made from Source Serif Pro where each font is a renamed single style. If you need language variant you would have to create a special font for it. Not very conveniet workflow.
    2. [111]
