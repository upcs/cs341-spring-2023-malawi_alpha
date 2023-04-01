#!/usr/bin/python3
import pymysql

def connect():
    conn = pymysql.connect(
        db='MalawiDB',
        user='root',
        passwd='cs341mwalpha',
        host='localhost')
        
    return conn.cursor()

