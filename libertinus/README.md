* [ ] [Fix Greek](https://github.com/khaledhosny/libertinus/issues/132).

Lowercase Greek italic (regular, semibold, bold) in Libertinus Serif only slanted instead of real italic: compare italic μ with italic u for example and see that italic μ simply automatically slanted regular μ (actually all greek lowercase italic poorly designed). Because of that it looks worse than Computer Modern or [GFS Porson](https://fontlibrary.org/en/font/gfs-porson). I wish this font to be better that CM so this should be fixed someday.

As a solution:

Adapt GFS Porson (OFL) and MathJax Computer Modern (Apache License v.2) - use Porson's "curls". CM Greek lowercase letters look ideal for math (also worth taking regular and italic Υ and Ω from CM). But I think it's better to stick closer to GFS Porson design to have a distinct look from CM (but it's a harder way).

I also suggest to fix: 
* regular μ, ν, γ - adapt from [Noto Serif](https://fonts.google.com/specimen/Noto+Serif)/Droid Serif (Apache License v.2),
* regular semibold μ - adapt from Noto Serif,
* regular bold μ, ν - adapt from Noto Serif,
* regular ψ (make a blend of Noto Serif - right part and Libertinus Serif - left part). So it looks more like [GFS Elpis](https://fontlibrary.org/en/font/gfs-elpis) (proprietary license).

* [ ] [Fix Cyrillic](https://github.com/khaledhosny/libertinus/issues/74). Cyrillic doesn't have bold italic. Cyrillic semibold italic is only slanted instead of real italic. PT Astra Serif (OFL) and Noto Serif/Droid Serif (Apache License v.2) can be adapted to Libertinus Serif.


### See [pseudo-spec](libertinus_serif_spec.docx)
