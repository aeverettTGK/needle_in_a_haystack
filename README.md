# Needle in a haystack

Python scripting activity involving reading/writing files and plotting data

# Contents

-   [Getting set up](#getting-set-up)
-   [Completing the exercise](#completing-the-exercise)


# Getting set up

At this point, you should have
(1) basic knowledge on using the command line to navigate in terminal,
(2) an account on [Github](https://github.com/), and
(3) been introduced to the very basics of [Git](https://git-scm.com/).

IF you don't know how to use terminal, don't have a github account, or don't know how to use git, notify your instructor (they will help you get the pretest up and running). Otherwise, proceed to #1 below.

1.  Login to your [Github](https://github.com/) account.

1.  Fork [this repository](https://github.com/KLab-UT/needle_in_a_haystack) by
    clicking the 'Fork' button on the upper right of the page.

    After a few seconds, you should be looking at *your* 
    copy of the repo in your own Github account.

1.  Click the 'Clone or download' button, and copy the URL of the repo via the
    'copy to clipboard' button.

1.  In your terminal, navigate to where you want to keep this repo (you can
    always move it later, so just your home directory is fine). Then type:

        $ git clone the-url-you-just-copied

    and hit enter to clone the repository. Make sure you are cloning **your**
    fork of this repo.

1.  Next, `cd` into the directory:

        $ cd the-name-of-directory-you-just-cloned

1.  At this point, you should be in your own local copy of the repository.

1.  As you work on the exercise below, be sure to frequently `add` and `commit`
    your work and `push` changes to the *remote* copy of the repo hosted on
    GitHub. Don't enter these commands now; this is just to jog your memory:

        $ # Do some work
        $ git add file-you-worked-on.py
        $ git commit
        $ git push origin master

---

# Introduction

Review and critique the module titled 'create_haystack.py'

- What does this module do?
- How can you run it? (make sure it works)
- What coding criticisms do you have about it?

# Activity

Within this repository there is a file called ```haystack.txt```. Each haystack is a text file made up mostly of 'X' characters ("hay"). Your job is to find out if there are any '|' characters ("needles") in your haystack. You should:
1. Determine if there is a needle
2. Indicate the line and position where each needle is located
3. Determine how many needles there are total
4. Create a scatterplot of the needle coordinates. The 'X' axis should be the length of each row in the haystack, and the 'Y' axis should be the number of lines in the haystack.
5. Create a histogram where the 'X' axis is the number of lines in the haystack and the 'Y' axis is the number of needles within a given row.

# Tips
1. Start by writing pseudocode to solve this puzzle
1. An example haystack is within this directory- use this to practice with
1. Work on one objective at a time
