import os

MTA_KEY       = os.environ.get('MTA_KEY')
STATIONS_FILE = os.environ.get('STATIONS_FILE', './data/stations.json')
CROSS_ORIGIN  = os.environ.get('CROSS_ORIGIN', '*')
MAX_TRAINS    = os.environ.get('MAX_TRAINS', '10')
MAX_MINUTES   = os.environ.get('MAX_MINUTES', '30')
CACHE_SECONDS = os.environ.get('CACHE_SECONDS', '60')
THREADED      = os.environ.get('THREADED', True)
DEBUG         = os.environ.get('DEBUG', False)
