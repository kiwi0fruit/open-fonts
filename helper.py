import os
import shutil
import fontforge


def rename_font(input, save_as, fontname=None, familyname=None, fullname=None, sfnt_ref=None, reps=(), clean_up=False, mono=False):
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
    """
    def _rep(obj):
        if isinstance(obj, str):
            for pair in reps:
                obj = obj.replace(pair[0], pair[1])
            return obj
        elif isinstance(obj, tuple):
            return tuple(_rep(o) for o in obj)
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
