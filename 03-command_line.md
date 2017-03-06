# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

**pwd** print current working directory  
**ls** list content of a directory  
**mkdir** create new directory  
**cd** change directory  
**cp** copy a folder/file  
**mv** move a folder/file  
**find** find a file  
**rm** delete a file  
**cat** show content of a file  
**touch** create/update a file  
**dir /a** list all hidden files
---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  


`ls` list the content of a folder

`ls -a` lists all files and folders in a directory

`ls -l` detailed list of content in a folder

`ls -lh` detailed list of content in a folder, human readable

`ls -lah` detailed list of all files in a folder, human readable

`ls -t` list with files in a folder based on timestamp, newest first

`ls -Glp` detailed list of content in a folder, folders a highlighted blue with '/' at the end

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > ls -m, ls -R, ls -1p, ls -x, ls -c

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

>> xargs is used to build and execute command lines from standard inputs. It is often used in combination with the `find` command - e.g. `find . name '*.txt' | xargs rm` searches for all text files and deletes them
 

