# -*- coding: utf-8 -*-
import os
import re
from os.path import join

from funcs import preview
# from ff_wrapper import ff
from ff_funcs import ff


print(ff('version', 'Hello!'))

repos = os.path.normpath(join(os.getcwd(), '../../'))
libertinus = join(repos, 'libertinus')
libertinus_serif = join(repos, 'libertinus_serif')
open_fonts = join(repos, 'open-fonts', 'Fonts')

if not os.path.exists(libertinus_serif):
    os.makedirs(libertinus_serif)

temp = '__temp__'
if not os.path.exists(temp):
    os.makedirs(temp)


# Set characters to take from Libertinus Serif, PT Astra Serif, Noto Serif and Tinos
# ----------------------------------------------------------------------------------
# Cyrillic: 256 - 7 + 4 = 253
# U+.... 0    1    2    3    4    5    6    7    8    9    A    B    C    D    E    F
cyrillic = u"""
040.     Ѐ    Ё    Ђ    Ѓ    Є    Ѕ    І    Ї    Ј    Љ    Њ    Ћ    Ќ    Ѝ    Ў    Џ
041.     А    Б    В    Г    Д    Е    Ж    З    И    Й    К    Л    М    Н    О    П
042.     Р    С    Т    У    Ф    Х    Ц    Ч    Ш    Щ    Ъ    Ы    Ь    Э    Ю    Я
043.     а    б    в    г    д    е    ж    з    и    й    к    л    м    н    о    п
044.     р    с    т    у    ф    х    ц    ч    ш    щ    ъ    ы    ь    э    ю    я
045.     ѐ    ё    ђ    ѓ    є    ѕ    і    ї    ј    љ    њ    ћ    ќ    ѝ    ў    џ
046.     Ѡ    ѡ    Ѣ    ѣ    Ѥ    ѥ    Ѧ    ѧ    Ѩ    ѩ    Ѫ    ѫ    Ѭ    ѭ    Ѯ    ѯ
047.     Ѱ    ѱ    Ѳ    ѳ    Ѵ    ѵ    Ѷ    ѷ    Ѹ    ѹ    Ѻ    ѻ    Ѽ    ѽ    Ѿ    ѿ
048.     Ҁ    ҁ         ҃                                  Ҋ    ҋ    Ҍ    ҍ    Ҏ    ҏ
049.     Ґ    ґ    Ғ    ғ    Ҕ    ҕ    Җ    җ    Ҙ    ҙ    Қ    қ    Ҝ    ҝ    Ҟ    ҟ
04A.     Ҡ    ҡ    Ң    ң    Ҥ    ҥ    Ҧ    ҧ    Ҩ    ҩ    Ҫ    ҫ    Ҭ    ҭ    Ү    ү
04B.     Ұ    ұ    Ҳ    ҳ    Ҵ    ҵ    Ҷ    ҷ    Ҹ    ҹ    Һ    һ    Ҽ    ҽ    Ҿ    ҿ
04C.     Ӏ    Ӂ    ӂ    Ӄ    ӄ    Ӆ    ӆ    Ӈ    ӈ    Ӊ    ӊ    Ӌ    ӌ    Ӎ    ӎ    ӏ
04D.     Ӑ    ӑ    Ӓ    ӓ    Ӕ    ӕ    Ӗ    ӗ    Ә    ә    Ӛ    ӛ    Ӝ    ӝ    Ӟ    ӟ
04E.     Ӡ    ӡ    Ӣ    ӣ    Ӥ    ӥ    Ӧ    ӧ    Ө    ө    Ӫ    ӫ    Ӭ    ӭ    Ӯ    ӯ
04F.     Ӱ    ӱ    Ӳ    ӳ    Ӵ    ӵ    Ӷ    ӷ    Ӹ    ӹ    Ӻ    ӻ    Ӽ    ӽ    Ӿ    ӿ
A64[CD]       Ꙍ    ꙍ
A65[67]       Ꙗ    ꙗ
"""
# Greek and other: 57
other = u"""
03[89A].      Ύ    Ώ    ΐ    Θ    Υ    Ω    Ϋ    ά    έ    ή    ί
03B.     ΰ    α    β    γ    δ    ε    ζ    η    θ    ι    κ    λ    μ    ν    ξ    ο
03C.     π    ρ    ς    σ    τ    υ    φ    χ    ψ    ω    ϊ    ϋ    ό    ύ    ώ
03[DEF].      ϐ    ϑ    Υ    ϓ    ϔ    ϕ    ϖ    ϗ    Ϛ    ϛ    ϰ    ϱ    ϵ    ϶
2202          ∂
"""

cyrillic = re.sub(r'[ x0123456789ABCDEF\r\n\+\.\!\?\[\]\|\(\)]', '', cyrillic)
other = re.sub(r'[ x0123456789ABCDEF\r\n\+\.\!\?\[\]\|\(\)]', '', other)
print(len(cyrillic), len(other))

# TODO: Merge fonts in fallback order: Libertinus Serif, PT Astra Serif. Then Tinos or Noto Serif (торчащие вниз лучше в Noto видны) on custom basis.
# TODO: Check stilistic coherence in clusters.
# TODO: Search for similar letters in other unicode blocks (accented - must have).
# TODO: Fix non-cyrillic.


# Test letters
# ------------
clusters = [
    (u"Ee-Ее",  u"ѐёеӗәӛҽҿӕЀЁЕӖӘӚҼҾӔ"),
    (u"Thm-Тт-REG",  u"ђћтҭЂЋТҬ"),
    (u"Γ-Гг",  u"гѓґғҕӷӻГЃҐҒҔӶӺ"),
    (u"I-ЭэЮю",  u"эєѥюӭЭЄѤЮӬ"),
    (u"IiJjSsCcPp",  u"іїІЇӀӏјЈѕЅсҫСҪрҏРҎ"),
    (u"AaXxIO-АаХхЮю",  u"аӓӑꙗАӒӐꙖхҳӽӿХҲӼӾ"),
    (u"BMXx-ЛлЬьХх",  u"лљӆЛЉӅ"),
    (u"BH-НнЬьГг",  u"нњҥңӊӈНЊҤҢӉӇ"),
    (u"Kkκ-Кк",  u"кќқҝҟҡӄКЌҚҜҞҠӃ"),
    (u"H-Ии",  u"иѝӣӥйҋИЍӢӤЙҊ"),
    (u"YyΥγ¥-Уу",  u"үұҮҰуўӱӳӯУЎӰӲӮ"),
    (u"ΠT-ПпТт",  u"пџцшщҧҵПЏЦШЩҦҴ"),
    (u"3-Зз",  u"зҙӟЗҘӞ"),
    (u"Жж",  u"жӝҗӂЖӜҖӁ"),
    (u"BΓITd-ВвТт",  u"бвъыӹьҍѣБВЪЫӸЬҌѢ"),
    (u"Oo-Оо",  u"оӧѳөӫѻѹОӦѲӨӪѺѸ"),
    (u"other",  u"ҩҨӡӠѯѮҀҁ҂ѧѩѭѫѦѨѬѪ"),
    (u"RfΦ-ФфЯяДдМм",  u"фФяЯдДмӎМӍ"),
    (u"Чч",  u"чҷӵҹӌһЧҶӴҸӋҺ"),
    (u"Ψψ",  u"ѱѰ"),
    (u"WwVvν",  u"ѵѷѴѶѡѿѽꙍѠѾѼꙌ ҃ "),
    (u"non-cyr",  u"∂"),

    (u"bar-ħ",  u"ђћғҟұҍӻӿҒҞҰҌӺӾҝҹҜҸ"),
    (u"tail1",  u"ђҕӈӄҧӽӻЂҔӇӃҦӼӺ"),
    (u"horn",  u"ґҐъҡЪҠ"),
    (u"tail2+curl",  u"ҭӷңқцщҵҗҳҷҋӆӎҬӶҢҚЦЩҴҖҲҶҊӅӍӊӉӌӋџЏҿҫҙҾҪҘ"),
    (u"ijÄä",  u"іјӓёӛїӱӭӟӥӧӫӝӹӵӒЁӚЇӰӬӞӤӦӪӜӸӴ"),
    (u"cyr-breve",  u"ӗӑўӂйҋӖӐЎӁЙҊѽѼ/ѡ҃"),
    (u"ÁáŐőĀāÀàȁ",  u"ѓќЃЌӳӲӯӣӮӢѐЀѷѶ"),
    (u"∂-italic",  u"бд"),
]


preview(temp, [("", cyrillic), ("", other)] + clusters)
