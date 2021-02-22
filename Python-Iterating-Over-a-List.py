mylines = []                              # Declare an empty list
with open ('lorem.txt', 'rt') as myfile:  # Open lorem.txt for reading text.
    for line in myfile:                   # For each line of text,
        mylines.append(line)              # add that line to the list.
    for element in mylines:               # For each element in the list,
        print(element)                    # print it.
        
        
 ### Iterating over Beautiful Soup methods
 
# .next_elements and .previous_elements
# You should get the idea by now. You can use these iterators to move forward or backward in the document as it was parsed:

for element in last_a_tag.next_elements:
    print(repr(element))
# 'Tillie'
# ';\nand they lived at the bottom of a well.'
# '\n'
# <p class="story">...</p>
# '...'
# '\n'


if(True): requests.get(...) else: requests.posts(...) 
if(True) else requests.post()

## Refactored shorthand version...

# esoteric solution:
getattr(requests, ("get", "post")[True])(...)

If you just want to remove the repetition:
(requests.get if True else requests.post)(...)

# of if you have the same arguments.
requests.request("get" if True else "post", ...)