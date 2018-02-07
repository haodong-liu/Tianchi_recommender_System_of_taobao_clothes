import time

class collocation():


    def cat_id(self,item_id):#return item's cat_id
        i=0
        dim_items = open('dim_items.txt', 'r')
        dim_items_line = dim_items.readlines()

        for each in dim_items_line:
            items_list = each.rstrip('\n').split(' ')
            if(item_id == items_list[0]):
                return items_list[1]



    def item_cat(self):# build fashion_cat.txt
        i = 0
        fashion_cat = []
        fashion_cat_file = open('fashion_cat.txt', 'a')
        fashion_matchsets = open('dim_fashion_matchsets.txt', 'r')
        fashion_match = fashion_matchsets.readlines()
        for each in fashion_match:
            items_list_d = []
            new_cat = []

            fashion_match_line = each.rstrip('\n').split(' ')
            items_list = fashion_match_line[1].split(';')
            for items in items_list:
                if ',' in items:
                    items_list_d.append(items.split(',')[0])
                    items_list.remove(items)
                else:
                    items_list_d.append(items)
            # print items_list_d

            n = 0
            for new in items_list_d:
                new_cat.append(self.cat_id(new))

            for out in new_cat:
                fashion_cat_file.write(out+' ')
            fashion_cat_file.write('\n')



    def all_cat_mat_frequency(self ,item1):
        #return ferquency of item1's cat and it's matching cat by dict[item1]
        dict_cat_match_num ={}
        dict_item_match = {}
        fashion_cat = open('fashion_cat.txt', 'r')
        fashion_cat_info = fashion_cat.readlines()
        item1_cat = self.cat_id(item1)
        # print item1_cat
        # item2_cat = self.cat_id(item2)
        for line in fashion_cat_info:
            line_list = line.rstrip('\n').split(' ')
            if '' in line_list:
                line_list.remove('')
            # print line_list
            if item1_cat in line_list:
                for cat in line_list:
                    if cat !=item1_cat:
                        if dict_cat_match_num.has_key(cat):
                            dict_cat_match_num[cat] = dict_cat_match_num[cat]+1
                        else:
                            dict_cat_match_num[cat] = 1
        dict_item_match[item1_cat] = dict_cat_match_num
        return dict_item_match

    def cat_mat_frequency(self, item1, item2):
        dict = self.all_cat_mat_frequency(item1)
        item1_cat = self.cat_id(item1)
        item2_cat = self.cat_id(item2)
        dict_item1 = dict[item1_cat]
        # print dict_item1
        if dict_item1.has_key(item2_cat):
            return dict[item1_cat][item2_cat]
        else:
            return 0

    def num(self):
        #search the items
        i=1
        f = open('dim_items.txt', 'r')
        line = f.readlines()
        list = []
        for each in line:
            a = each.rstrip('\n').split(' ')
            if(a[0] == str(667320)):
                print a
                list.append(each)
                print i
            else:
                i=1+i

        print len(line)
        print i


if __name__ == '__main__':
    a = collocation()
    time1 = time.time()
    print a.cat_mat_frequency(str(257), str(667320))
    time2 = time.time()
    print time2-time1