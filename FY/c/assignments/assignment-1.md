# Q.1 Write a short note on UNIX operating System.

Ans:

Unix is a family of multitasking, multiuser computer operating systems that derive from the original AT&T Unix, whose development started in 1969 at the Bell Labs research center by Ken Thompson, Dennis Ritchie, and others.

Initially intended for use inside the Bell System, AT&T licensed Unix to outside parties in the late 1970s, leading to a variety of both academic and commercial Unix variants from vendors including University of California, Berkeley (BSD), Microsoft (Xenix), Sun Microsystems (SunOS/Solaris), HP/HPE (HP-UX), and IBM (AIX). In the early 1990s, AT&T sold its rights in Unix to Novell, which then sold the UNIX trademark to The Open Group, an industry consortium founded in 1996. The Open Group allows the use of the mark for certified operating systems that comply with the Single UNIX Specification (SUS).

Unix systems are characterized by a modular design that is sometimes called the "Unix philosophy". According to this philosophy, the operating system should provide a set of simple tools, each of which performs a limited, well-defined function. A unified and inode-based filesystem (the Unix filesystem) and an inter-process communication mechanism known as "pipes" serve as the main means of communication, and a shell scripting and command language (the Unix shell) is used to combine the tools to perform complex workflows.

Unix distinguishes itself from its predecessors as the first portable operating system: almost the entire operating system is written in the C programming language, which allows Unix to operate on numerous platforms.

Unix was originally meant to be a convenient platform for programmers developing software to be run on it and on other systems, rather than for non-programmers. The system grew larger as the operating system started spreading in academic circles, and as users added their own tools to the system and shared them with colleagues.

At first, Unix was not designed to be portable or for multi-tasking. Later, Unix gradually gained portability, multi-tasking and multi-user capabilities in a time-sharing configuration. Unix systems are characterized by various concepts: the use of plain text for storing data; a hierarchical file system; treating devices and certain types of inter-process communication (IPC) as files; and the use of a large number of software tools, small programs that can be strung together through a command-line interpreter using pipes, as opposed to using a single monolithic program that includes all of the same functionality. These concepts are collectively known as the "Unix philosophy". Brian Kernighan and Rob Pike summarize this in The Unix Programming Environment as "the idea that the power of a system comes more from the relationships among programs than from the programs themselves".

By the early 1980s, users began seeing Unix as a potential universal operating system, suitable for computers of all sizes. The Unix environment and the client–server program model were essential elements in the development of the Internet and the reshaping of computing as centered in networks rather than in individual computers.

Both Unix and the C programming language were developed by AT&T and distributed to government and academic institutions, which led to both being ported to a wider variety of machine families than any other operating system.

The Unix operating system consists of many libraries and utilities along with the master control program, the kernel. The kernel provides services to start and stop programs, handles the file system and other common "low-level" tasks that most programs share, and schedules access to avoid conflicts when programs try to access the same resource or device simultaneously. To mediate such access, the kernel has special rights, reflected in the distinction of kernel space from user space, the latter being a priority realm where most application programs operate. 

# Q.2 Illustrate with syntax and example any 20 Linux commands for performing the operation on Linux system.

Linux 'commands' are the programs installed on the system, and by typing them in, we are utilizing them in a command-line interface. Most of the Linux commands have roots back in UNIX, and so, they follow the UNIX style of interacting. Most of them have the syntax of `command [-options or --options] [filename/input]`, for e.g.,  `ls -la Downloads`.

A few commands used in the Linux operating system are:
    
|Command| Function                                         |Usage                         |
|-------| ------------------------------------------------ | ---------------------------- |
|man    | UNIX help facility                               | man -k topic or man command  |
|ls     | directory listing                                | ls ~                         | 
|mv     | renames (moves) file                             | mv oldfile.txt newfile.txt   |
|cp     | copies files                                     | cp origfile.txt copyfile.txt |
|rm     | deletes (removes) file                           | rm file.txt                  |
|cd     | change directory                                 | cd newdirectory              |
|mkdir  | create new directory                             | mkdir mea443                 |
|rmdir  | removes directory                                | rmdir mea443                 |
|df     | check disk status                                | df -h                        |
|du     | show your disk usage, including subdirectories   | du -h                        |
|ps     | list your processes                              | ps -aux                      |
|kill   | stops processes                                  | kill -9 process_id           |
|cat    | list contents of file                            | cat file1 >> file2           |
|more   | view contents of file                            | more filename.txt            |
|head   | view first 10 lines of file                      | head filename.txt            |
|tail   | view last 10 lines of file                       | tail filename.txt            |
|diff   | shows differences in files                       | diff file1 file2             |
|file   | displays type of file                            | file filename                |
|chmod  | changes file mode                                | chmod u+x file               |
|grep   | search for string in file                        | grep string filenames        |
|vim    | a text editor                                    | vi filename                  |
|ssh    | login to remote host                             | ssh remote_ip_number         |
|gcc    | a standard C compiler                            | gcc test.c                   |
|awk    | an extremely powerful data manipulation program. | awk "{print 1}" test         |
|who    | show current users                               | who                          |
|pwd    | shows present working (current) directory        | pwd                          |
|setenv | set environmental variable                       | setenv DISPLAY sun2:0        |
|history| see list of past commands                        | history                      |
