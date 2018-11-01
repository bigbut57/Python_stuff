import sys
from random import randint
lotto='Cash5_apr.txt'
date='today'
picks='pickstuff'
Hit_gap_list=list(range(0,69))
Fibs=[1,2,3,5,8,13,21,34,55,89,144,155,4,8,16,32,64,128,156,125,47,19,99,20,33,168,93,27,52,32,192,60]
##print (lotto)
output=''
hist=''
f1=open(lotto, 'r')
f2=open(picks, 'w')
linein=f1.readline()
line_length=0
count=0
num_list = []
winners = []
tot_list = []
lownums = []
secnd_num = []
thrd_num = []
forth_num = []
Hit_count = []
Hit_gap_table = []
fifth_num = []
global all_nums
all_nums = []
final_picks = []

while linein :
    #if "/".find(linein):
      #  linein=f1.readline()
    #if "$".find(linein):
       # linein=f1.readline()
    #if not linein.strip():
        #linein=f1.readline()
    line_length=len(linein)
    winners=linein.split()
    print (linein,winners[0:5])
    
    #hist=hist.append(linein)
    #####print (winners)
    wincount=len(winners)
    print (winners)
    
    ####print (wincount)
    if wincount == 5:  # dont process blank lines
        lownum=winners[0]
        midlow=winners[1]
        middle=winners[2]
        midhigh=winners[3]
        highnum=winners[4]
        
        diff=int(highnum)-int(lownum)
        diff2=int(midhigh)-int(midlow)
        ##print(lownum, highnum, diff, diff2)
        lownums.append(lownum)
        secnd_num.append(midlow)
        thrd_num.append(middle)
        forth_num.append(midhigh)
        fifth_num.append(highnum)
        
        for hit in range(1,43):
            hit_table=(hit)
            

        
        for number in range(0,5):
            #print (winners[number], "Number")
            all_nums.append(winners[number])
          
    linein=f1.readline()
hit_chart=[]
###build the hit chart

for i in range(0,len(all_nums),5):
    j=i+5
    print (all_nums[i:j])
    hit_simple=(all_nums[i:j])
    ##print (hit_simple)
    hit=set(hit_simple)
    #print(hit)
    for k in range(1,44):
        test=str(k).zfill(2)
        
        #print ("test, k",test,k)
        if test in hit:
            hit_chart.append('#')
            #print ("got a match", test, k)
            #print(hit, 'X', test)
        else:
            hit_chart.append('-')
            #print(hit, '#', test)
    begin= ((j-4)*43)
    end=begin+43
    #print ( 'hit chart', hit_chart )
    
    
                           
#print (all_nums)


hit_length=(200 )
##hit_length=(all_nums * 8 )
for i in range(0,hit_length,43):
    hit_string=''
    for j in range(i,(i+43)):
        hit_string=hit_string+(hit_chart[j]).strip("'")
    print (hit_chart[i:j])
    hit_string.strip("'")
    print (hit_string)
    
print ('\n\n\n\n')

#print (hit_chart)
#for i in range(0,len(hit_length),68):
   # j=i+34
   # ja=j+1
    #k=ja+34
    
    #print (hit_chart[ja:k])
    #print ('')
                             
#print (hit_string)
