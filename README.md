## isAWord

You have a string of text and an error has occured leading to all the spaces to be removed. The following code has been created to try and recreate all possible original solutions.

## word_sieve()

This function checks all prefixes of the string and checks if they are a word. If true then the string is split and all the prefixes of the latter of the split string are checked. This is done again and again until all possible computations have been exhausted. Valid solutions are then determined by a terminating character. 

## brute_force()

This function finds all possible substrings and checks which ones are words, valid words are saved in a tuple with their start and end positions. Based on these start and end positions the original possible solutions can be recreated. This ideally should be implemented in a tree to reduce the program runtime.

## [PyEnchant](https://github.com/rfk/pyenchant)

This code utilises [PyEnchant](https://github.com/rfk/pyenchant) which has a function which returns True/False when given a "string" that is or isn't a word. 