# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 14:25:15 2023

@author: ilknu
"""
from scapy.all import *

capture=sniff()
capture.show()