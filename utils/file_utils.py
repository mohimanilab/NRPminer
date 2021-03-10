import os
import errno
import sys
from os.path import isdir, isfile, getsize


def error(msg):
    print(msg)
    sys.exit(1)


def verify_file(fpath, description=''):
    if not check_file(fpath):
        error(fpath + (' (' + description + ' file)' if description else '') + ' is empty or does not exist!')


def verify_dir(dirpath, description=''):
    if not isdir(dirpath):
        error(dirpath + (' (' + description + ' dir)' if description else '') + ' does not exist!')


def check_file(fpath):
    return isfile(fpath) and getsize(fpath) > 0


def remove_if_exists(fpath):
    # http://stackoverflow.com/questions/10840533/most-pythonic-way-to-delete-a-file-which-may-not-exist
    try:
        os.remove(fpath)
    except OSError as e:
        if e.errno != errno.ENOENT:  # errno.ENOENT = no such file or directory
            raise  # re-raise exception if a different error occured


def count_lines(fpath):
    with open(fpath) as f:
        return len(f.readlines())


def removeDir(path):
    #https://stackoverflow.com/questions/303200/how-do-i-remove-delete-a-folder-that-is-not-empty-with-python
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
