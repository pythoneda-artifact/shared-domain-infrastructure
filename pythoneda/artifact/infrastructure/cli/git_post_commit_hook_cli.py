"""
pythoneda/artifact/infrastructure/cli/git_post_commit_hook_cli.py

This file defines the GitPostCommitHookCli.

Copyright (C) 2023-today rydnr's pythoneda-shared-pythoneda/domain-artifact-infrastructure

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import argparse
from pythoneda import BaseObject, PrimaryPort
from pythoneda.shared.artifact_changes import Change
from pythoneda.shared.artifact_changes.events import StagedChangesCommitted
from pythoneda.shared.git import GitCommit, GitDiff, GitRepo
import sys

class GitPostCommitHookCli(BaseObject, PrimaryPort):

    """
    A PrimaryPort to be used as post-commit-hook in git to send StagedChangesCommitted events.

    Class name: StagedChangesCommittedCli

    Responsibilities:
        - Parse the command-line to retrieve the information about the commit.

    Collaborators:
        - PythonEDA subclasses: They are notified back with the information retrieved from the command line.
        - pythoneda.shared.artifact_changes.events.StagedChangesCommitted
    """

    async def accept(self, app):
        """
        Processes the command specified from the command line.
        :param app: The PythonEDA instance.
        :type app: PythonEDA
        """
        parser = argparse.ArgumentParser(description="Sends a StagedChangesCommitted events")
        parser.add_argument(
            "-r", "--repository-folder", required=False, help="The repository folder"
        )
        args, unknown_args = parser.parse_known_args()

        if not args.repository_folder:
            print(f"-r|--repository-folder is mandatory")
            sys.exit(1)
        else:
            git_repo = GitRepo.from_folder(args.repository_folder)
            change = Change.from_unidiff_text(GitDiff(args.repository_folder).committed_diff(), git_repo.url, git_repo.rev, args.repository_folder)
            event = StagedChangesCommitted(change, GitCommit(args.repository_folder).latest_commit())
            GitPostCommitHookCli.logger().debug(event)
            await app.accept(event)
