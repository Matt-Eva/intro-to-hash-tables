# Intro to Hash Tables

Hash tables (also known as hash maps) are a commonly used data structure that appear in many programming languages and solutions to algorithmic problems. If you've started learning a programming language, you've likely already used a hash table. Data structures like dictionaries in Python, hashes in Ruby, and objects, maps, and sets in JavaScript are all implemented as hash tables.

## But What is a Hash Table?

Put simply, a hash table is a type of data structure that connects keys to values. This is different than an array, which maps indexes to values, where the index corresponds to a specific address in computer memory.

In reality, hash tables actually <em>are</em> arrays - or, rather, they use arrays under the hood.

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
<td>2</td>
<td>z</td>
<td>15</td>
</tr>
<tr>
<td>3</td>
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
