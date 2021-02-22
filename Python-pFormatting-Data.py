#---------------------------------------------------------------------------------------
# Formatting
# If you need to format a data structure, but do not want to write it directly
# to a stream (for logging purposes, for example) you can use pformat()
# to build a string representation that can then be passed to another function.
#---------------------------------------------------------------------------------------
import logging
from pprint import pformat
from pprint_data import data

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)-8s %(message)s',
                    )

logging.debug('Logging pformatted data')
logging.debug(pformat(data))


# run python pprint_pformat.py (filename)
# outputs:
# DEBUG    Logging pformatted data
# DEBUG    [(0,
  # {'a': 'A',
   # 'b': 'B',
   # 'c': 'C',
   # 'd': 'D',
   # 'e': 'E',
   # 'f': 'F',
   # 'g': 'G',
   # 'h': 'H'}),
 # (1,
  # {'a': 'A',
   # 'b': 'B',
   # 'c': 'C',
   # 'd': 'D',
   # 'e': 'E',
   # 'f': 'F',
   # 'g': 'G',
   # 'h': 'H'}),
 # (2,
  # {'a': 'A',
   # 'b': 'B',
   # 'c': 'C',
   # 'd': 'D',
   # 'e': 'E',
   # 'f': 'F',
   # 'g': 'G',
   # 'h': 'H'})]

#------------------------------------------------------------------------------
#-- Recursion 
#-- Recursive data structures are represented with a reference to the original
#-- source of the data... with the form <Recursion on typename with id=number>
#------------------------------------------------------------------------------



# from pprint import pprint

# local_data = [ 'a', 'b', 1, 2 ]
# local_data.append(local_data)

# print 'id(local_data) =>', id(local_data)
# pprint(local_data)

# outputs:
# id(local_data) => 4299545560
# ['a', 'b', 1, 2, <Recursion on list with id=4299545560>]