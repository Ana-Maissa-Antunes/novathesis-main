#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 16:06:46 2022

@author: mac
"""
from http.server import CGIHTTPRequestHandler, HTTPServer

def main():
	httpd = HTTPServer(('',61025),CGIHTTPRequestHandler)
	print( "Starting webserver ...")
	httpd.serve_forever()
	print("Error in server!")    


if __name__ == "__main__":
	main()
