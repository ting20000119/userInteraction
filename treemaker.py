#!/usr/bin/python
import psycopg2
import datetime
from tqdm import tqdm
from config import config
import json
conn = None
def connect():
    """ Connect to the PostgreSQL database server """
    params = config()
#    print(config(section="subreddit"))
    print('Connecting to the PostgreSQL database...')
    global conn
    conn = psycopg2.connect(**params)

def disconnect():
    global conn
    conn.close()
    print('Database connection closed.')

def execute_SQL(insert_stmt):
    
    cur = conn.cursor()
    cur.execute(insert_stmt)
    try:
        result = cur.fetchall()
    except:
        result = None
    cur.close()
    return result





def subtree(sub_id):
    connect()
    subtreeroot = {}
    sub_id = 't3_'+sub_id 
    comment_id_list = execute_SQL("select id from politicscom2020 where parent_id = '{sub}'".format(sub=sub_id))
    comment_id_list = [x for (x,) in comment_id_list]

    for comment_id in comment_id_list:
        subtreeroot[comment_id] = comchild(comment_id)
    return subtreeroot



def comchild(com_id):
    comtreeroot = {}
    com_id = 't1_'+com_id 
    comment_id_list = execute_SQL("select id from politicscom2020 where parent_id = '{com}'".format(com=com_id))
    comment_id_list = [x for (x,) in comment_id_list]

    for comment_id in comment_id_list:
        comtreeroot[comment_id] = comchild(comment_id)
    return comtreeroot

def main():
    connect()
    print(json.dumps(subtree('j3ygfd'), indent=4, sort_keys=True))


if __name__ == '__main__':
    main()
