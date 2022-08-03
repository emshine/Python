# Python

## Variables:
  * Variables does not begins with number.
  * Variables are separated by underscore and they are called snake cases.ex E_fg.
  * Variables can have small letter ,capital letter as well as numbers.
## Comments:
  * '#'- For single line comment
  * ''' ''' - For multi line comment
## Dictionaries:
  Dictionaries are used to store data's in a key:value pair.Usually the data's in dictionaries are - ordered changable,no duplicates are allowed.The values in dictionary items can be of any data type.
* Example:
      ```   
         thisdict = {
                       "brand": "Ford",
                        "model": "Mustang",
                        "year": 1964,
                        "colors": ["red", "white", "blue"]
                     }
       ```
 * #### Functions used in Dictionaries:
      
          ```
              * len()-len(thisdict).Length of dictionary.
              * get()-ex: x = thisdict.get("model").
              * keys()-gives the set of all the keys. ex:x=thisdict.keys().
              * values()-gives all the values in the dictionary. ex:x=thisdictvalues().
              * thisdict["age"]=45-To update the values in the dictionary.
              * items()- method will return each item in a dictionary, as tuples in a list. ex:x=thisdict.items().
              * update()- method will update the dictionary with the items from the given argument.The argument must be a dictionary, or an iterable object with                          key:value pairs.ex:= thisdict.update({"year": 2020}).
              * The pop() method removes the item with the specified key name: ex:=thisdict.pop("model").
              * del keyword removes the item with the specified key name: del thisdict["model"].
              * clear()-method empties the dictionary: ex:=thisdict.clear().
              * popitem()-	Removes the last inserted key-value pair.
              * copy()-make a copy of dictionary.ex:-my=thisdict.copy() .
         ```
 * #### Looping :
   * ##### Print the values in the dictionaries:    
           * for x in thisdict:
            print(thisdict[x])
           * for x in thisdict.values():
            print(x)
           * for x in thisdict.keys():
            print(x)
            
## String:
   * String is enclosed in double quotes g= "hello".
## List:
  * Lists are used to store multiple items in a single variable.Lists are created using square brackets.
  * List items are ordered, changeable, and allow duplicate values.
  * List items are indexed, the first item has index [0], the second item has index [1] etc.Negative indexing means start from the end -1 refers to the last item, -2       refers to the second last item etc.
  Example:
    ```
    thislist = ["apple", 17, ["cherry",20]]
    print(thislist) 
    ```
    * To change a range of list values:
    Example:
    ``` 
     thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
     thislist[1:3]=["cherry","kiwi"]
    ```
    * Functions used in Lists:
     ``` 
      * len() - To find the length of the list.ex: len(thislist)
      * list() - It is used to convert a set or any to list.
      * insert() - It insert values to the specified location without replacing the values.ex: thislist.insert(2,"Papaya")
      * append() - To add an item to the end of the list.ex: thislist.append("shamam")
      * extend() - To append another list to the current list at the end.
         Example:
         ```
          this=["Emmanuel",21]
          address=["Kerala","India"]
          this.extend(address)
         ```
      * remove() - Remove a specified item from the list.
      * pop() - Remove the last item.If it has the index then it removes the item in that index.
      * clear() - Empties the list . ex: thislist.clear()
      * sort() - Sort the items in the list in alphanumerical,ascending order. Ex: thislist.sort()
      * sort(reverse=True) - Sort the items in descending order.
      * reverse() - Reverse the current sorting order.Ex:-thislist.reverse()
      * copy(),list() - To create the copy of the list.Ex: x=thislist.copy(),x=list(thislist)
      * index() - 	Returns the index of the first element with the specified value.
    ```   
## Tuples:
 * Tuples are used to items in a single variable.
 * Tuples are unchangeable ,allow duplicate values and ordered.
 * Examples:
    ```
    Tuple = ("Emmanuel","Addrress")
    print(Tuples)
    ```
