#!/usr/bin/env python
# coding: utf-8

# ### MATRICES / NUMPY -----
# 
# * Matrix is the tabular representation of the data
# * Lot of datas are stored in table format,that is why Matrices is very very important topic in python
# * as we working on dataframe so matrices are played a major rule 
# * List is one dimension & matrix is multidimension
# * indexation is very important to plot the datapoints
# * we will see tht & we gonna analyze the NBA players  
# * hear i have taken top 10 highest paid player in 2015-2016 season
# * we will analyze how 10 players have been playing over the past 10 years & we had the data for past 10 yrs 
# * our main goal is to find trends,patterns & their performance for the past 10 yrs
# * Now i will explain with matrices ##

# In[149]:


#Import numpy
import numpy as np


# # Seasons

# In[150]:


Seasons = ["2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"]



# In[151]:


Sdict = {"2010":0,"2011":1,"2012":2,"2013":3,"2014":4,"2015":5,"2016":6,"2017":7,"2018":8,"2019":9}


# # Players

# In[152]:


Players = ["Sachin","Rahul","Smith","Sami","Pollard","Morris","Samson","Dhoni","Kohli","Sky"]


# In[153]:


Pdict = {"Sachin":0,"Rahul":1,"Smith":2,"Sami":3,"Pollard":4,"Morris":5,"Samson":6,"Dhoni":7,"Kohli":8,"Sky":9}


# # Salaries

# In[154]:


Sachin_Salary = [15946875,17718750,19490625,21262500,23034375,24806250,25244493,27849149,30453805,23500000]
Rahul_Salary = [12000000,12744189,13488377,14232567,14976754,16324500,18038573,19752645,21466718,23180790]
Smith_Salary = [4621800,5828090,13041250,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
Sami_Salary = [3713640,4694041,13041250,14410581,15779912,17149243,18518574,19450000,22407474,22458000]
Pollard_Salary = [4493160,4806720,6061274,13758000,15202590,16647180,18091770,19536360,20513178,21436271]
Morris_Salary = [3348000,4235220,12455000,14410581,15779912,14500000,16022500,17545000,19067500,20644400]
Samson_Salary = [3144240,3380160,3615960,4574189,13520500,14940153,16359805,17779458,18668431,20068563]
Dhoni_Salary = [0,0,4171200,4484040,4796880,6053663,15506632,16669630,17832627,18995624]
Kohli_Salary = [0,0,0,4822800,5184480,5546160,6993708,16402500,17632688,18862875]
Sky_Salary = [3031920,3841443,13041250,14410581,15779912,14200000,15691000,17182000,18673000,15000000]


# # Matrix

# In[155]:


Salary = np.array([Sachin_Salary, Rahul_Salary, Smith_Salary, Sami_Salary, Pollard_Salary, Morris_Salary, Samson_Salary, Dhoni_Salary, Kohli_Salary, Sky_Salary])


# # Games 

# In[156]:


Sachin_G = [80,77,82,82,73,82,58,78,6,35]
Rahul_G = [82,57,82,79,76,72,60,72,79,80]
Smith_G = [79,78,75,81,76,79,62,76,77,69]
Sami_G = [80,65,77,66,69,77,55,67,77,40]
Pollard_G = [82,82,82,79,82,78,54,76,71,41]
Morris_G = [70,69,67,77,70,77,57,74,79,44]
Samson_G = [78,64,80,78,45,80,60,70,62,82]
Dhoni_G = [35,35,80,74,82,78,66,81,81,27]
Kohli_G = [40,40,40,81,78,81,39,0,10,51]
Sky_G = [75,51,51,79,77,76,49,69,54,62]


# # Matrix

# In[157]:


Games = np.array([Sachin_G, Rahul_G, Smith_G, Sami_G, Pollard_G, Morris_G, Samson_G, Dhoni_G, Kohli_G, Sky_G])


# # Points

# In[158]:


Sachin_PTS = [2832,2430,2323,2201,1970,2078,1616,2133,83,782]
Rahul_PTS = [1653,1426,1779,1688,1619,1312,1129,1170,1245,1154]
Smith_PTS = [2478,2132,2250,2304,2258,2111,1683,2036,2089,1743]
Sami_PTS = [2122,1881,1978,1504,1943,1970,1245,1920,2112,966]
Pollard_PTS = [1292,1443,1695,1624,1503,1784,1113,1296,1297,646]
Morris_PTS = [1572,1561,1496,1746,1678,1438,1025,1232,1281,928]
Samson_PTS = [1258,1104,1684,1781,841,1268,1189,1186,1185,1564]
Dhoni_PTS = [903,903,1624,1871,2472,2161,1850,2280,2593,686]
Kohli_PTS = [597,597,597,1361,1619,2026,852,0,159,904]
Sky_PTS = [2040,1397,1254,2386,2045,1941,1082,1463,1028,1331]


# # Matrix

# In[159]:


Points = np.array([Sachin_PTS, Rahul_PTS, Smith_PTS, Sami_PTS, Pollard_PTS, Morris_PTS, Samson_PTS, Dhoni_PTS, Kohli_PTS, Sky_PTS])             


# In[160]:


Salary # martrix format


# In[161]:


# Building your first matrix -
Games


# In[162]:


Points


# In[163]:


mydata = np.arange(0,20)
print(mydata) 


# In[164]:


np.reshape(mydata,(4,5))


# In[165]:


mydata


# In[166]:


MATR1 = np.reshape(mydata, (5,4), order = 'c')
MATR1


# In[167]:


MATR1


# In[168]:


MATR1[4,3] 


# In[169]:


MATR1[3,3]


# In[170]:


MATR1


# In[171]:


MATR1[-3,-1] 


# In[172]:


MATR1


# In[173]:


mydata


# In[174]:


MATR2 = np.reshape(mydata, (5,4), order = 'F')


# In[175]:


MATR2


# In[176]:


MATR2[4,3]


# In[177]:


MATR2[0,2]


# In[178]:


MATR2[0:2] 


# In[179]:


MATR2


# In[180]:


MATR2[1:2] 


# In[181]:


MATR2[1,2] 


# In[182]:


MATR2


# In[183]:


MATR2[-2,-1]  


# In[184]:


MATR2[-3,-3]  


# In[185]:


MATR2


# In[186]:


MATR2[0:2]  


# In[187]:


mydata


# In[188]:


MATR3 = np.reshape(mydata, (5,4), order = 'A')
MATR3


# In[189]:


MATR2


# In[190]:


MATR1 


# In[191]:


a1 = ['welcome', 'to','datascience']
a2 = ['required','hard','work' ]
a3 = [1,2,3] 


# In[192]:


[a1,a2,a3]


# In[193]:


[a1+a2+a3]


# In[194]:


np.array([a1,a2,a3])


# In[195]:


Games


# In[196]:


Games[0] 


# In[197]:


Games[5] 


# In[198]:


Games[0:5] 


# In[199]:


Games[0,5] 


# In[200]:


Games[0,2] 


# In[201]:


Games


# In[202]:


Games[0:2]


# In[203]:


Games


# In[204]:


Games[1:2] 


# In[205]:


Games[2] 


# In[206]:


Games


# In[207]:


Games[2,8] 


# In[208]:


Games


# In[209]:


Games[-3:-1] 


# In[210]:


Games[-3,-1] 


# In[211]:


Points


# In[212]:


Points[0]


# In[213]:


Points[6,1] 


# In[214]:


Points[3:6] 


# In[215]:


Points


# In[216]:


Points[-6,-1] 


# # ====== DICTIONARY =======
# 

# In[217]:


dict1 = {'key1':'val1', 'key2':'val2', 'key3':'val3'}


# In[218]:


dict1


# In[219]:


dict1['key2'] 


# In[220]:


dict2 = {'bang':2,'hyd':'we are hear', 'pune':True}


# In[221]:


dict2


# In[222]:


dict3 = {'Germany':'I have been here', 'France':2, 'Spain': True}


# In[223]:


dict3


# In[224]:


dict3['Germany'] 


# In[225]:


Games


# In[226]:


Pdict


# In[227]:


Pdict['Sachin']


# In[228]:


Games[0] 


# In[229]:


Games


# In[230]:


Pdict['Rahul']


# In[231]:


Games[1]


# # Games

# In[232]:


Games[Pdict['Rahul']]


# In[233]:


Points


# In[234]:


Salary


# In[235]:


Salary[2,4]


# In[236]:


Salary


# In[237]:


Salary[Pdict['Sky']][Sdict['2019']]


# In[238]:


Salary[Sdict['2019']]


# In[239]:


Games


# In[240]:


Salary/Games


# In[241]:


np.round(Salary/Games) 


# In[242]:


import warnings
warnings.filterwarnings("ignore")


# In[243]:


import matplotlib.pyplot as plt


# In[244]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[245]:


Salary


# In[246]:


Salary[0]


# In[247]:


Pdict


# In[248]:


Games[5]


# In[249]:


Pdict


# In[250]:


Games[Pdict['Dhoni']]


# In[251]:


Points[6]


# In[252]:


import warnings
warnings.filterwarnings('ignore')


# In[253]:


import numpy as np 
import matplotlib.pyplot as plt


# In[254]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[255]:


Salary


# In[256]:


Salary[0] 


# In[257]:


plt.plot(Salary[0]) 


# In[258]:


plt.plot(Salary[0], c='red') 


# In[259]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize'] = 10,6 


# In[260]:


plt.plot(Salary[0], c='Blue', ls = 'dashed')


# In[261]:


plt.plot(Salary[0], c='Green', ls = '--', marker = 's')


# In[262]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize'] = 10,8


# In[263]:


plt.plot(Salary[0], c='Green', ls = '--', marker = 's', ms = 10)
plt.show()


# In[264]:


list(range(0,10))


# In[265]:


Sdict


# In[266]:


Pdict


# In[267]:


plt.plot(Salary[0], c='Green', ls = '--', marker = 's', ms = 7)
plt.xticks(list(range(0,10)), Seasons) 
plt.show() 


# In[268]:


plt.plot(Salary[0], c='Green', ls = ':', marker = 's', ms = 7, label = Players[0])
plt.xticks(list(range(0,10)), Seasons,rotation='vertical')
plt.show()


# In[269]:


Games


# In[270]:


plt.plot(Salary[0], c='Green', ls = '--', marker = 's', ms = 7, label = Players[0])
plt.xticks(list(range(0,10)), Seasons,rotation='horizontal')
plt.show()


# In[271]:


Salary[0]


# In[272]:


Salary[1]


# In[273]:


plt.plot(Salary[1], c='Blue', ls = ':', marker = 'o', ms = 10, label = Players[1])


# In[274]:


plt.plot(Salary[0], c='Green', ls = '--', marker = 's', ms = 10, label = Players[0])
plt.plot(Salary[1], c='Blue', ls = ':', marker = 'o', ms = 10, label = Players[1])

plt.xticks(list(range(0,10)), Seasons,rotation='vertical')

plt.show()


# In[275]:


plt.plot(Salary[0], c='Green', ls = '--', marker = 's', ms = 7, label = Players[0])
plt.plot(Salary[1], c='Blue', ls = '--', marker = 'o', ms = 5, label = Players[1])
plt.plot(Salary[2], c='purple', ls = '--', marker = '^', ms = 8, label = Players[2])


plt.xticks(list(range(0,10)), Seasons,rotation='vertical')

plt.show()


# In[276]:


plt.plot(Salary[0], c='Green', ls = '--', marker = 's', ms = 7, label = Players[0])
plt.plot(Salary[1], c='Blue', ls = '-', marker = 'o', ms = 5, label = Players[1])
plt.plot(Salary[2], c='purple', ls = '--', marker = '^', ms = 8, label = Players[2])
plt.plot(Salary[3], c='Red', ls = ':', marker = 'd', ms = 8, label = Players[3])

plt.xticks(list(range(0,10)), Seasons,rotation='vertical')

plt.show()


# In[277]:


plt.plot(Salary[0], c='Green', ls = '--', marker = 's', ms = 7, label = Players[0])
plt.plot(Salary[1], c='Blue', ls = ':', marker = 'o', ms = 5, label = Players[1])
plt.plot(Salary[2], c='purple', ls = '-', marker = '^', ms = 8, label = Players[2])
plt.plot(Salary[3], c='Red', ls = '--', marker = 'd', ms = 8, label = Players[3])
plt.legend() 
plt.xticks(list(range(0,10)), Seasons,rotation='vertical')

plt.show()


# In[278]:


plt.plot(Salary[0], c='Green', ls = '--', marker = 's', ms = 7, label = Players[0])
plt.plot(Salary[1], c='Blue', ls = '--', marker = 'o', ms = 5, label = Players[1])
plt.plot(Salary[2], c='Green', ls = '--', marker = '^', ms = 8, label = Players[2])
plt.plot(Salary[3], c='Red', ls = '--', marker = 'd', ms = 8, label = Players[3])
plt.legend(loc = 'upper right',bbox_to_anchor=(1,0) )
plt.xticks(list(range(0,10)), Seasons,rotation='vertical')

plt.show()


# In[279]:


plt.plot(Salary[0], c='Green', ls = '--', marker = 's', ms = 7, label = Players[0])
plt.plot(Salary[1], c='Blue', ls = '--', marker = 'o', ms = 5, label = Players[1])
plt.plot(Salary[2], c='Green', ls = '--', marker = '^', ms = 8, label = Players[2])
plt.plot(Salary[3], c='Red', ls = '--', marker = 'd', ms = 8, label = Players[3])
plt.legend(loc = 'lower right',bbox_to_anchor=(0.5,1) )
plt.xticks(list(range(0,10)), Seasons,rotation='vertical')

plt.show()


# In[280]:


plt.plot(Salary[0], c='Green', ls = '--', marker = 's', ms = 7, label = Players[0])
plt.plot(Salary[1], c='Blue', ls = '--', marker = 'o', ms = 7, label = Players[1])
plt.plot(Salary[2], c='Green', ls = '--', marker = '^', ms = 7, label = Players[2])
plt.plot(Salary[3], c='Purple', ls = '--', marker = 'D', ms = 7, label = Players[3])
plt.plot(Salary[4], c='Black', ls = '--', marker = 's', ms = 7, label = Players[4])
plt.plot(Salary[5], c='Red', ls = '--', marker = 'o', ms = 7, label = Players[5])
plt.plot(Salary[6], c='Red', ls = '--', marker = '^', ms = 7, label = Players[6])
plt.plot(Salary[7], c='Red', ls = '--', marker = 'd', ms = 7, label = Players[7])
plt.plot(Salary[8], c='Red', ls = '--', marker = 's', ms = 7, label = Players[8])
plt.plot(Salary[9], c='Red', ls = '--', marker = 'o', ms = 7, label = Players[9])

plt.legend(loc = 'lower right',bbox_to_anchor=(0.5,1) )
plt.xticks(list(range(0,10)), Seasons,rotation='vertical')

plt.show()


# In[281]:


plt.plot(Games[0], c='Green', ls = '--', marker = 's', ms = 7, label = Players[0])
plt.plot(Games[1], c='Blue', ls = '--', marker = 'o', ms = 7, label = Players[1])
plt.plot(Games[2], c='Green', ls = '--', marker = '^', ms = 7, label = Players[2])
plt.plot(Games[3], c='Red', ls = '--', marker = 'D', ms = 7, label = Players[3])
plt.plot(Games[4], c='Black', ls = '--', marker = 's', ms = 7, label = Players[4])
plt.plot(Games[5], c='Blue', ls = '--', marker = 'o', ms = 7, label = Players[5])
plt.plot(Games[6], c='red', ls = '--', marker = '^', ms = 7, label = Players[6])
plt.plot(Games[7], c='Green', ls = '--', marker = 'd', ms = 7, label = Players[7])
plt.plot(Games[8], c='Red', ls = '--', marker = 's', ms = 7, label = Players[8])
plt.plot(Games[9], c='Blue', ls = '--', marker = 'o', ms = 7, label = Players[9])

plt.legend(loc = 'lower right',bbox_to_anchor=(0.5,1) )
plt.xticks(list(range(0,10)), Seasons,rotation='vertical')

plt.show()


# In[ ]:





# In[282]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize']=8,5


# In[283]:


plt.plot(Salary[0],color='r',marker='o',linestyle='-.',ms='8',label=Players[0])
plt.plot(Salary[1],color='g',marker='o',linestyle='-.',ms='8',label=Players[1])
plt.legend(loc="upper left")
plt.xticks(np.arange(0,10),Seasons)

plt.show() 


# In[284]:


plt.plot(Games[0])


# In[ ]:





# In[285]:


plt.plot(Points[0])

