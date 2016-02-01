Instructions of setting up ipython notebook on trms-analytics host:

08/2015
Jun Ma


1. Download and install Anaconda on the server.

To start:
2. On server, navigate into your work directory:
   $PATH_TO_ANACONDA/bin/ipython notebook --no-browser --port=8889
   
   /home/junmaa/anaconda/bin/ipython notebook --no-browser --port=8889
3. On local:
   ssh -N -f -L localhost:8888:localhost:8889 $YOUR_LOGIN@$HOST_NAME
   ssh -N -f -L localhost:8888:localhost:8889 zhengdu@bf-analytics-r-na-link-snapshot-6001.iad6.amazon.com
   
   ssh -N -f -L localhost:8888:localhost:8889 zhengdu@bf-analytics-r-na-25003.iad55.amazon.com
   
4. Open a browser:
   http://localhost:8888
Ready to go !


To shutdown:
5. On local:
   ps aux | grep localhost:8889
   kill $PID_OF_YOUR_SSH
6. On server,
   Ctril-C, and y

   
import sys
import numpy as np
import pandas as pd
from pandas import DataFrame, Series

%matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt

import json
import IPython
from IPython.display import Image, display

print "Python version: " + sys.version
print "Pandas version: " + pd.__version__
print "IPython version: " + IPython.__version__

pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)
