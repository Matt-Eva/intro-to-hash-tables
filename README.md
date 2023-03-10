# Intro to Hash Tables

Hash tables (also known as hash maps) are a commonly used data structure that appear in many programming languages and solutions to algorithmic problems. If you've started learning a programming language, you've likely already used a hash table. Data structures like dictionaries in Python, hashes in Ruby, and objects, maps, and sets in JavaScript are all implemented as hash tables.

## But What is a Hash Table?

Put simply, a hash table is a type of data structure that connects keys to values. This is different than an array, which maps indexes to values, where the index corresponds to a specific address in computer memory.

In reality, hash tables actually <em>are</em> arrays - or, rather, they use arrays under the hood. (Although some use binary search trees - more on that later.) For this reason, hash tables that use arrays under the hood are considered a type of "associative array" - basically an array that uses key value pairs.

While many programming languages have built in hash tables, we're going to explore how a hash table actually works, and practice implementing our own custom hash table.

## A Brief Aside on Computer Memory

Before we dive into that, we're going to briefly discuss how computers store values in memory.

When a computer runs a program, it has to save information about that program - variables, functions, data, etc. - in memory. In order to keep track of and access these different pieces of information, a computer assigns each piece of data it's own memory <em>address</em>.

<table>
<tr>
<th>Address</th>
<th>Name</th>
<th>Value</th>
</tr>
<tr>
<td>0</td>
<td>y</td>
<td>10</td>
</tr>
<tr>
<td>1</td>
<td>z</td>
<td>15</td>
</tr>
<tr>
<td>2</td>
<td>w</td>
<td>3</td>
</tr>
</table>

In this example, we have three different variables, their values, and the addresses at which those values are stored. When we want to access those values, the computer will reference these memory addresses in order to retrieve the value.

This is very similar to how arrays work. Arrays are basically sequential data sets that use a consecutive series of addresses to store a bunch of data. Each array index will reference a different address in memory - when we retrieve a specific element from an array, the computer will use the address associated with that index to retrieve the value we want.

What does this have to do with hash tables? Well, it has to do with a hash table's hashing function.

## The Hashing Function

As mentioned previously, hash tables are actually implemented as arrays within computer memory - that is, the computer stores the values in a hash table as index value pairs, where each index is associated with a specific address in computer memory.

Then how does the key come into the picture? Don't we use hash tables so we can use keys instead of indexes?

This is where the hashing function comes in - essentially, it's a function that takes in a key as an argument and converts that key into an index. This index is then associated with a particular "bucket" in which the value is stored.

Here's a diagram from the wikipedia article on hash tables that illustrates this concept:

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Hash_table_3_1_1_0_1_0_0_SP.svg/315px-Hash_table_3_1_1_0_1_0_0_SP.svg.png"/>

We create keys we want to use and pass them through the hashing function, which translates them into indexes.

On average, the time complexity for access a value stored within a hash table is O(1) - constant time. This efficiency for lookup is one reason hash tables are so widely used, and why so many programming languages have built in hash tables (not to mention it's an easy data structure to work with conceptually).

However, the worst case time complexity for lookup is actually O(n) - linear time. This has to do with <em>collisions</em>.

## Hash Table Collisions

As mentioned above (and shown in the above diagram from Wikipedia), values associated with hash keys are stored in individual "buckets", which are paired with the index that corresponds to that hash key. However, these "buckets" can actually store multiple values - this occurs when two different hash keys are mapped to the same index after having run through the hashing function. This type of phenomenon is known as a "collision", and it's best to avoid it when possible. Often, however, it's inevitable.

### Managing Collisions

Collisions are a common symptom of using hash tables, and two main techniques have been developed to ensure that keys mapped to the same index are still able to store their values in a hash table. 

#### Separate Chaining

Separate chaining involves storing different key-value pairs that have been mapped to the same bucket as individual nodes in a linked list. (For more on linked lists, see our linked-list lesson!) Each node in the linked list stores both the original key and the value associated with that key. Our search algorithm will iterate over the linked list until it finds the matching key - then it will return the value. This diagram from wikipedia visually illustrates this concept:

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Hash_table_5_0_1_1_1_1_1_LL.svg/450px-Hash_table_5_0_1_1_1_1_1_LL.svg.png"/>

#### Open Addressing

Open addressing is another common solution to handling collisions. Rather than storing multiple values within the same bucket, if a key is mapped to an index that already has an existing key, the hashing function will use a probing algorithm to check other indexes within the array. Once it finds an available index, it will store the key and value in the bucket associated with that index. Note that the search algorithm follows this same sequence - however many steps it took to insert the new key-value pair, that's how many steps it will take to retrieve it. This diagram from wikipedia visually illustrates this concept:

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Hash_table_5_0_1_1_1_1_0_SP.svg/380px-Hash_table_5_0_1_1_1_1_0_SP.svg.png"/>

Collisions are the reason hash tables have an O(n) worst case time complexity. If all keys are mapped to the same index and all values are stored in the same bucket, then our search algorithm will have to simply iterate through every value stored in that bucket before it can find the correct value - an O(n) operation. 

### Load Factor

Part of determining a hash table's performance involves a metric call a "load factor". Basically, a load factor represents the relationship between the number of key value pairs stored within a hash table and the number of buckets available in that hash table.

`load factor = n / k`

where `n` represents the number of key value pairs in the hash table and `k` represents the number of buckets available in the hash table.

As the value of the load factor approaches 1 - at which point the hash table would have the same number of values stored as entries available - the performance of the hash table worsens. Why? Well, because collisions start to become more likely. The fewer available entries, the more likely it is that your hashing function will map two different keys to the same index.

Many hash table implementations have a <em>rehashing</em> feature built into them, where a hash table will increase the number of buckets it has when the load factor approaches 1. Note that rehashing itself can be a resource-intensive operation, as the computer has to reallocate memory for the newly sized hash table.

## Performance Implications

Hash tables can be an extremely handy data structure to use to organize data and solve algorthmic problems, in part because of the way the information is organized, and in part due to their quick lookup operations. 

Oftentimes, accessing a key within a hash table will be referred to as having an O(1) time complexity. That's ideal for a hash table, and hash tables do routinely achieve that level of performance, but it's important to know that the under-the-hood mechanics aren't quite that simple. 

It's also important to consider whether or not your hash table will be dynamically resized at runtime, in which case your computer could end up having to reallocate memory for that hash table a number of times, which could drastically impact the overall performance of your program. 

Higher level languages - Python, Ruby, JavaScript - don't give you much control over this, although it's still something to take into consideration, while lower level lanugages - Rust, Go, C++ - do.

It's important to note that not all hash tables use an array as the underlying data structure - some use Binary Search Trees. This changes the time complexity of looking up values within a hash table, from an average of O(1) and a worst case to O(n), to an average of O(log n) and a worst case of O(log n). One version - array as underlying structure - offers a chance at improved performance, but an overall worst case time complexity. The other - Binary Search Tree as underlying structure - offers a more consistent performance with a lower peak performance.

## Using Hash Tables

As mentioned before, most languages have built in hash tables:

- JavaScript - all `objects` in JavaScript are implemented as hash tables.
- Ruby - ruby `hashes` are ruby's implementation of a hash table
- Python - python `dictionaries` are python's implementation of a hash table
- Java - Java has `HashSets`s, `HashMap`s, `LinkedHashSet`s, and `LinkedHashMap`s
- Go - Go has a `map` data type, which is implemented as a hash table
- C++ - includes the `unordered_map`
- Rust - includes `HashMap` and `HashSet` as part of it's standard library

Due to the wide inclusion of hash tables (also known as hash maps, as previously mentioned) in major programming languages, you'll often be able to leverage the functionality of a hash map without having to implement your own custom solution. Just get familiar with your language of choice's hash table, and read up on how that language uses and implements it.

## Custom Hash Table Implementation

That being said, we're programmers, and we want to understand how things work and build things ourselves! For that reason, we're going to build out our own custom hashing function using Python. 

This custom hashing function has been adapted from Adrian Mejia's custom hashing function he built using JavaScript. To read more about HashMaps and other data structures in JavaScript, please check out his <a href="https://adrianmejia.com/data-structures-time-complexity-for-beginners-arrays-hashmaps-linked-lists-stacks-queues-tutorial/#HashMaps">awesome website</a>, where he includes tutorials on a wide variety of topics.

Note that the hashing functions that programming languages use will likely be more sophisticated that the one present here. Hashing data is part of a field of science called <a href="https://en.wikipedia.org/wiki/Cryptography"><em>cryptography</em></a>, which is the science of encoding information. 

Cryptography is a fascinating field, and you should definitely research more of it if you're interested, but it falls outside of the scope of this lesson.

### Setting up our Classes

We're going to be building our custom Hash Tables in both Python and Ruby. The hash table we'll be building will have an array as its underlying data structure, and will use separate chaining to handle collisions. To set this up, we're going to need 3 classes:

Python:
```
class Node:

class LinkedList:

class HashTable:
```

Our `HashTable` class is what we'll use to create a new HashTable. We'll use the `LinkedList` class to set up LinkedLists that correspond to each index in the array that implements our HashTable. Finally, we'll use the `Node` class to implement our LinkedList. A singly Linked List will work fine for our purposes.

### Initializing instances of our classes

Now that we have our classes created, let's create initialize methods so that we can actually start creating instances using our classes:

Python:
```
class Node:
  
  def __init__(self, key, val):
      self.key = key
      self.val = val
      self.next_node = None

class LinkedList:

    def __init__(self):
      self.head = None


class HashTable:

    def __init__(self, size):
        self.buckets = [LinkedList()] * size
        self.capacity = size
```

Let's break down why we wrote each initialize function in this manner:

#### HashTable Init
- When creating our hash table, we want to start it off with a certain number of `buckets` that we can use to store key value pairs. So, we set our buckets to an array of a starting size.
- One `bucket` - which corresponds with one index in our array - will store a LinkedList, which we can use to store multiple key value pairs if we end up getting any collisions.

#### LinkedList Init
- When creating a new LinkedList, we don't initially store any nodes within it. So, we can just set the `head` to `None` for the time being.

#### Node Init
- A Node is going to be a single entry within our Linked List. In other words, our Linked List is going to be a series of Nodes connected to one another.
- We want each Node in our Linked List to store information about a specific key and value that we've put in our Hash Table. So, we give it a field to store a key and a field to store a value. We also allow the `init` function to receive the new key and value as arguments.
- Nodes in a Singly Linked List are connected by a `next_node` field in each Node. The `next_node` field points the the next node in the Linked List (for more on this, refer to our Linked List lesson). When a new node is created, it's added to the end of the Linked List, which means that its `next_node` field will be `null`. Hence, we start that field off with a default value of `null`. Once a new Node is added to the Linked List, this field will be updated to point to the new node.

### Aside: Why Linked Lists instead of Arrays

You may be wondering - why would we use Linked Lists to implement Open Addressing instead of using Arrays?

Well, once again, it has to do with the way a computer allocates memory. Arrays (or "lists" in Python) are data structures whose individual pieces of data <em>must</em> be stored in sequential order. If we remember our diagram of memory addresses from earlier, this implies that any element within an array must be stored in this fashion:

<table>
<tr>
<th>Address</th>
<th>Name</th>
<th>Value</th>
</tr>
<tr>
<td>0</td>
<td>First array element</td>
<td>10</td>
</tr>
<tr>
<td>2</td>
<td>Second array element</td>
<td>15</td>
</tr>
<tr>
<td>3</td>
<td>Third array element</td>
<td>3</td>
</tr>
<tr>
<td><em>More addresses</em></td>
<td><em>More elements of our array</em></td>
<td><em>More values associated with elements in our array</em></td>
</tr>
<tr>
<td>8</td>
<td>Final array element</td>
<td>15</td>
</tr>
</table>

All array elements must be stored <em>sequentially</em> in memory. 

Because of this, if an array increases in size, the computer may have to reallocate memory for an entirely new array. (If, for instance, the memory address following the final array element already had a value associated with it).

This can be an expensive and inefficient operation, especially if you have a hash table with the potential for a lot of collisions.

<strong>Linked Lists</strong>, on the other hand, <em>do not</em> have to store nodes in sequential order. The implementation of a Linked List would look more like this:

<table>
<tr>
<th>Address</th>
<th>Name</th>
<th>Value</th>
</tr>
<tr>
<td>0</td>
<td>1st Node of Linked List</td>
<td>10</td>
</tr>
<tr>
<td>1</td>
<td>Some other variable</td>
<td>15</td>
</tr>
<tr>
<td>2</td>
<td>Yet another variable</td>
<td>3</td>
</tr>
<tr>
<td>3</td>
<td>2nd Node of Linked List</td>
<td>8</td>
</tr>
 <tr>
<td>4</td>
<td>1st Element of an Array that begins at this address</td>
<td>8</td>
</tr>
<tr>
<td>...</td>
<td>...</td>
<td>...</td>
</tr>
<tr>
<td>8</td>
<td>3rd Node of Linked List</td>
<td>15</td>
</tr>
</table>

Basically, individual nodes of a Linked List can be stored at any address in memory. They don't have to be directly adjacent to other nodes in the Linked List. 

Because of this, when we add a new Node to our list, our computer only needs to allocate memory for that new entry. This is much more efficient that having to reallocate memory for an entire array.

### Building our Hashing Function

Ideally, our hashing function will be able to take a variety of keys and consistently generate unique numberical values based on those keys.

We could create a very simple hashing function like this:

Python:
```
def simple_hash(self, key):
  return len(key)
```

But this would produce the same number for all words that have the same number of letters - `cat`, `bat`, `dog`, and `eat` would all produce the same value, which means each of these keys would be mapped to the same bucket. That's a lot of collisions!

Instead, let's come up with a better hash. This hash will still likely produce collisions, but there will be far fewer of them.

Python
```
def better_hash(self, key):
  hash_val = 0
  key_len = len(key)
  i = 0
  while i < key_len:
      char_val = ord(key[i])
      hash_val += (char_val + i) **2
      i+=1
  return hash_val
```

Let's break down what's going on here.


- First, we're creating variable `hash_val` which will ultimately reference the hashed value of our key that we want our `better_hash` method to produce. We'll start it off at `0`, since we're going to be adding values to it.
- Next, we're going to be creating a variable that represents the number of characters within the key we want to hash - `key_len`. This isn't strictly necessary, but it's often helpful to break down your code into individual steps, especially when you're first drafting new code
- After that, we're creating a variable, `i`, which we'll be using to run our while loop. `i` will also represent an index within our key. (Remember, strings in Python have indexes!)
- Now, we're ready to start looping through each character in our key and generate a unique number value based on each character
- First, we get the <a href="https://en.wikipedia.org/wiki/Unicode">unicode character value</a> of the character at a specific index in our key: `char_val = ord(key[i])`
  - Each character will give us a unique number, which means we'll be generating unique values for every character in our key!
  - Our goal is to sum up all of the unique character values within our key to generate our unique hash value.
  - However, as you may have already realized, this will cause some problems - what about keys that have the exact same letters, like `teach` and `cheat`? Since they have the same letters, adding the unique character codes together will result in the same final value. We don't want that! That's a guaranteed collision!
- To account for this issue, we incorporate the <em>index</em> into the value we add to our `hash_val`.
  - Because `teach` and `cheat` have have characters in a different order, we can use the index of each character to generate different values for the entire word.
  - For example, in our code we've written `hash_val += (char_val + i)**2` - this means that we're increasing the value of our `hash_val` variable by the current character value, plus the index value, squared.
    - If we look at the value that `e` generates in `teach`, we'll get `101` (the unicode value of the character `e`), multiplied by `1` (the index of `e` in the word `teach`), squared. Which all in all results in `(101 + 1) **2 = 10404`.
    - Now, if we look at the value that `e` generates in `cheat` we see that it will generate a <em>different value</em> because it has a <em>different index value</em> in the word cheat.
    - `(101 + 2)**2 = 10609`.
    
We now have a decent solution for generating unique values based on any given key. We will still likely experience collisions on our hash table, but ensuring that each key has a unique hash value will help minimize the number of collisions our hash table generates.

### Getting the Index from the Hash

As you may have noticed, the hash values we'll be generating for each key will be fairly large numbers. (The value generated for `e` in `teach` was <em>over 10000!</em>)

These numbers probably won't immediately correspond to a specific index within the array we've set up to implement our hash table. (Unless we have an array with tens of thousands of entries, which is unlikely).

So, we're going to build another method - `get_index`, which will enable us to translate the value of our hashed key to an index value:

Python:
```
get_index(self, key):
  hash_val = self.better_hash(key)
  index = hash_val % self.capacity
  return index
```

Let's break down how this is working:

- First, we're using our `better_hash` method we just built to generate a unique hash value for our key. We save that hash value in our `hash_val` variable.
- Next, to translate that `hash_val` to a valid index in our array, we're using the modulus operator - `%` - along with the capacity of our hash table.
  - If we remember from out `__init__` method we set up earlier, `self.capacity` is keeping track of the number of elements in our array.
  - The modulus operator - `%` - is used to get the remainder of a division of two numbers.
    - For example, if we were to run `10 % 5`, we would receive `0`: `10 % 5 = 0`.
      - We receive `0` because `5` fits into `10` exactly two times. So there is no remainder of this division
    - However, if we were to run `11 % 5`, we would recieve `1`: `11 % 5 = 1`.
      - Essentially, `5` fits into `11` two times, but it's not a <em>perfect</em> fit. `5` times `2` is `10`. So, we have `1` <em>left over</em> when we try to divide `11` by `5`. The modulus operator calculates that <em>remainder</em> for us.
  - The modulus operator is really helpful in this context, because it allows us to get the remainder when we divide our `hash_val` by the size of our array. 
    - This remainder is <em>guaranteed</em> to correspond with an index in our array - the remainder generated cannot be greater than or equal to the capacity itself. (Take some time to consider why this might be.)
    - Moreover, if the capacity of our array is somehow <strong>larger</strong> than our `hash_val`, the modulus operator will just return the `hash_val`.
    - Ex: `20 % 100 = 20`.
- Finally, we return the index value generated by using the modulus operator.

We've now managed to take a key and translate the value of that key to an index value in our array! Success!

Our `HashTable` class should now look like this:

Python
```
class HashTable:

    def __init__(self, size):
        self.buckets = [LinkedList()] * size
        self.capacity = len(self.buckets)
        
    def better_hash(self, key):
        hash_val = 0
        key_len = len(key)
        i = 0
        while i < key_len:
            char_val = ord(key[i])
            hash_val += (char_val + i)**2
            i+=1
        return hash_val

    def get_index(self, key):
        hash_val = self.better_hash(key)
        index = hash_val % self.capacity
        return index
```
  


