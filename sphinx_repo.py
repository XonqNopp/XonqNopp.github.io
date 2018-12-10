#!/usr/bin/env python3
"""
Sphinx repository version
*************************

This module helps sphinx log the repository version when building.
"""
import os.path
from time import gmtime, strftime
from git import Repo


class GitVersion:
    """
    Get version and release infos for sphinx from git repository.

    Args:
        * *repoPath* (str)
    """
    TIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'

    def __init__(self, repoPath):
        now = strftime(self.TIME_FORMAT, gmtime())
        self.version = now
        self.release = now

        if repoPath is not None:
            self._parse(repoPath)

    def _parse(self, gitPath):
        branch = None
        tags   = None
        gitrepo = Repo(os.path.abspath(gitPath))
        commitobj = gitrepo.head.commit
        commitsha  = commitobj.hexsha[:7]
        commitdate = strftime(self.TIME_FORMAT, gmtime(commitobj.committed_date))
        if not gitrepo.head.is_detached:
            branch = gitrepo.active_branch.name
            try:
                tags = gitrepo.tags

            except TypeError as typeError:
                print('[warnings] Impossible to get the tags from this repos. \n {}'.format(typeError))
                # https://github.com/gitpython-developers/GitPython/issues/687
                # We will need to update the package as soon as the issue is fixed.

        branchStr = '@{}'.format(branch) if branch is not None else '_DETACHED'
        gitdata = '(git:{}{} {})'.format(commitsha, branchStr, commitdate)
        self.version = 'git:{}{}'.format(commitsha, branchStr)
        if bool(tags):
            tagname = gitrepo.tags[-1].name
            tagsha  = gitrepo.tags[-1].commit.hexsha[:7]

            if commitsha == tagsha:
                gitdata = tagname + ' ' + gitdata
                self.version = 'git:{}'.format(tagname)

        self.release = gitdata

