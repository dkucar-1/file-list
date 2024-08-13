#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from queue import deque

# helper function to strip out http, https and garbage links
def filter_http(href):
    import re
    return href and not re.compile("http|\\?C=.*;O=.*|css").search(href)

def recursive_list(url):
        
        if not url: return 

        indent  = (" "*0)
        directories = deque([url])
       
        while directories:
            cur_dir = directories.pop()
            webpage = requests.get(cur_dir).content
            soup = BeautifulSoup(webpage, features="html.parser")
            files = [anchor.get('href') for anchor in soup.find_all(href=filter_http) 
                     if anchor.get('href') != "/"
                     and not anchor.get('href').startswith("/")]
            
            
            # keep track of directories with only sub-directories.. don't display
            files_only = len([f for f in files if not f.endswith("/")]) != 0

            # display current directory name, save indentation for files under
            if cur_dir != url and files_only: 
                print_dir = cur_dir.split(url)[-1]
                print(f"{print_dir}")
                #num_indents = len(print_dir.split("/")) - 1
                indent = (" "*2)

            for f in files:  
                if (f.endswith('/')):
                    directories.appendleft(cur_dir+f)
                else:  
                    print (f"{indent}{f}")
        return


# call the initial directories web folder
if __name__ =="__main__": 
    import sys

    url = sys.argv[1] if len(sys.argv) > 1 else  'https://apache.osuosl.org/airflow/'
    #url = 'https://gentoo.osuosl.org/distfiles/'
    recursive_list(url)

