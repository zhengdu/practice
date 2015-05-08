#!/Users/zheng/anaconda/bin/python

#!/apollo/env/MLEnvImprovement/bin/python
"""
  Create html page for WW fortress volume monitor 

"""

import numpy as np
import pyh
import pandas as pd
import matplotlib
matplotlib.use('Agg') # Force matplotlib to not use any Xwindows backend.
import matplotlib.pyplot as plt
from datetime import datetime
import pytz
from jinja2 import Environment, FileSystemLoader

def parseDayFormat(x):
    """
        Parser day format
    """
    return datetime.strptime(x, '%d%b%Y').strftime('%Y-%m-%d')


def get_summary_stats(org):    
    """
        read data into panda DataFrame
        generate pivotal table
    """ 
    
    colNames = ['objectId','date','by','orgId','day','hour']
    dataFile = '/local_1/server-root/digitalQRate/fortress_ww/ncfap' + org + '.txt'
    
    data = pd.read_table(dataFile,names = colNames, 
                         skiprows = [0], parse_dates = [4],date_parser= parseDayFormat)    
    pTable = data.pivot_table('objectId', rows='hour', cols='day', aggfunc='count').sort_index(axis=1,ascending=False)
    colNum = len(pTable.columns)
    
    pTable = pTable.ix[:,0:8] # remove last day which has missing data
    sumTable = pTable.sum().to_frame().transpose()
    sumTable.rename(index={0:'Sum'},inplace=True)
    sumTable.index.name = 'hour'
    pTable = pTable.append(sumTable).fillna(0)
    
    fig = plt.figure(figsize=(12,5))
    # Add a subplot
    ax = fig.add_subplot(111)
    pTable.ix['Sum'].plot(style='bx-')
    ax.set_xticks(np.arange(len(pTable.columns)))
    ax.set_xticklabels(list(pTable.columns))
    ax.set_ylabel('Count')
    figFile = 'plot'+ org + '.png'
    fig.savefig(figFile)
    plt.clf()
    
    summaryOut = {'html':pTable.to_html(),'img':figFile} 
    
    return summaryOut

def renderHTML(info):
    env = Environment(loader=FileSystemLoader('/local_1/server-root/digitalQRate/html/html_temp'))
    template = env.get_template("monitorWWQueue.html")
    template_vars = {"title": "WW FORTRESS Queue Monitor",
                     "results": info,                     
                     "update_time": datetime.now(pytz.timezone('US/Pacific')).strftime('%m/%d/%y %H:%M')}
    html_out = template.render(template_vars)
    
    fname = '/local_1/server-root/digitalQRate/html/tt2.html'
    with open(fname, 'w') as f:        
        f.write(html_out)

if __name__== "__main__":
     
    orgs = ['us','gb','de','fr','jp','au','ca','mx','br','it','es','cn']
    results = []
    for org in orgs:
        try:
            pivotTable = get_summary_stats(org)
            results.append([org.upper(),pivotTable])
        except: 
            print " NO data in " + org 
            
    renderHTML(results)        
        
