import time, datetime, os, shutil
from backup_dirs_pkg.app import backup as backup_dirs
from backup_dirs_pkg.app import config_file
from backup_dirs_pkg.config import constants

def createDir(path):
    if not os.path.isdir(path):
        os.mkdir(path)
        return True
    else:
        print 'The directory already exists\t' + path
        return False

if config_file.config_load() and config_file.config_validate():
    backup_to_basedir = config_file.config_get_basedir()
    backup_configfile = config_file.config_get_filepath()
    ts = time.time()
    backup_to_dir = os.path.join(
        backup_to_basedir,
        datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
    )
    if createDir(backup_to_dir):
        shutil.copy(
            backup_configfile,
            backup_to_dir
        )
        backup_dirs.backupLocal(backup_to_dir)
        backup_dirs.backupRemote(backup_to_dir)
    else:
        print 'The backup destination directory already exists:\n' + backup_to_dir
else:
    print 'Try again'