'''
1. 购买1级五行石:消耗金和钻石
2. 1级五行石合成3级五行石:消耗金，体力和1级五行石
3. 3级五行石合成4级五行石:消耗金，体力和1级五行石，一定概率
4. 4级五行石合成6级五行石:消耗金，体力和4级五行石
'''


l1_value = 0.75 # 1级石头消耗0.75金
l1_value_diamond = 8 #1级石头同时还需要消耗8颗钻石
'''
    1级合成3级
'''
l1_to_13 = 12 #12颗1级石头才能合成一颗3级石头
l1_to_13_gold = 0.39 #同时还需要0.39
l1_to_13_vit = 10 #同时还需要10点体力
'''
    3级合成4级
'''
l3_to_14 = 16 #3级到4级需要消耗16个1级石头
l3_to_14_gold = 0.897 #同时需要0.897金
l3_to_14_vit = 10
l3_to_14_rate = 0.4878 #成功率只有0.4878 #如果失败，16颗1级石头也会被扣除，但不消耗体力
'''
    4级合成6级
'''
l4_to_16 = 12 #4级变6级石头，概率100%，需要消耗12颗4级石头
l4_to_16_gold = 19.75 #需要消耗19.75金
l4_to_16_vit = 10
''''
已知1颗6级石头的市场售价为750，请问是自己合成划算还是直接购买划算
其他数据:
    1 Diamond --> 0.05 Gold
    1 Vit --> 1 Gold
'''
diamond_value=0.05
vit_value = 1
l6_market_value = 750
'''
def econ():
    def stone_1(num_1=1):
        l1_stone_cost = (l1_value + diamond_value * l1_value_diamond)*num_1
        #print('Total cost of Level 1 stone is: ' + str(l1_stone_cost) + ' gold')
        return l1_stone_cost
    def stone_3 (num_3=1):
        l3_stone_cost = (round(stone_1(l1_to_13) + l1_to_13_gold + l1_to_13_vit,3))*num_3
        print('Total cost of Level 1 stone is: ' + str(stone_1(1)) + ' gold')
        print('Total cost of Level 3 stone is: ' + str(l3_stone_cost) + ' gold')
        return l3_stone_cost
    def stone_4 (num_4=1):
        l4_stone_cost = ((l3_to_14_rate*(stone_3(1) + stone_1(l3_to_14)+l3_to_14_gold + l3_to_14_vit))+(1-l3_to_14_rate)*(stone_1(l3_to_14)+l3_to_14_gold))/l3_to_14_rate* num_4
        print('Total cost of Level 4 stone is: ' + str(round(l4_stone_cost,3)) + ' gold')
        return l4_stone_cost

    def stone_6 (num_6=1):
        l6_total_cost = (stone_4(l4_to_16) +l4_to_16_gold +l4_to_16_vit)*num_6

        print('Total cost of Level 6 stone is: ' + str(round(l6_total_cost,3)) + ' gold')        
        return l6_total_cost 
    def empty():
        return
     
    if stone_6() >= l6_market_value:
        print('It is more worth for buying it')
    else:
        print('it is more worth for making it') 
'''      
def stone_1(num_1=1):
    l1_stone_cost = (l1_value + diamond_value * l1_value_diamond)*num_1
    #print('Total cost of Level 1 stone is: ' + str(l1_stone_cost) + ' gold')
    return l1_stone_cost
def stone_3 (num_3=1):
    l3_stone_cost = (round(stone_1(l1_to_13) + l1_to_13_gold + l1_to_13_vit,3))*num_3
    print('Total cost of Level 1 stone is: ' + str(stone_1(1)) + ' gold')
    print('Total cost of Level 3 stone is: ' + str(l3_stone_cost) + ' gold')
    return l3_stone_cost
def stone_4 (num_4=1):
    l4_stone_cost = ((l3_to_14_rate*(stone_3(1) + stone_1(l3_to_14)+l3_to_14_gold + l3_to_14_vit))+(1-l3_to_14_rate)*(stone_1(l3_to_14)+l3_to_14_gold))/l3_to_14_rate* num_4
    print('Total cost of Level 4 stone is: ' + str(round(l4_stone_cost,3)) + ' gold')
    return l4_stone_cost

def stone_6 (num_6=1):

    l6_total_cost = (stone_4(l4_to_16) +l4_to_16_gold +l4_to_16_vit)*num_6
    print('Total cost of Level 6 stone is: ' + str(round(l6_total_cost,3)) + ' gold')      
    return l6_total_cost 

if stone_6() >= l6_market_value:
    print('It is more worth for buying it')
else:
    print('it is more worth for making it') 