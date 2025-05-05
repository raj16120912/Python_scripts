#!/usr/bin/env python

from urllib.request import urlretrieve
import sys
import tarfile
import paramiko

url = ( "https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.91/bin/apache-tomcat-9.0.91.tar.gz" )
filename = "apache-tomcat-9.0.91.tar.gz"

def download_file(url, filename):
    try:
        urlretrieve(url, filename)
        tar = tarfile.open(filename, "r:gz")
        tar.extractall()
        tar.close()
    except:
        print('Download failed')
        sys.exit(1)

download_file(url, filename)
