import os
import shutil
import fontforge


def rename_font(input, save_as, fontname=None, familyname=None, fullname=None, clean_up=False):
    """
    Parameters
    ----------
    input: str
        Path to font to rename.
    fontname, familyname, fullname: str, str, str
        Font name parameters.
    save_as: str
        Save file path.
    """

    shutil.copy(input, save_as)
    renamed = fontforge.open(save_as)
    renamed.sfnt_names = []
    if fontname is not None:
        renamed.fontname = fontname
    if familyname is not None:
        renamed.familyname = familyname
    if fullname is not None:
        renamed.fullname = fullname

    if save_as[-4:] == '.sfd':
        renamed.save(save_as)
    else:
        renamed.generate(save_as)
    
    if clean_up:
        try:
            os.remove(input)
        except:
            pass
