import os
import io

main_template = u"""<!DOCTYPE html>
<html>
  <head>
      <meta charset="utf-8" />
      <title>auto_bold</title>
  </head>
  <body style="line-height: 1.5; font-size: 40px; padding-left: 10em;">
{}
  </body>
</html>
"""

template = u"""    <p style="font-family: '{0}', 'Noto Sans', Symbola; font-weight: {1}; font-style: {2};">
      {0}</br>{3}&nbsp;&nbsp;{4}
    </p>
"""


def preview(temp, clusters):
    text = main_template.format(
        ''.join([
            template.format(font, weight, style, etalon, string)
            for etalon, string in clusters
            for weight, style in [('normal', 'normal'), ('normal', 'italic'), ('500', 'normal'), ('500', 'italic'), ('bold', 'normal'), ('bold', 'italic'),]
            for font in ('Libertinus Serif', 'PT Astra Serif', 'Tinos', 'Noto Serif')
        ])
    )
    with io.open(os.path.join(temp, 'preview.html'), 'w', encoding='utf-8') as file:
        file.write(text)
