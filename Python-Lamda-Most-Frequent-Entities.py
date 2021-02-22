d = {
  "a": 4,
  "b": 1,
  "c": 0,
  "d": 9,
  "e": 12,
  "f": 3,
}

### Sort the key in reverse other, retrieving the first 3....
print(sorted(d.items(), key=lambda t: t[1], reverse=True)[:3])
[('e', 12), ('d', 9), ('a', 4)]

# not really, that list is just not finished yet
# All you need to do is extract the key into a new list, which can be done with a simple listcomp:

### Displays name of the key 
[t[0] for t in sorted_kvs]
[k for k, _ in sorted_kvs]
[*map(itemgetter(0), sorted_kvs)] # using operator.itemgetter

# well that last one is just the real fancy solution; 
# second one unpacks the tuple values directly into k and _ (to signalize it's unused), 
# first one gets the entire tuple into variable t


# itemgetter is effectively just
def itemgetter(idx):
    return lambda seq: seq[idx]
    
# So it would be the same as...
[*map(lambda seq: seq[0], sorted_kvs)]
# or
[(lambda seq: seq[0])(t) for t in sorted_kvs]
# or
[t[0] for t in sorted_kvs]
, all boils down to the same stuff

# I'm guessing you were wondering about the *?
# That's the splat operator, which has a few special meanings in different places;
# in this case when placed in front of an iterable (which map is) inside a comprehension (which this is)
# It will drag out everything this map object produces into the list; if you left it out 
# you'd end up with a single-element list containing a map object

### Display integer values from dictionary...
[t[1] for t in sorted_kvs]
[_ for _ in sorted_kvs]
[*map(itemgetter(1), sorted_kvs)] # using operator.itemgetter


def get_top_frequent_elements(freq_list: list) -> list:
    freq_list = sorted(dict.items(), key=lambda t: t[1], reverse=True)[:6])
    return freq_list



