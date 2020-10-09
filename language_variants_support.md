# Language variants support

See example of Cyrillic variants in Source Sans Pro [preview](https://localfonts.eu/freefonts/traditional-cyrillic-free-fonts/source-sans-pro/).

Browsers, Pandoc and LibreOffice support language variants inside single font:

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
* LibreOffice v.7.0.1 supports language variants. For CJK first enable `Tools / Options / Language Settings / Languages / Default languages for documents / Asian`. See [CJK document example](./cjk-test). But the built-in math renderer is very bad (not the math editor that is somewhat OK). Hence you have options:
  * Try TexMaths extension together with installing WYSIWYM editor LyX and copypasting back and forth TeX formulas for easy WYSIWYM editing. But mind that it's buggy. I wasn't able to get TexMaths working on Windows 7 at all. See LyX quick templates [in this dir](./math_formulas) to speed up copypasting a bit.
