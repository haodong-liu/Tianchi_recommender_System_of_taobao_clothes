class matchhistory():
    match_list =[]

    def separate(self,list1):
        new_list = []
        for each in list1:
            if ',' not in each:
                new_list.append(each)
            else:
                itemids = each.split(',')

                for id in itemids:
                    new_list.append(id)

        return new_list

    def match_item(self, simi_list):

        fashion_matchsets = open('dim_fashion_matchsets.txt', 'r')
        fashion_match = fashion_matchsets.readlines()
        for each in fashion_match:
            fashion_match_line = each.rstrip('\n').split(' ')
            items_list = fashion_match_line[1].split(';')

            for similirity in simi_list:
                for item_id in items_list:
                    if ',' in item_id:
                        ids = item_id.split(',')
                        # print ids
                        if similirity in ids:
                            items_list.remove(item_id)
                            for match in self.separate(items_list):
                                if match not in self.match_list:
                                    self.match_list.append(match)

                    else:
                        if similirity == item_id:
                            items_list.remove(item_id)
                            for match in self.separate(items_list):
                                if match not in self.match_list:
                                    self.match_list.append(match)
        print 'final matching result:\n'
        for each in self.match_list:
            print each

if __name__ == '__main__':
    a = matchhistory()
    line = ['1062118', '2787884', '3109993']
    '''similar gather with item waiting testing'''
    a.match_item(line)



