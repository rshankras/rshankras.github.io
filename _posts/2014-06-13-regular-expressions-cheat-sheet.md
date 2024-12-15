---
title: "Regular Expressions Cheat sheet"
date: "2014-06-13"
categories: 
  - "programming"
tags: 
  - "regex"
  - "regular-expression"
---

Regular Expressions form sequence of characters which can be used for pattern matching. They are quite powerful tool for finding or matching combination of characters.

**Special Characters in Regular Expression**

1. backslash ( \\ ) - Used for matching special character by proceeding with backslash Eg:- For matching period in a string use backslash before period (\\.) as period is a special character.

3. asterisk ( \* ) - Refers to zero or more occurrences of regular expression.

5. plus ( + ) - Refers to one or more occurrences of regular expression.

7. question mark ( ? ) - Used for special optional characters.

9. period ( . ) - Matches any character except newline.

11. caret ( ^ ) - Refers to start of the current line.

13. ampersand ( & ) - Ampersand used for matching both expression

15. Or sign ( | ) - Used for matching either expression.

17. dollar sign ( $ ) - Refers to end of entire regular expression.

19. square brackets ( \[ \] ) - Matches any one character in the square brackets. If ^ sign is present before the contents in square brackets then characters except those mentioned inside square brackets are matched.

**Regular Expression example**

**/^\[a-z0-9\]{6,10}$/**

The above expression specifies the start of the string as either alphabets or numbers with characters count minimum as 6 and maximum as 10. This would match string such as david007 and not david-007 as hyphen is not included in the RegEx pattern. And to fix this change the pattern to include hyphen. **/^\[a-z0-9-\]{6,10}$/**
