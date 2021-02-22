#-------------------------------------------------
#-- Populating dictionary using for-loop
#-------------------------------------------------

# creates empty dictionary dict = { }
# creates key range: key = range(4)
# creates values: values [ ]
dicts = {}
keys = range(4)
values = ["Hi", "I", "am", "John"]

for i in keys:                          # iterating with standard for-loop
    dicts[i] = values[i]                # concatenates name-value pair

print(dicts)

{ 0: 'Hi', 1: 'I', 2: 'am', 3: 'John' }


## Alternatively...

>>> dict(list(enumerate(values))
{ 0: 'Hi', 1: 'I', 2: 'am', 3: 'John' }

## Alternately...
>>> dict(zip(keys, values))
{ 0: 'Hi', 1: 'I', 2: 'am', 3: 'John' }

#--------------------------------------------------------
#-- Add new items to a dictionary in a loop
#--------------------------------------------------------

word_freq = {"Hello " : 24, "Wonderful": 48, "World": 96}
new_keys = ['how', 'why', 'what', 'where']

i = 1
for key in new_keys:
    # 1) takes key -> 2) puts it into word_freq dict -> 3) with a corresponding value pair
    ## Computes both i) name and ii) generated value
    word_freq[key] = i
    i += 1

print(word_freq)
{'Hello' : 24,
 'Wonderful': 48,
 'World': 96
 'how': 1,
 'why': 2,
 'what': 3,
 'where': 4}

#----------------------------------------------------------
#-- Add a 'list' as a value to a dictionary in Python
#----------------------------------------------------------

word_freq = {"Hello " : 24, "Wonderful": 48, "World": 96}

word_freq.update( {'why': [1,2,3]} )
print(word_freq)
#{"Hello " : 24, "Wonderful": 48, "World": 9, 'why': [1, 2, 3]}

word_freq['what'] = [1, 2, 3]
print(word_freq)
#{"Hello " : 24, "Wonderful": 48, "World": 9, 'what': [1, 2, 3]}


#----------------------------------------------------------------------
#-- Find the MAX VALUE(with the key) in a Dictionary... key associated with max value
#-----------------------------------------------------------------------

myDictionary = {"bird": 1, "cat": 2, "dog": 3, "cow": 4, "lion": 5}

maxKey = max(myDictionary, key=mmyDictionary.get)
print(maxKey)
''' >>> lion '''


#------------------------------------------------------------------------
#-- Find the MAX VALUE in a DICTIONARY
#------------------------------------------------------------------------
myDictionary = {"bird": 1, "cat": 2, "dog": 3, "cow": 4, "lion": 5}
allValues = myDictionary.values()
maxValue = max(allValues)
print(maxValue)
''' >>> 5 '''

#---------------------------------------------------------------------
#-- Collections: Enumeration
#---------------------------------------------------------------------
x = ('Cat', 'Dog', 'Rabbit', 'Velociraptor' )
for i, v in enumerate(x):
    print(f'{i}: {v}')
''' 
Outputs:
0: Cat
1: Dog
2: Rabbit
3: Velociraptor
'''


#---------------------------------------------------------------------------
#-- Collections: Reversed List
#---------------------------------------------------------------------------
x = (1,2,3,4,5)
y = list(reversed(x)
print(x)    # print original
print(y)    # prints reveresed list
''' Outputs:
(1,2,3,4,5)
[5,4,3,2,1]
'''
x = (1,2,3,4,5)
y = reversed(x)
for i in y: 
    print (i)   # prints i separately 
print(x)    # print original
print(y)    # prints reveresed list
''' Outputs: 
5
4
3
2
1
'''

#---------------------------------------------------------------------------
### ZIP FUCNTION
#---------------------------------------------------------------------------
z = zip( x,y )
for a, b in z:
    print(f'{a} - {b}')
''' Outputs: 0 - A , 1 - B , 2 - C , 3 - D'''

#---------------------------------------------------------------------------
### isinstance
#---------------------------------------------------------------------------
x = 42.0
y = isinstance(x, int)
print(x)
print(y)
    ''' Outputs:
    42.0
    False
    '''

#---------------------------------------------------------------------------
### id
#---------------------------------------------------------------------------
x = 42.0
y = id(x)
print(x)
print(y)
    ''' Outputs:
    42.0
    4302377296
    '''


# AMEND MULTIPLE KEY VALUE PAIR IN DICTIONARY

#---------------------------------------------------------------
#-- Adding a list of tuples (key-value pairs) in the dictionary
#---------------------------------------------------------------

# Dictionary of strings and ints
word_freq = {"Hello": 56, "at": 23, "test": 43, "this": 43}

# List of 4 Tuples
new_pairs = [ ('where', 4), ('who',5), ('why',6), ('before', 7) ] 

word_freq.update(new_pairs)
print(word_freq)

{'Hello': 56,
 'at': 23,
 'test': 43,
 'this': 43,
 'where': 4,
 'who': 5,
 'why': 6,
 'before': 7}


#-------------------------------------------------------------------
#-- Add a dictionary to another dictionary
#-------------------------------------------------------------------

# Two dictionaries
dict1 = {
    "Hello": 56,
    "at": 23,
    "test": 43,
    "this": 43
}

dict2 = {'where': 4,
         'who': 5,
         'why': 6,
         'this': 20
         }
         
# Adding elements from dict2 to dict1
dict1.update( dict2 )
print(dict1)

{'Hello': 56,
 'at': 23,
 'test': 43,
 'this': 20,
 'where': 4,
 'who': 5,
 'why': 6}
















####################
## NLP-WebScrap.py | looping through a loop, populating key-value pair
####################

  for i in self.named_entities:
            print("Named Entity: ", i, "\n")
            
            # checks if key's element existence in dict or not
            if not i in self.ne_dict.keys():
                # then, key exists in dict
                self.ne_dict[i] = 1
                
                # append value in list
                # self.ne_dict[i].append(value)
                # self.ne_dict[i] = self.named_entities.count(i)  # add frequency
                # self.ne_dict[i] = 1
                
                # check if type of value of key is list or not
                # if not insinstance(self.ne_dict[i], list):
                    # if type isn't list, then make it list
                #     # self.ne_dict[i] = [self.ne_dict[i]]
                
           
            else:
                # as key isn't in dict
                # adds in key-value pair
                self.ne_dict[i] = self.frequency[i] + 1     # adds frequency
            
        print(">>> Dictionary of Named Entities and Frequency: \n", self.ne_dict, "\n")
            
            
            # self.ne_dict[self.ne_value] = self.named_entities.count(i)
            
            # checks for existence of a key in dictionary
            # if self.ne_value in self.ne_dict:
            #     print("Key exists")
            #     self.ne_dict[i] = self.ne_dict[i] + 1
            
            # else:
            #     print("Key doesn't exist")
            #     self.ne_dict[i] = 1

            # print(" Word: ", self.ne_value, " | ", "Count: ", self.named_entities.count(i), "\n")
        
        # prints the dictionary with stored named entities and frequencies 
        # print(">>> Dictionary of Named Entities : \n", self.dict_ne_freq, "\n")

    
    #-- Counts up the Frequency Distribution based on Named Entities
    ''' def count_entity_frequency(self):

        # count = self.count_ne

        print(">>> Frequency Distribution of Named Entities: \n")
        
        for ne in self.named_entities:
            # print("Named Entity: ", ne)
            
            # checks if key's element existence in dict or not
            if not ne in self.ne_dict.keys():
                
                # then, add one as a value to current dictionary's key element
                self.ne_dict[ne] = 1
                
                    # storing first value from tuples as dict key
                    # self.ne_dict[ne[0]] = (ne[1], self.ne_dict + 1)
             
            else:
                # key is in dict, increment frequency in key-value pair
                self.ne_dict[ne] = self.ne_dict[ne] + 1
       
        print("\n>>> Dictionary of Named Entities' Frequency: \n", self.ne_dict, "\n")
    '''
    ''' Returns the top 5 most frequent entities from the NEs dictionary '''
    # def get_top_frequent_entities(self):
    #     # note - items getting popped out - no longer in the original dict
    #     self.frequent_entities = []
    #     for _ in range(6):
    #         print(_)
    #         item = max(self.ne_freq_dict, key=self.ne_freq_dict.get)
    #         self.ne_freq_dict.pop(item)
    #         self.frequent_entities.append(item)
    #     print("\n>>> Computes the 6 Most Common entity by pop/append approach: \n{}".format(self.frequent_entities))
        
            
            
            
            
            
