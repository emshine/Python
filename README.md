# Python

## Dictionaries:
  Dictionaries are used to store data's in a key:value pair.Usually the data's in dictionaries are - ordered changable,no duplicates are allowed.The values in dictionary items can be of any data type.
  Example:
          thisdict = {
                       "brand": "Ford",
                        "model": "Mustang",
                        "year": 1964,
                        "colors": ["red", "white", "blue"]
                     }
  * Functions used in Dictionries:
      Length of dictionary:
          ```Python
              len()-len(thisdict).
              get()-ex: x = thisdict.get("model").
              keys()-gives the set of all the keys. ex:x=thisdict.keys().
              values()-gives all the values in the dictionary. ex:x=thisdictvalues().
              thisdict["age"]=45-To update the values in the dictionary.
              items()- method will return each item in a dictionary, as tuples in a list. ex:x=thisdict.items().
              update()- method will update the dictionary with the items from the given argument.The argument must be a dictionary, or an iterable object with                          key:value pairs.ex:= thisdict.update({"year": 2020}).
              The pop() method removes the item with the specified key name: ex:=thisdict.pop("model").
              del keyword removes the item with the specified key name: del thisdict["model"].
              clear()-method empties the dictionary: ex:=thisdict.clear().
              popitem()-	Removes the last inserted key-value pair.
              copy()-make a copy of dictionary.ex:-my=thisdict.copy() .
         ```
    * Looping :
          Print the values in the dictionaries:    
          for x in thisdict:
            print(thisdict[x])
          for x in thisdict.values():
            print(x)
          for x in thisdict.keys():
            print(x)
          
    
