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
    comment_id_list = execute_SQL(
        "select id from politicscom2020 where parent_id = '{sub}'".format(sub='t3_'+sub_id))
    comment_id_list = [x for (x,) in comment_id_list]
    sub_leaning = execute_SQL("select leaning from politicsuserleaning,politicssub2020 where politicssub2020.id = '{sub}' and politicsuserleaning.author = politicssub2020.author".format(sub=sub_id))[0][0]
    #print(sub_leaning)

    for comment_id in comment_id_list:
        com_leaning = execute_SQL("select leaning from politicsuserleaning,politicscom2020 where politicscom2020.id = '{com}' and politicsuserleaning.author = politicscom2020.author".format(com=comment_id))[0][0]
        dict_obj = {}
        child_dict_obj = {}
        child_dict_obj["parentAuthor"] = sub_id
        child_dict_obj["parentLeaning"] = sub_leaning
        child_dict_obj["childLeaning"] = com_leaning
        dict_obj[comment_id] = child_dict_obj
        pair_list.append(dict_obj)
        subtreeroot[comment_id] = comchild(comment_id,com_leaning)
    return subtreeroot


def comchild(com_id,com_leaning):
    comtreeroot = {}
    comment_id_list = execute_SQL(
        "select id from politicscom2020 where parent_id = '{com}'".format(com='t1_'+com_id))
    comment_id_list = [x for (x,) in comment_id_list]
    
    for comment_id in comment_id_list:
        child_com_leaning = execute_SQL("select leaning from politicsuserleaning,politicscom2020 where politicscom2020.id = '{com}' and politicsuserleaning.author = politicscom2020.author".format(com=comment_id))[0][0]
        dict_obj = {}
        child_dict_obj = {}
        child_dict_obj["parentAuthor"] = com_id
        child_dict_obj["parentLeaning"] = com_leaning
        child_dict_obj["childLeaning"] = child_com_leaning
        dict_obj[comment_id] = child_dict_obj
        pair_list.append(dict_obj)
        comtreeroot[comment_id] = comchild(comment_id,child_com_leaning)

    return comtreeroot

pair_list = []
def main():
    connect()
    print(getpairlist('j3ygfd'))
    #print(json.dumps(subtree('j3ygfd'), indent=4, sort_keys=True))
    #print(pair_list)

def getpairlist(sub_id):
    global pair_list
    pair_list=[]
    json.dumps(subtree(sub_id), indent=4, sort_keys=True)
    print(pair_list)
    return pair_list

if __name__ == '__main__':
    main()
