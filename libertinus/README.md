* [ ] [Fix Greek](https://github.com/khaledhosny/libertinus/issues/132).

Lowercase Greek italic (regular, semibold, bold) in Libertinus Serif only slanted instead of real italic: compare italic μ with italic u for example and see that italic μ simply automatically slanted regular μ (actually all greek lowercase italic poorly designed). Because of that it looks worse than Computer Modern or [GFS Porson](https://fontlibrary.org/en/font/gfs-porson). I wish this font to be better that CM so this should be fixed someday.

As a solution:

Adapt GFS Porson (OFL) and MathJax Computer Modern (Apache License v.2) - use Porson's "curls". CM Greek lowercase letters look ideal for math (also worth taking regular and italic Υ and Ω from CM). But I think it's better to stick closer to GFS Porson design to have a distinct look from CM (but it's a harder way).

I also suggest to fix: 
* regular μ, ν, γ - adapt from [Noto Serif](https://fonts.google.com/specimen/Noto+Serif)/Droid Serif (Apache License v.2),
* regular semibold μ - adapt from Noto Serif,
* regular bold μ, ν - adapt from Noto Serif,
* regular ψ (make a blend of Noto Serif - right part and Libertinus Serif - left part). So it looks more like [GFS Elpis](https://fontlibrary.org/en/font/gfs-elpis) (proprietary license).

* [ ] [Fix Cyrillic](https://github.com/khaledhosny/libertinus/issues/74). Cyrillic doesn't have bold italic. Cyrillic semibold italic is only slanted instead of real italic. PT Astra Serif (OFL) and Noto Serif/Droid Serif (Apache License v.2) bold italic can be adapted to Libertinus Serif:

* Bold italic ж and л should be adapted from Noto Serif:
    * fix л like Libertinus bold r,
    * fix ж like Libertinus bold n, r, c,
* Bold italic к should be adapted from Libertinus greek bold italic κ, and normal italic к,
* Bold italic и, у, е, х, a, n, p, o, с, т should be taken from Latin (u, y, e, x, a, n, p, o, c, m),
* Other bold italic should be adapted from PT Astra Serif:
    * fix й, ц, ш, щ like Libertinus bold u,
    * fix н, ю like Libertinus bold n,
    * fix з, э like Libertinus normal italic з, э,
    * ъ should be adjusted or shortened may be,
    * fix ф like Libertinus bold j,
    * fix ы like Libertinus bold u, i,
    * fix я, ч, ь like Libertinus bold i,
    * fix м like Libertinus bold r, u,
* Take normal italic д from PT Astra Serif,
* Fix normal italic ж like c so it's more like bold italic from Noto Serif,
* From PT Astra Serif adapt normal italic я, м like Libertinus я, м.


### See [pseudo-spec](libertinus_serif_spec.docx)
