from parameters import *
import csv
from datetime import datetime as dt
from datetime import timezone as tz
import pandas as pd


def log_to_suitelogfile(level, message, time=''):
    ## apply generic settings
    levels={'info':'[INFO]   ', 'debug':'[DEBUG]  ', 'warning':'[WARNING]', 'error':'[ERROR]  '}
    level=levels[level] if level in levels.keys() else '[UNKNOWN]'
    now = time if not time=='' else dt.now(tz.utc)
    ## write to file
    hdr=suitelogfileheader
    file=open(suitelogfilename, 'a')
    writer=csv.DictWriter(file, fieldnames=hdr)
    writer.writerow({hdr[0]:level, hdr[1]:now, hdr[2]:message})
    file.close()

def load_xls(filename=''):
    filename=askopenfilename(filetypes=[("Excel Worksheets","*.xls")], initialdir='.') if filename='' else filename
    df = pd.read_excel(filename, skiprows=[0,1])
    dt = df.to_dict()
    dl = [dict(zip(dt,t)) for t in zip(*dt.values())]
    return dl