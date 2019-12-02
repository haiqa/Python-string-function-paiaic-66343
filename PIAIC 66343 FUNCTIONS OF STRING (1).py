#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT PYTHON #TIMING 9:00 TO 12:00

# # PYTHON STRING BUITL IN FUNCTIONS 

# ## PIAIC 66343 HAIQA SUHAIL 

# In[2]:


n='Haiqa Suhail'
dir(n)


# In[4]:


name='haiqa Suhail'
print(name)
print(name.capitalize()) #Only capitalize 1 character of string


# In[5]:


name='Haiqa Suhail'
print(name.casefold()) #lower all character of string


# In[6]:


name='Haiqa Suhail'
print(name.center(40)) #taking space of 40 character and pring name in the middle


# In[7]:


name='Haiqa Suhail'
print(name.count('a')) #print total number of a character like 'a'


# In[9]:


name='Haiqa Suhiål'
print(name.encode()) #encode the string


# In[10]:


name='Haiqa Suhåil'
print(name.endswith('l')) #compare with end character of string and reture true or false


# In[11]:


name='H\taiq suhåil'
print(name.expandtabs(3)) #space between the character


# In[12]:


name='haiqa suhail'
print(name.find('i')) #return the index of find character


# In[13]:


name='My Name is {fname} {lname}'
print(name.format(fname='Haiqa',lname='Suhail')) #Insert the fname and lname inside the placeholder{}, the fname and lname should be in fixed point


# In[14]:


name={'fname':'Haiqa', 'lname':'Suhail'}
print('{fname} {lname}'.format_map(name))


# In[15]:


name='Haiqa Suhail' 
print(name.index('S'))  #return the index of specific character


# In[16]:


name='Haiqa 1111' 
print(name.isalnum()) #return if string is alphanumeic or not e.g character and number


# In[17]:


name='HaiqaSuhail' 
print(name.isalpha()) #return true of false if string have all alphabets without space


# In[18]:


name='HaiqaSuhail' 
print(name.isascii())


# In[19]:


name='Haiqa Suhail' 
print(name.isdecimal()) #return if string have any decimal value


# In[20]:


name='Haiqa Suhail' 
print(name.isdigit()) #return if string have any digits


# In[21]:


name='HaiqaSuhail' 
print(name.isidentifier()) #return true or false if string have some identifier like start with _,or no space between word


# In[22]:


name='HaiqaSuhail'
print(name.islower()) #return true or false if string have all characters are lower case


# In[23]:


name='Haiqa Suhail'
print(name.isnumeric())
number='12'
print(number.isnumeric()) #return true or false if string have all characters are numeric


# In[24]:


name='Haiqa Suhail'
print(name.isprintable()) #return true or false if string have all characters are printable


# In[25]:


name='Haiqa Suhail'
print(name.isspace())
name='  '
print(name.isspace())  #returns True if all the characters in a string are whitespaces, otherwise False


# In[26]:


name='Haiqa Suhail'
print(name.istitle()) #return true or false if each word start with an upper case letter


# In[27]:


name='Haiqa Suhail'
print(name.isupper())
name='HAIQA SUHAIL'
print(name.isupper())  #return true or false if whole string will have upper case letter


# In[28]:


name={'Haiqa','Suhail'}
print('  '.join(name)) #method takes all items in an iterable and joins them into one string. A string must be specified as the separator.


# In[29]:


name='haiqa  '
name1=name.ljust(20)
print(name1,"suhail")  #return 20 character space from left justified


# In[30]:


name='Haiqa Suhail'
print(name.lower())  #return all character in lower case


# In[31]:


name='   Haiqa Suhail  '
print(name)
name='   Haiqa Suhail   '
print(name.lstrip())   #remove space for letf side


# In[32]:


name='Haiqa Suhail'
print(name.partition('Khalid'))  #return a tuple


# In[33]:


name='Haiqa Suhail'
print(name.replace('Haiqa','Suhail'))  #replace the word to another word


# In[34]:


name='Haiqa suhail'
print(name.rfind('l')) #return the index almost rindex(),if value not found return -1


# In[35]:


name='Haiqa Suhail'
print(name.rindex('S')) #return the index almost rindex(),if value not found return error


# In[36]:


name='Haiqa Suhail'
print(name.rjust(25)) #return a justified version of string


# In[38]:


name='Haiqa Suhail'
print(name.rpartition('Suhail'))


# In[39]:


name='Haiqa Suhail'
print(name.rsplit()) #return in list


# In[40]:


name='Nauman Khalid'
print(name.rstrip())


# In[41]:


name='Haiqa Suhail'
print(name.split())


# In[42]:


name='Haiqa Suhail'
print(name.splitlines()) #return a single work list


# In[43]:


name='Haiqa Suhail'
print(name.startswith('H'))
name='Haiqa Suhail'
print(name.startswith('S')) #return true or false if the given character are starting character of whole string


# In[44]:


name='Haiqa Suhail'
print(name.strip())


# In[45]:


name='Haiqa Suhail'
print(name.swapcase())  #return first character of every work in lower and other whole string will be UPPER case


# In[46]:


name='Haiqa Suhail'
print(name.title()) #convert the first character of every word in UPPER Case


# In[47]:


name='Haiqa Suhail'
print(name.upper()) #return the whole string in upper case


# In[48]:


name='Haiqa Suhail'
print(name.zfill(14)) #add zeros after the total character of string with includes spaces


# In[ ]:




