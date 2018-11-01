import sys
from random import randint
import re
global winners
winners=[]
lotto='Cash5_apr.txt'
date='today'
picks='picks.txt'
lotto_out='Pick5.txt'
pick_list=[]
pick_data=[]
Ranked_List=[]
all_nums=[]
def pick_my_nums():
    for num in final_picks:
        for pick_num in range(2,len_of_final_picks, 2):
            pick_list=pick_list.append(final_picks[pick_num])
            len_of_pick_list=len(pick_list)
            if len_of_pick_list > 5:
                pick_data=pick_data.append(pick_list)
                pick_list=[]
    print (pick_data)
            
            
    
Fibs=[1,2,3,4,5,6,7,8,9,10,13,17,19,21,23,25,27,29,32,34,38,41,42,43,44,51,52,55,63,66,72,76,81,83,85,88,96,100,110,120,130,131,132,133]
def check_line(linein):
    global all_nums
    winout=''
    #new_winners=[]
    winners=re.split(' |/|\t|\n',linein)
    #print (winners)
    win_len=len(winners)
    #print (win_len)
    if win_len == 5:
        print (winners, 'in the def')
        lownums.append(winners[0])
        secnd_num.append(winners[1])
        thrd_num.append(winners[2])
        forth_num.append(winners[3])
        fifth_num.append(winners[4])
        #all_nums.append(winners)
        for item in range(win_len):
            if winners[item]:
                print (winners[item])
                item_out=''.join(winners[item])
                winout=winout + ' ' + item_out
                all_nums.append(winners[item])

        winout=winout+'\n'
        #print(winners, 'winners')
        #print (winout, 'winout winners')
        fo.write(winout)
        return (winners)
    
    print (winners, win_len)



def Rank_numbers():
    global all_nums
    global Len_All_Nums
    global Ranked_List
    Len_All_Nums=len(all_nums)
    #for num in range(0,Len_All_Nums):
    for num in range(0,50):
        compnum=str(num).zfill(2)
        #print('this is it', Len_All_Nums, num)
        for LAN in range(1,43):
            add=0
            #print(compnum, all_nums[LAN], int(all_nums[LAN]))
            comp=all_nums[LAN].strip("'")
            Rank_len=len(Ranked_List)
            if compnum == comp:
                #print ('we got a hit')
                for check in range(0, Rank_len):
                    if Ranked_List[check] == compnum:
                        #print ('already on this list')
                        add=1
                if add == 0:
                    #print('Need to add it')
                    Ranked_List.append(num)
                    break


##print (lotto)
output=''
hist=''
f1=open(lotto, 'r')
f2=open(picks, 'w')
fo=open(lotto_out,'w')
line_length=0
count=0
num_list = []
#winners = []
tot_list = []
lownums = []
secnd_num = []
thrd_num = []
forth_num = []
Hit_count = []
fifth_num = []
all_nums = []
final_picks = []

linein=f1.readline()
while linein :
    linein=linein.rstrip()
    check_line(linein)
    line_length=len(winners)
    #hist=hist.append(linein)
    #print (winners, 'this is a test')
    
    linein=f1.readline()

fo.close()

Rank_numbers()
print (secnd_num)
print (all_nums)
Fib_Search=len(Fibs)
for Fib_num in range(Fib_Search):
    print (Fib_num)
    print (Fibs[Fib_num])
    print (all_nums[Fibs[Fib_num]],'Pick')
    final_picks.append(all_nums[Fibs[Fib_num]])
    outline=str(final_picks)+'What is this'

set_of_picks=set(final_picks)
final_picks=list(set_of_picks)
final_picks=sorted(final_picks)
pick_num=len(set_of_picks)
long_pick_num=pick_num-1
pick_num=pick_num-3  # so we dont go over - should put a try and die

for value in range(1,pick_num):
    
    mypick=" ".join(final_picks[value])

print ('mypick')
print (mypick)
mylen=len(mypick)
length_of_picks=len(set_of_picks)
print('length of picks', length_of_picks)
# So final_picks is a  set of unique number from the "pick_nums" and we will pick from them
for i in range(0,4):
    j=length_of_picks-(i+15)
    k=length_of_picks-(i+8)
    l=length_of_picks-(i+5)
    m=length_of_picks-(i+2)    
    #print(final_picks[i], final_picks[j], final_picks[k], final_picks[l], final_picks[m])
    pickum=[final_picks[i], final_picks[j], final_picks[k], final_picks[l], final_picks[m]]
    #pickum=tuple(pickum)
    my_pick_set=sorted(pickum)
    print(my_pick_set, 'sorted Picks!')

print('final picks')
print (final_picks)
print ('now for the long list', long_pick_num)
print ('These are the picks selected from the small subset of numbers')
for i in range(0,6,2):
    j=i+3
    k=i+5
    m=i+8
    l=i+12
    n=int(long_pick_num - (i))
       # n=pick_num-(long_pick_num - j)m
       # k=j-2
       #l=j-i
       # la=j-i
    #picks=(final_picks[i],final_picks[j],final_picks[k],final_picks[l],final_picks[m],final_picks[n])
    #sum_of_picks=sum(picks)
    print( final_picks[j], final_picks[k], final_picks[l], final_picks[m], final_picks[n])
    
#f2.close()

print ('picks', all_nums[9], all_nums[15], all_nums[23], all_nums[31], all_nums[68])
print ('picks', all_nums[11], all_nums[12], all_nums[22], all_nums[33], all_nums[66])
print('Play these final_picks')
print(final_picks[3], final_picks[5], final_picks[12], final_picks[14], final_picks[20])
print(final_picks[2], final_picks[6], final_picks[11], final_picks[18], final_picks[19])
print(final_picks[7], final_picks[9], final_picks[12], final_picks[16], final_picks[21])

print(my_pick_set)

print(final_picks)

print ('Ranked list', Ranked_List)
