
#Local Dependencies
import config

#Package Dependencies
import shutil

def archive_logs():
    #shutil.make_archive(config.web_dir_logfile, 'zip', config.zeek_log_dir)
    shutil.make_archive(config.web_path, 'zip', config.zeek_log_dir)
