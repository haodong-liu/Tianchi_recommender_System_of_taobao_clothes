#-*-coding:utf8-*-
import math
import time
import frequency_cat

def user_time(item, ubh_line):
    dict_item_couple = {}
    dictMerged ={}
    for each in ubh_line:
        ubh_lineone = each.split(' ')
        if(ubh_lineone[1] == item):
            user_id = ubh_lineone[0]
            bought_day = ubh_lineone[2]
            dict1 = user_bought(user_id, bought_day, item)
            dictMerged = dict(dictMerged.items()+dict1.items())
    dict_item_couple[item] = dictMerged
    print dict_item_couple
    return dict_item_couple
#return  dict

def user_bought(user_id, bought_day,item1_id):
    num_dict = {}
    for each in ubh_line:
        ubh_lineone = each.split(' ')
        if((ubh_lineone[0] == user_id)and(bought_day == ubh_lineone[2])and(ubh_lineone[1]!=item1_id)):
            match_item = ubh_lineone[1]
            user_bought_1_day_list.append(match_item)
            if(num_dict.has_key(match_item) and (match_item != item1_id)):
                num_dict[match_item] = num_dict[match_item]+1
            else:
                num_dict[match_item] = 1
    return num_dict



def fpm(item1,item2,dict_item1):

    item2_num = dict_item1[item1]
    if item2_num.has_key(item2):
        return item2_num[item2]
    else:
        return 0

def S1(fpm_, fcm_):
    return fpm_*math.log((1+fcm_), math.e)


def match_dict_S1(item,user_bought_1_day_list,dict_item):
    a = frequency_cat.collocation()
    dict_utlimate = {}
    dict_item_s1 = {}
    for each in user_bought_1_day_list:
        num_item = fpm(item, each, dict_item)
        num_cat = a.cat_mat_frequency(item, each)
        n = S1(num_item, num_cat)
        dict_item_s1[each] = n
    dict_utlimate[item] = dict_item_s1
    print dict_utlimate
    return dict_utlimate

def final(dict,item1_id):
    dict1 = dict[item1_id]
    print '---------------------------------------'
    print '|final result:                        |\n|                                     |'
    dict2 = sorted(dict1.items(), key=lambda item: item[1])
    for each in dict2:
        if(each[1]!=0.0):
            print '|'+each[0]+'                              |'
    print '---------------------------------------'

if __name__ == '__main__':
    time1 = time.time()
    num_dict = {}
    user_bought_1_day_list = []
    a = frequency_cat.collocation()
    user_bought_history = open('user_bought_history.txt', 'r')

    fashion_matchsets = open('dim_fashion_matchsets.txt', 'r')

    dim_item = open('dim_items.txt', 'r')

    ubh_line = user_bought_history.readlines()

    fashion_match = fashion_matchsets.readlines()

    dim_all_item = dim_item.readlines()

    item_list = []
    item1_id = str(438823)
    dict_user_time = user_time(item1_id,ubh_line)
    final(match_dict_S1(item1_id, user_bought_1_day_list, dict_user_time),item1_id)
    time2 = time.time()
    print 'spend time:'+str(time2 - time1)