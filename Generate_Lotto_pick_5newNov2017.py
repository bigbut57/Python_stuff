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
Final_Rank_list=[]
Final_Num_list=[]



def pick_my_nums():
    for num in final_picks:
        for pick_num in range(2,len_of_final_picks, 2):
            pick_list=pick_list.append(final_picks[pick_num])
            len_of_pick_list=len(pick_list)
            if len_of_pick_list > 5:
                pick_data=pick_data.append(pick_list)
                pick_list=[]
    print (pick_data)
            
            
    

def check_line(linein):
    global all_nums
    winout=''
    #new_winners=[]
    winners=re.split(' |/|\t|\n',linein)
    #print (winners)
    win_len=len(winners)
    #print (win_len)
    if win_len == 5:
        #print (winners, 'in the def')
        lownums.append(winners[0])
        secnd_num.append(winners[1])
        thrd_num.append(winners[2])
        forth_num.append(winners[3])
        fifth_num.append(winners[4])
        #all_nums.append(winners)
        for item in range(win_len):
            if winners[item]:
                #print (winners[item])
                item_out=''.join(winners[item])
                winout=winout + ' ' + item_out
                all_nums.append(winners[item])

        winout=winout+'\n'
        #print(winners, 'winners')
        #print (winout, 'winout winners')
        fo.write(winout)
        return (winners)
    
    #print (winners, win_len)



def Rank_numbers():
    global all_nums
    global Len_All_Nums
    global Ranked_List
    Ranked_List.append(all_nums[0])
    Len_All_Nums=len(all_nums)
    #for num in range(0,Len_All_Nums):
    for num in range(0,43):
        compnum=str(num).zfill(2)
        #print('this is it', Len_All_Nums, num)
        for LAN in range(0,300):
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
                    if num==0:
                        Num='0'
                    else:
                        Num=str(num)
                    value=num
                    Ranked_List.append(value)
                    break


##print (lotto)
output=''
hist=''
f1=open(lotto, 'r')
f2=open(picks, 'w')
fo=open(lotto_out,'w')
line_length=0
count=0
num_list=[]
#winners=[]
tot_list=[]
lownums=[]
secnd_num=[]
thrd_num=[]
forth_num=[]
Hit_count=[]
fifth_num=[]
all_nums=[]
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
#print (secnd_num)
#print (all_nums)
print(Ranked_List)

set_of_picks=set(final_picks)
final_picks=list(set_of_picks)
final_picks=sorted(final_picks)
pick_num=len(set_of_picks)
long_pick_num=pick_num-1
pick_num=pick_num-3  # so we dont go over - should put a try and die

for value in range(1,pick_num):
    
    mypick=" ".join(final_picks[value])

Num_list=[]
Num_Rank_list=[]

print(Ranked_List)
ranked_len=len(Ranked_List)
for num in range(0,ranked_len):
    if num==0:
        Lotto_num=Ranked_List[num]
        Lotto_rank=0
        Num_list.append(Lotto_num)
        Num_Rank_list.append(Lotto_rank)
    else:
        Split_Val=Ranked_List[num].split(':')
        Lotto_num=Split_Val[0]
        Lotto_rank=Split_Val[1]
        #print(Split_Val)
        Num_list.append(Lotto_num)
        Num_Rank_list.append(Lotto_rank)

print( Num_list)
print ('###################')
print (Num_Rank_list)
## Begin the list

for idx in range(0,42):
    for rank in range(0,300):
        val1=int(Num_list[idx])
        Rank=Num_Rank_list[idx]
        #print (rank, Rank, Num_Rank_list[idx] ,Num_list[idx], val1)
        #print ('%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
        if rank == val1:
            RANK=int(Rank)+1
            Final_Rank_list.append(val1)
            Final_Num_list.append(RANK)
            break

            
for pick in range(2,12,3):
    aa=pick + 3
    bb=pick + 8
    cc=pick +13
    dd=pick + 21
    print(Num_list[pick],Num_list[aa],Num_list[bb],Num_list[cc],Num_list[dd])
    
    
for pick in range(6,18,5):
    aa=pick + 3
    bb=pick + 8
    cc=pick +13
    dd=pick + 21
    print(Num_list[pick],Num_list[aa],Num_list[bb],Num_list[cc],Num_list[dd])
    
print(Final_Rank_list)
print(Final_Num_list)

print(Num_Rank_list)



