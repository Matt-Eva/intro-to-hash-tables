# Intro to Hash Tables

Hash tables (also known as hash maps) are a commonly used data structure that appear in many programming languages and are widely used throughout the programming world. They offer a useful, approachable format for structuring data and often boast quick lookup times, which make them ideal for certain types of algorithmic problems. 

If you've started learning a programming language, you've likely already used a hash table. Data structures like dictionaries and sets in Python, hashes in Ruby, and objects, maps, and sets in JavaScript are all implemented as hash tables.

## But What is a Hash Table?

Put simply, a hash table is a type of data structure that pairs keys with values. 

Example of a dictionary in Python:

```
my_dict = {
  "key": "value"
}
```

You can think of hash tables as a filing cabinet (or, well, a dictionary, as the Python developers did). Each cabinet has a label on it, which corresponds to our "key". The files inside the drawer correspond with our "value". When we want to access a set of files from the cabinet, we use the label to look up the appropriate drawer that contains our files.

Or, to use Python's dictionary analogy, each word in our dictionary correlates with a "key" in our hash table. The definition associated with each word correlates with the "value" in our hash table. When we want to look up a certain definition, we locate the word we're looking up in our dictionary, then read the definition.

This is exactly how computers operate as well! Once we've added a key-value pair to our dictionary, we can pass the key to our program, and it will find the value associated with that key.

This is a very easy and convenient way to structure data. It gives us, as programmers, a more flexible way of organizing information than arrays, which use index-value pairings.

Arrays and hash tables are very similar data structures, but they have a couple of important differences, which we'll explore in this reading. As a high level overview, we can think of arrays as <em>ordered, sequential</em> data structures with <em>index-value</em> pairings, and hash tables as <em>unordered</em> data structures with <em>key-value</em> pairings.

In reality, hash tables actually <em>are</em> arrays - or, rather, they use arrays under the hood. (Although some use binary search trees - more on that later.) For this reason, hash tables that use arrays under the hood are considered a type of "associative array" - basically an array that uses key value pairs.

But enough introduction! Let's get into it!

## A Brief Aside on Computer Memory

Hmm, actually, we have a little more introduction to do. Before we dive into the inner workings of hash tables themselves, we need to briefly discuss how computers store values in memory.

When a computer runs a program, it has to save information about that program - variables, functions, data, etc. - in memory. In order to keep track of and access these different pieces of information, a computer assigns each piece of data its own memory <em>address</em>.

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

When we store a value in a hash table, we're actually storing it at a specific index in an array that corresponds to a specific address in computer memory. 

But how do we get from a key to an index? Well, it has to do with a hash table's hashing function.

## The Hashing Function

What is a "hashing function"?

Essentially, it's a function that takes in a key as an argument and converts that key into an index in the  array that underlies the hash table. This array contains a series of "buckets" - one "bucket" for each index in our array. 

These "buckets" contain the key-value pairs we're entering in our hash table. (So, a key is both converted into an index via our hashing function <em>and</em> stored in a bucket in our array.) 

We call them "buckets" because they can - and often do - hold <em>multiple key value pairs</em>. 

In reality, this array just works the way any normal array would - it has a series of indexes and a series of values associated with each index. "Bucket" is just a term that's often used when discussing hash tables.

Here's a diagram from the Wikipedia article on hash tables that illustrates this concept:

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Hash_table_3_1_1_0_1_0_0_SP.svg/315px-Hash_table_3_1_1_0_1_0_0_SP.svg.png"/>

We create keys we want to use and pass them through the hashing function, which translates them into indexes. Each index corresponds with a bucket, in which we store the key-value pair were entering.

On average, the time complexity to access a value stored within a hash table is O(1) - constant time - which is the same time complexity for accessing a value within an array using an index. (Because that's <em>exactly</em> what we're doing.) This efficiency for lookup is one reason hash tables are so widely used, and why so many programming languages have built in hash tables.

However, the worst case time complexity for lookup is actually O(n) - linear time. This has to do with <em>collisions</em>.

## Hash Table Collisions

As mentioned above (and shown in the above diagram from Wikipedia), key-value pairs are stored in individual "buckets", which are paired with the index that corresponds to the key. As mentioned, these "buckets" can actually store multiple values - this occurs when two different keys are mapped to the same index after having run through the hashing function. This type of phenomenon is known as a "collision", and it's best to avoid it when possible. Often, however, it's inevitable.

### Managing Collisions

Collisions are a common symptom of using hash tables, and two main techniques have been developed to ensure that keys mapped to the same index are still able to store their values in a hash table. 

#### Separate Chaining

Separate chaining involves storing different key-value pairs that have been mapped to the same bucket as individual nodes in a linked list. (For more on linked lists, see our linked-list lesson!) Each node in the linked list stores both the original key and the value associated with that key. Our search algorithm will iterate over the linked list until it finds the matching key - then it will return the value. This diagram from wikipedia visually illustrates this concept:

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Hash_table_5_0_1_1_1_1_1_LL.svg/450px-Hash_table_5_0_1_1_1_1_1_LL.svg.png"/>

#### Open Addressing

Open addressing is another common solution to handling collisions. Rather than storing multiple values within the same bucket, if a key is mapped to an index that already has an existing key, the hashing function will use a probing algorithm to check other indexes within the array. 

Once it finds an available index, it will store the key and value in the bucket associated with that index. 

So each bucket will only store _one_ value.

Note that the search algorithm will follow the same set of sets as the insert algorithm. If the insert algorithm mapped the key to a specific index, then had to probe 4 other indexes to find an empty bucket, then the search algorithm will follow those same set of steps. 

This diagram from wikipedia visually illustrates this concept:

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Hash_table_5_0_1_1_1_1_0_SP.svg/380px-Hash_table_5_0_1_1_1_1_0_SP.svg.png"/>

#### Collisions and Time Complexity

Collisions are the reason hash tables have an O(n) worst case time complexity. 

For separate chaining, if all keys are mapped to the same index and all values are stored in the same bucket, then our search algorithm will have to  iterate through every value stored in that bucket before it can find the correct value - an O(n) operation.

It's a similar phenomenon for open addressing. The more entries you have in your hash table, the fewer empty buckets there will be, and the more steps your insert and search algorithms will have to take to add and access newly stored key-value pairs, eventually approaching O(n). 

### Load Factor

Part of determining a hash table's performance involves a metric call a "load factor". Basically, a load factor represents the relationship between the number of key value pairs stored within a hash table and the number of buckets available in that hash table.

`load factor = n / k`

In this example, `n` represents the number of key value pairs in the hash table and `k` represents the number of buckets available in the hash table.

As the value of the load factor approaches 1 - at which point the hash table would have the same number of values stored as entries available - the performance of the hash table worsens. 

Why? Well, because collisions start to become more likely. The fewer empty buckets available, the more likely it is that your hashing function will map two different keys to the same index and store multiple values in the same bucket.

Many hash table implementations have a <em>rehashing</em> feature built into them, where a hash table will increase the number of buckets it has when the load factor approaches 1. Note that rehashing itself can be a resource-intensive operation, as the computer has to reallocate memory for the newly sized hash table.

## Conclusion

Hash tables can be an extremely handy data structure to use to organize data and solve algorthmic problems, in part because of the way the information is organized, and in part due to their quick lookup operations. 

Oftentimes, accessing a key within a hash table will be referred to as having an O(1) time complexity. That's ideal for a hash table, and hash tables do routinely achieve that level of performance, but it's important to know that the under-the-hood mechanics aren't quite that simple, as we've discussed. 

It's also important to consider whether or not your hash table will be dynamically resized at runtime, in which case your computer could end up having to reallocate memory for that hash table a number of times, which could negatively impact the overall performance of your program. 

## Other Types of Hash Tables

It's important to note that not all hash tables use an array as the underlying data structure - some use Binary Search Trees. 

This changes the time complexity of adding and looking up values within a hash table from an average of O(1) and a worst case to O(n) to an average of O(log n) and a worst case of O(log n). 

One version - array as underlying structure - offers a chance at improved performance, but an overall worst case time complexity. The other - Binary Search Tree as underlying structure - offers a more consistent performance with a lower peak performance.

## Using Hash Tables

As mentioned before, most languages have built in hash tables:

- JavaScript - all `objects` in JavaScript are implemented as hash tables, as are Sets and Maps.
- Ruby - ruby `hashes` are ruby's implementation of a hash table
- Python - python `dictionaries` are python's implementation of a hash table. Python Sets are also implemented as hash tables.
- Java - Java has `HashSets`s, `HashMap`s, `LinkedHashSet`s, and `LinkedHashMap`s
- Go - Go has a `map` data type, which is implemented as a hash table
- C++ - includes the `unordered_map`
- Rust - includes `HashMap` and `HashSet` as part of it's standard library

Due to the wide inclusion of hash tables (also known as hash maps, as previously mentioned) in major programming languages, you'll often be able to leverage the functionality of a hash table without having to implement your own custom solution. Just get familiar with your language of choice's hash table, and read up on how that language uses and implements it.

## Hash Table Practice

It's possible that you'll receive questions in technical interviews where the solution will involve using a hash table. To get more practice, try working through these <a href="https://leetcode.com/tag/hash-table/">LeetCode problems</a>! 

If you haven't created a LeetCode account yet, I'd highly recommend doing so. It's a great place to hone your algorithmic problem solving ability and learn the value of humility, patience, perserverance, and practice! 

Don't be afraid of trying problems that are very difficult, or of looking at solutions if you've been grinding away forever to no avail. These solutions will teach you to think about programming in a new way! It doesn't mean that you've "failed" if you study someone else's code to figure out what they're doing and how they're doing it. We learn by example, especially in programming! 

If you do look up somebody else's solution, try implementing it yourself! That will give you a much better grasp of how the code is working, and improve your ability to apply the concepts you've learned in the future.

## Further Reading
- Curious about how a custom hash table might be implemented? (Wondering if it might <a href="https://leetcode.com/problems/design-hashmap/">come up during a technical interview</a>?)
  - Check out our Custom Hash Table write-up, where we walk through the implementation of our own Custom Hash Table!
- Want to keep learning about Data Stuctures? Check out our next reading on Sets, which we can use Hash Tables to implement!
