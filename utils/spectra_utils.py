import os
from os.path import join, isfile, splitext, getsize, dirname, basename, isdir


allowed_spectrum_extensions = ['mzML', 'mzXML', 'mzdata', 'mz5', 'mgf', 'ms1', 'ms2', 'cms1', 'cms2', 'raw']
not_converted_extensions = ['.mgf', '.mzXML', '.mzdata']
extension_after_conversion = '.mgf'


def get_spectra_fpaths(all_fpaths):
    spectra_fpaths = []
    for entry in all_fpaths:
        if isdir(entry):
            spectra_fpaths += [join(path, fpath) for (path, dirs, files) in os.walk(entry)
                               for fpath in files if is_spectrum_file(join(path, fpath))]
        elif is_spectrum_file(entry):
            spectra_fpaths.append(entry)
    spectra_fpaths.sort()
    return spectra_fpaths


def is_spectrum_file(fpath):
    allowed_extensions = map(lambda x: '.' + x.lower(), allowed_spectrum_extensions)

    if not isfile(fpath):
        return False
    basename, ext = splitext(fpath)
    if ext.lower() in allowed_extensions:
        return True
    return False


def spectra_need_convertion(fpath):
    basename, ext = splitext(fpath)
    if ext.lower() in map(lambda x: x.lower(), not_converted_extensions):
        return False
    return True