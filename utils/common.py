import xml.etree.ElementTree
from distutils import dir_util
from os.path import join, isfile, isdir, basename


def parse_params_xml(fpath):
    with open(fpath) as f:
        content = f.read()
    params = dict()
    file_mapping = dict()
    for e in xml.etree.ElementTree.fromstring(content).findall('parameter'):
        if e.attrib['name'] == 'upload_file_mapping':
            fname, real_fname = e.text.split('|')[0:2]
            file_mapping[basename(fname)] = real_fname
            continue
        if e.text == 'on':
            value = True
        elif e.text == 'off':
            value = False
        else:
            value = e.text
        params[e.attrib['name']] = value
    return params, file_mapping


def uniqify(seq, idfun=None): 
   # order preserving
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   for item in seq:
       marker = idfun(item)
       # in old Python versions:
       # if seen.has_key(marker)
       # but in new ones:
       if marker in seen: continue
       seen[marker] = 1
       result.append(item)
   return result


def removeDir(path):
    import os
    import stat
    import shutil
    def errorRemoveReadonly(func, path, exc):
        excvalue = exc[1]
        if func in (os.rmdir, os.remove) and excvalue.errno == errno.EACCES:
            # change the file to be readable,writable,executable: 0777
            os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)  
            # retry
            func(path)
        # else:
        #     # raiseenter code here
    shutil.rmtree(path, ignore_errors=False, onerror=errorRemoveReadonly) 



def mkdir_p(path):
    import errno
    import os
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise




def is_valid_file(parser, arg):
    """
    Check if arg is a valid file that already exists on the file system.
    Parameters
    """
    arg = os.path.abspath(arg)
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg

def uniqify(seq, idfun=None): 
   # order preserving
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   for item in seq:
       marker = idfun(item)
       # in old Python versions:
       # if seen.has_key(marker)
       # but in new ones:
       if marker in seen: continue
       seen[marker] = 1
       result.append(item)
   return result
    

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

class CleanChildProcesses:
  def __enter__(self):
    os.setpgrp() # create new process group, become its leader
  def __exit__(self, type, value, traceback):
    try:
      os.killpg(0, signal.SIGINT) # kill all processes in my group
    except:
    #   # SIGINT is delievered to this process as well as the child processes.
    #   # Ignore it so that the existing exception, if any, is returned. This
    #   # leaves us with a clean exit code if there was no exception.
      pass
total = 0

def readable_dir(prospective_dir):
    print prospective_dir
    if not os.path.isdir(prospective_dir):
        raise Exception("readable_dir:{0} is not a valid path".format(prospective_dir))
    if os.access(prospective_dir, os.R_OK):
        return prospective_dir
    else:
        raise Exception("readable_dir:{0} is not a readable dir".format(prospective_dir))

        
