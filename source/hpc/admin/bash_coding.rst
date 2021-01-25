Bash Coding Standards
=====================

Scripting Language to use
-------------------------

Bash is the only shell language allowed in the Research Computing department. Therefore no shell, korn, TC shell, or c shell is permitted. Your shell script must start with ``#!/bin/bash``

When to use BASH
----------------

Shell scripting isn't a development language therefore its use should follow the following guideline.

* If you are automating tasks in Linux and system administration
* You are calling other binaries in Linux with relatively little data manipulation.
* You are implementing system wide configurations.

File Extension
--------------

Each bash script file should have .sh extension to know file type.

Comments
--------

Writing a script that is easy to read and easy to maintain, which means that it must have plenty of comments describing the steps. There is nothing worse than having to hack through someone else’s code that has no comments to find out what each step is supposed to do. It can be tough enough to modify the script in the first place, but having to figure out the mindset of the author of the script will sometimes make us think about rewriting the entire shell script from scratch. We can avoid this by writing a clearly readable script and inserting plenty of comments describing what our philosophy is and how we are using the input, output, variables, and files.

Introductory comments in your bash script
-----------------------------------------

Every bash script file must be documented with an introductory comment that provides information on the file name and its contents. Example below:

.. code-block:: bash

    #!/bin/Bash
    #========================================================================
    # SCRIPT:   NAME_of_SCRIPT
    # AUTHOR:   AUTHORS_NAME
    # DATE:     DATE_of_CREATION
    # VERSION:  1.1                                                         
    # USAGE:    stale-links.sh [-d] [-l] [-h] [starting directories]
    # PURPOSE:  Give a clear, and if necessary, long, description of the
    #           purpose of the shell script. This will also help you stay 
    #           focused on the task at hand.
    #
    # REVISION: DATE_of_REVISION
    # BY: AUTHOR_of_MODIFICATION
    # MODIFICATION: Describe what was modified, new feature, etc --
    #
    #===========================================================================
 

Code Layout
-----------

Your bash script should have the following layout:

.. code-block:: bash

    #Introductory comments (See above)
    
    ##########################################################
    # DEFINE FUNCTIONS HERE
    ##########################################################
    
    
    ##########################################################
    # DEFINE FILES AND VARIABLES HERE
    ##########################################################
    
    
    ##########################################################
    # BEGINNING OF MAIN
    ##########################################################
    
    Your script
    
    # End of script
 

Function Comments
-----------------

Each function is described by an introductory comment. This comment contains the function name, a short description and the description of the parameters if any. The name of the author and the date of the issue should be added in case of subsequent amendments. Below is a format to follow:

.. code-block:: bash

    #Bash Function comments
    #=== FUNCTION ================================================================
    # NAME: usage
    # DESCRIPTION: Display usage information for this script.
    # PARAMETER 1:              ---
    #=============================================================================
 

Instruction Comments and Readability of your code
--------------------------------------------------

Try to comment as much as possible what your code is doing in a clear concise manner. To make it easier for yourself to keep your code healthy and improve it regularly you should keep an eye on the readability of what you write. Examples below

.. code-block:: bash

    ## Check if the new user id already exists in /etc/passwd
    password_chk=$(grep -c ":$new_uid:" /etc/passwd)
    
    if (( $password_chk > 1 )) then;
    ## If it does, skip
    echo "UID: $new_uid seems to exist check /etc/passwd"
    
    else
    ## If not add the user
    useradd -u $new_uid -c "$new_comment" -md $new_homedir -s $new_shell -g $new_group
    
    ## Check if new_pass is empty or not
    if [ ! -z $new_pass ] then;
        ## If not empty set the password and pass expiry
        echo $new_pass | passwd --stdin $new_user
        chage -M $new_chage $new_user
        chage -d 0 $new_user
    fi
    fi

Code Readability
----------------

.. code-block:: bash

    friends=( "Marcus The Rich" "JJ The Short" "Timid Thomas" "Michelangelo The Mobster" )
    
    # Say something significant about my friends.
    for name in "${friends[@]}" do;
    # My first friend (in the list).
    if [[ $name = "${friends[0]}" ]] then;
        echo "$name was my first friend."
    
    # My friends whose names start with M.
    elif [[ $name = M* ]] then;
        echo "$name starts with an M"
    
    # My short friends.
    elif [[ " $name " = *" Short "* ]] then;
        echo "$name is a shorty."
    
    # Friends I kind of didn't bother to remember.
    else
        echo "I kind of forgot what $name is like."
    fi
    
    done
 

Below is a horrible way of writing a bash script

.. code-block:: bash


    x=(       Marcus\ The\ Rich JJ\ The\ Short
    Timid\ Thomas Michelangelo\ The\ Mobster)
    for name in "${x[@]}"
    do if [ "$name" = "$x" ]; then echo $name was my first friend.
    elif
    echo $name    |   \
    grep -qw Short
    then echo $name is a shorty.
    elif [ "x${name:0:1}" = "xM" ]
    then echo $name starts   with an M; else
    echo I kind of forgot what $name \
    is like.; fi; done

**For readability keep the following points in mind**

* Healthy white space gives you breathing space. Indent your code properly and consistently. Use blank lines to separate paragraphs or logic blocks. 

* Avoid backslash-escaping. It's counter-intuitive and boggles the mind when overused. Even in small examples it takes your mind more effort to understand a\ b\ c than it takes to understand 'a b c'. 

* Comment your way of thinking before you forget. You might find that even code that looks totally common sense right now could become the subject of "What the hell was I thinking when I wrote this?" or "What is this supposed to do?". 

* Consistency prevents mind boggles. Be consistent in your naming style. Be consistent in your use of capitals. Be consistent in your use of shell features. In coding, it's good to be simple and predictable.

Formatting
----------

Indentation is a must for all your loops and conditional statements.

.. code-block:: bash

    If Block
    Bash Formatting
    echo –n “How old are you? “
    read age
    If (( age >= 0 && age <=12 )); then 
    echo “A child is a garden of verses”
    
    elif (( age > 12 && age <= 19 )); then 
    echo “Rebel without a cause”
    
    elif (( age > 19 && age <= 29 )); then 
        echo “You got the world by the tail”
    
    else
    echo “sorry I asked"

For Statement
-------------

.. code-block:: bash

    for (( i=1; i<=4; i++)) do;
        echo "Number is $i"
    done
  
    for user_info in $(grep "/bin/bash" /etc/passwd | grep ":/home") do;
    user_name=$(echo $user_info | cut -d: -f1)
    home_dir=$(echo $user_info | cut -d: -f6)
    chown -R $user_name $home_dir
    done

While Statement
---------------

.. code-block:: bash

    a=0
    while (( $a < 10 )) do;
    echo $a
    a++
    done
    Case Statement
    Case Statement
    printf '%s ' 'Which fruit do you like most?'
    read fruit
    
    case $fruit in
        apple)
            echo 'Mmmmh... I like those!'
            ;;
        banana)
            echo 'Hm, a bit awry, no?'
            ;;
        orange|tangerine)
            echo $'Eeeks! I don\'t like those!\nGo away!'
            exit 1
            ;;
        *)
            echo "Unknown fruit - sure it isn't toxic?"
    esac

Naming Conventions
------------------

1. Function names are lower case with underscores to separate words. Names should be as descriptive and meaningful as possible. 
Example: ``check_to_see_if_user_authroized()``
2. Variable names are lower case with underscores to separate words. Names should be as descriptive and meaningful as possible. 
Example: ``$current_user``
3. Environment variables are all upper case with underscores and declared at the top

Scope of Bash Variables
-----------------------

Local variables are visible only within the block of code. local is a keyword which is used to declare the local variables. In a function, a local variable has meaning only within that function block. Use local variables if you do not want your variables to be visible in the entire script and visible to the shell environment. The use of local variables greatly enhances the debugging of your script.

.. code-block:: bash

    $ cat localvar.sh
    #!/bin/bash
    pprint()
    {
    local lvar="Local content"
    echo -e "Local variable value with in the function"
    echo $lvar
    gvar="Global content changed"
    echo -e "Global variable value with in the function"
    echo $gvar
    }
    
    gvar="Global content"
    echo -e "Global variable value before calling function"
    echo $gvar
    echo -e "Local variable value before calling function"
    echo $lvar
    pprint
    echo -e "Global variable value after calling function"
    echo $gvar
    echo -e "Local variable value after calling function"
    echo $lvar

Execute the above script

**localvar script**

.. code-block:: bash

    Global variable value before calling function
    Global content
    Local variable value before calling function
    
    Local variable value with in the function
    Local content
    Global variable value with in the function
    Global content changed
    Global variable value after calling function
    Global content changed
    Local variable value after calling function

Use $(command) for command substitution
----------------------------------------

Back ticks are not allowed. Please use the following convention

**Command Substitution**

.. code-block:: bash

    today_date=`date +%F`   ---- Not Correct
    today_date=$(date +%F)  ---- Correct Way


Evaluating an Expression
------------------------

To evaluate an expression use double brackets instead of single brackets. Please use the following convention

**Evaluate an Expression**

.. code-block:: bash

    test $name != Tom                          ---- Not Correct
    [$name == Tom ]                            ---- Not Correct
    [[ $name == [Tt]om ]]                      ---- Correct Way
    [[ $name == [Tt]om && $friend == "Jose" ]] ---- Correct Way

Arithmetic Expression
---------------------

To evaluate arithmetic expression use double parentheses instead of single parenthesis. Please use the following convention

**Arthemetic Expressions**

.. code-block:: bash

    a=5
    b=4
    
    # Not Correct
    if [[ $a -gt $b ]] then;
        ...
    fi
    
    # Correct Way
    if (( a > b )) then;
        ...
    fi
  
 