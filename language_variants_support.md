# Language variants support

Browsers, Pandoc and LibreOffice support language variants inside single font:

* Browsers support language variants via `lang="bg-BG"` (`"zh-CN"`, `"zh-TW"`, `"zh-HK"`, `"ja-JP"`, `"ko-KR"`) HTML property.
* LibreOffice v.7.0.1 supports language variants. For CJK first enable `Tools / Options / Language Settings / Languages / Default languages for documents / Asian`. See document example [here](./cjk-test). Built-in math editor in LibreOffice is rather dissapointing so you can try TexMaths extension together with installing WYSIWYM editor LyX and copypasting back and forth TeX formulas for easy editing (Mind that it's buggy. I wasn't able to get TexMaths working on Windows 7 at all). LyX [quick templates](./lyx).
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
* See example of Cyrillic variants in Source Sans Pro [preview](https://localfonts.eu/freefonts/traditional-cyrillic-free-fonts/source-sans-pro/).
