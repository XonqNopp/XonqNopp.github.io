git sub
#######

:title:    git sub
:date:     2018-12-10 14:34
:category: git
:tags:     git



If you are sharing code in several repository or using third-party code, you are likely to have come to think how to do
it efficiently.
Git provides some ways to do this, but...
All existing solution sucks:

* submodule is nice but painful for users, and for beginner developers
* subtree is nice but painful for developers since push can be wrong
* subrepo is nice but does not allow to change branch easily

So I have come to think that sticking to the basics is maybe better.
**Git sub** is a new way to include git repos in a git repo.
It is simply a clone of the other repo into the main repo and we track all files in the main repo as well.
For repositories with more than one developer, I advise to use sub.

You only need to take special action the first time.
I wrote a script for this here:
https://github.com/XonqNopp/conf/blob/master/git/bin/git-sub-init
This script is only needed the first time::

   git sub-init my/sub/path/in/repo https://github.com/awesome/repo

* If you are introducing a new sub, it will clone the repo and stage all files for commit.
* If you pulled from the repo and new commits introduce a sub, it will add the .git directory in the sub
  so you can easily change branch, commit or anything.

Later on, you can also check if there are uncommitted changes with this script:
https://github.com/XonqNopp/conf/blob/master/git/bin/git-sub-st


Pros
****

* all files available with a simple clone, no additional arg/command required


Cons
****

* if you do changes and commit them in main repo, sub remote won't be update.
  You need to cd there and commit-push as well


HowTo advice
************

* when changes are required in sub, cd there, do the changes, commit, push, and when state is clean (as opposed to
  submodule dirty status), cd back to main repo and commit.
  This way you ensure you use only versions of the sub which are available in the remote.
  To be sure to have everything synchronized on both repos, you can use ``git sub-st`` (see above).
