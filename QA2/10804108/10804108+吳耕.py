#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
class Similarity:
    def __init__(self,cosine,ejaccard,correlation_1,correlation_2):
        self.cosine = cosine(x,y)
        self.ejaccard = cosine(x,y)
        self.correlation_1 = correlation_1(x,y)
        self.correlation_2 = correlation_2(x,y)
    def cosine(x,y):
        dot = np.dot(x,np.transpose(y))
        norm_x = np.linalg.norm(x)
        norm_y = np.linalg.norm(y)
        cosine = dot / (norm_x * norm_y)
        return cosine
    def ejaccard(x,y):
        dot = np.dot(x,np.transpose(y))
        x_x = np.dot(x,np.transpose(x))
        y_y = np.dot(y,np.transpose(y))
        ejac = dot / (x_x + y_y-dot)
        return ejac
    def correlation_1(x,y):
        cor_std_x=np.sqrt(np.sum((x-np.mean(x))*(np.transpose(x-np.mean(x))))/(len(x)-1))
        cor_std_y=np.sqrt(np.sum((y-np.mean(y))*(np.transpose(y-np.mean(y))))/(len(y)-1))
        cor_x = (x-np.mean(x))/cor_std_x
        cor_y = (y-np.mean(y))/cor_std_y
        correlation_1 = (np.dot(cor_x,np.transpose(cor_y)))/((np.sqrt(np.dot(cor_x,np.transpose(cor_x))))*(np.sqrt(np.dot(cor_y,np.transpose(cor_y)))))
        return correlation_1
    def correlation_2(x,y):
        cor_std_x=np.sqrt(np.sum((x-np.mean(x))*(np.transpose(x-np.mean(x))))/(len(x)-1))
        cor_std_y=np.sqrt(np.sum((y-np.mean(y))*(np.transpose(y-np.mean(y))))/(len(y)-1))
        correlation_2=np.dot(x-np.mean(x),np.transpose(y-np.mean(y)))/((len(x)-1)*cor_std_x*cor_std_y)
        return correlation_2
#-----------------------------------------------------------------------------------------------------
if __name__=='__main__':
    q = np.array([1,1,0])
    x1 = np.array([2,2,0]) 
    x2 = np.array([0,1,1])
    x3 = np.array([1,-1,0])
    x4 = np.array([0,0,1])
    # Correlation相似度用了兩種方法做，爲了美觀不重複:q和x1,x2用方法一,q和x3,x4用方法二。
    print(f'''q和x1的Cosine,Extended Jaccard以及Correlation相似度分别为:
    [{Similarity.cosine(q,x1)},{Similarity.ejaccard(q,x1)},{Similarity.correlation_1(q,x1)}]''')
    print(f'''q和x2的Cosine,Extended Jaccard以及Correlation相似度分别为:
    [{Similarity.cosine(q,x2)},{Similarity.ejaccard(q,x2)},{Similarity.correlation_1(q,x2)}]''')
    print(f'''q和x3的Cosine,Extended Jaccard以及Correlation相似度分别为:
    [{Similarity.cosine(q,x3)},{Similarity.ejaccard(q,x3)},{Similarity.correlation_2(q,x3)}]''')
    print(f'''q和x4的Cosine,Extended Jaccard以及Correlation相似度分别为:
    [{Similarity.cosine(q,x4)},{Similarity.ejaccard(q,x4)},{Similarity.correlation_2(q,x4)}]''')


# In[3]:


#另一組數據用老師簡報上的數據
if __name__=='__main__':
    x = [-3,-2,-1,0,1,2,3]
    y = [0,2,4,6,8,10,12]
    z = [9,4,1,0,1,4,9,]
    print(f'''x和y的Cosine,Extended Jaccard以及Correlation相似度分别为:
    [{Similarity.cosine(x,y)},{Similarity.ejaccard(x,y)},{Similarity.correlation_1(x,y)}]''')
    print(f'''x和z的Cosine,Extended Jaccard以及Correlation相似度分别为:
    [{Similarity.cosine(x,z)},{Similarity.ejaccard(x,z)},{Similarity.correlation_2(x,z)}]''')


# In[ ]:




