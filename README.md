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
                     
                     
          newdict = {
                      ("name":"Emmanuel","age":21),
                      ("name":"Kiran","age":21)
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
              *dict()- Convert the set or list to dictionary.ex: x=dict(hai)
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
 * Tuple items can be of any data type.
 * We can access items in the tuples by using the index.
    ```
    Tuples = ("Emmanuel","Address")
    print(Tuples[1])
    ```
  * #### Add items:
    * Since tuples is unchangeable it is possible to add the items by converting the tuples into list and then back to tuples.
      ```
      h = list(Tuples)
      h.append(23)
      Tuples = tuples(h)
      ```
     * Same method is used to remove a tuples by using remove() keyword.ex: h.remove("Emmanuel")
     * We can add an item into the tuple by adding a tuple into it. F
        ```
         Tuples = ("Emmanuel","Address")
         y= ("Orange",)
         Tuples+=y
        ```
  * Tuple items can be of any data type.
     ```
      fruits = ("apple", "banana", "cherry")
      (green, yellow, red) = fruits
      print(green)
      print(yellow)
      print(red*)
     
      -----
      Output:
      apple
      banana
      ['cherry', 'strawberry', 'raspberry']
        ```
  * To join two tuples.
     ```
      tuple1 = ("a", "b" , "c")
      tuple2 = (1, 2, 3)
      tuple3 = tuple1 + tuple2
      print(tuple3)
     ```
  * #### Functions:
    * count():Returns the number of times a specified value occurs in a tuple.
    * len() : Returns the length of the tuples.
    * isinstance: It mostly occur in if statement.
      ```
       def add(car,Car):
        raise Type Error(f"If Error occur with the {car,Car} if car is not taking object from Car")
       
       car = Car['Ford','Maruthi']
       add(car)
      ```
## Errors:
 *  Name Error: Name error occur when you try to reference some variable which hasnt been defined in the code.
 *  Index Error: It is raised when a sequence is raised which is out of order.
 * Key Error: It is raised when we attempt to access a key that isn't used.
 * Type Error: It is raised when an operation or function is applied to an object of inappropriate type.
 * Value Error:It is raised when a built in operation or function receives an argument that has the right type but an invalid value.
  ```
   for i in range 20.5:
  ```
 *  Attribute Error:Raised whe we try to access an attribute that is not possessed by that object.
   ```
    F = ['R','J']
    S = ['K','I']
    F.intersection(s) ## Which is not possible because intersection is only possible for set.
   ```
 * Indentation Error : Occurs when their is insufficient spce between the lines.
 
## Object Oriented Programming:
 ## Class:
  * It is an abstration of some entities which contain common object and methods.
  * Object : Specific instantsce of a class.They have similar behaviour but actual values are different.
  *  (self) : Refers to the object that is currently modifying.
  #### Magic Methods or Dunder Methods:
  A method that is wrapped by two underscores on both sides is called Magic Methods. The motive behind the magic method is to overload Python’s built-in methods and its operators. Here, _syntax prevents the programmers from defining the same name for custom methods. Each magic method serves its purpose.
   They are __init__ ,__getitem__,___len__,__repr__,__str__,__eq__
  * __init__ : The __init__ method of an object executes right away after the instance creation. Here, the method takes one positional argument – self – and any number of optional or keyword arguments. 
  * __str__ : The __str__ method requires one positional argument – self – and it returns a string. It is called when an object is passed to the str() constructor. Le

#### Refer the [Github page:](https://github.com/emshine/Python/blob/main/Basic/Classes).
