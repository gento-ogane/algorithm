#!/usr/bin/env python
# coding: utf-8

for i in range(1,n):#比べる必要があり、２個から始める。
    v=l[i]
    j=i-1
    while j>=0 and v<l[j]:#後ろから並べていく
        l[j+1]=l[j]
        j-=1
    l[j+1]=v
    print(*l)


n = int(input())
l = list(map(int, input().split()))



def inserted_sort(r,n):
    for i in range(1,n):#1からでよい、「ソート済みj領域」と「未ソートi」を比べるアルゴリズムなので
        v=r[i]#ずらす必要が会った時に、右端が上書きされてしまうので、格納しておく場所
        j=i-1#A[i]の一つ左から始める
        while j>=0 and r[j]<v:#jは0まで満遍なくみる。入れ替えるポイントを見つけ次第反応する。>で昇順、<で降順
            r[j+1]=r[j]#右へずらしていく。
            j-=1#jは右端から数えているので、-する
        r[j+1]=v#ループ抜けたあとに処理するが、ここでjはwhile文で引かれているので、+1しておく
    print(*r)


# In[16]:


inserted_sort(l,n)


# In[8]:


n = int(input())
l = list(map(int, input().split()))


# In[ ]:


def a(r,n):
    for i in range(1,n):
        v=r[i]
        j=i-1
        while j>=0 and r[j]<[i]:
            r[j+1]=r[j]
        j-=1
        r[j+1]=v
    

