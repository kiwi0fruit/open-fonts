import os
import os.path as p
import shutil
import fontforge
import subprocess
import os
import sys
here = p.dirname(p.abspath(__file__))
sys.path.insert(0, p.join(p.dirname(here), 'shutilwhich-cwdpatch'))
from shutilwhich_cwdpatch import which


def rename_font(input, save_as, fontname=None, familyname=None, fullname=None,
                sfnt_ref=None, reps=(), clean_up=False, mono=False, remove=()):
    """
    Parameters
    ----------
    input : str
        Path to font to rename.
    fontname, familyname, fullname : str, str, str
        Font name parameters.
    save_as : str
        Save file path.
    sfnt_ref : str
        path to reference font with right SFNT section
    reps : tuple(tuple)
        replacements for SFNT section like: (('Roboto', 'Open'), ('STIX', 'STYX'))
    mono : bool
        set isFixedPitch flag to 1 and OS/2 PANOSE Proportion to Monospaced
    remove : iterable
        list of characters to delete form a font
    """
    def _rep(obj):
        if isinstance(obj, str):
            for pair in reps:
                obj = obj.replace(pair[0], pair[1])
            return obj
        elif isinstance(obj, tuple):
            t = tuple(_rep(o) for o in obj)
            if t[1] == 'PostScriptName':
                t = tuple([t[0], t[1], t[2].replace(' ', '')] + list(t[3:]))
            return t
        else:
            raise RuntimeError('Tried to replace something that is not tuple/str superposition.')

    shutil.copy(input, save_as)
    if sfnt_ref is not None:
        ref_font = fontforge.open(sfnt_ref)
        sfnt_names = _rep(ref_font.sfnt_names)
        ref_font.close()
    else:
        sfnt_names = ()

    renamed = fontforge.open(save_as)
    renamed.sfnt_names = sfnt_names

    if fontname is not None:
        renamed.fontname = fontname
    if familyname is not None:
        renamed.familyname = familyname
    if fullname is not None:
        renamed.fullname = fullname
    if mono:
        lst = list(renamed.os2_panose)
        lst[3] = 9
        renamed.os2_panose = tuple(lst)

    if remove:
        for c in remove:
            renamed.selection[ord(c)] = True
        for i in renamed.selection.byGlyphs:
            renamed.removeGlyph(i)

    if save_as[-4:] == '.sfd':
        renamed.save(save_as)
    else:
        renamed.generate(save_as)
    
    if clean_up:
        try:
            os.remove(input)
        except:
            pass
    renamed.close()

    if mono:
        if os.name != 'nt':
            pyexe = which('python3')
            if not pyexe:
                pyexe = which('python')
        else:
            pyexe = which('python')
        if not pyexe:
            raise RuntimeError("python executable wasn't found")
        print(subprocess.check_output([pyexe, p.join(here, 'setisFixedPitch-fonttools.py'), save_as]))
