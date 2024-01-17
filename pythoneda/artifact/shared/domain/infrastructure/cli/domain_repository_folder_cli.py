# vim: set fileencoding=utf-8
"""
pythoneda/artifact/shared/domain/infrastructure/cli/domain_repository_folder_cli.py

This file defines the DomainRepositoryFolderCli.

Copyright (C) 2023-today rydnr's pythoneda-artifact/shared-domain-infrastructure

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
from pythoneda.shared.artifact.infrastructure.cli import RepositoryFolderCli


class DomainRepositoryFolderCli(RepositoryFolderCli):

    """
    A PrimaryPort used to gather the repository folder information.

    Class name: DomainRepositoryFolderCli

    Responsibilities:
        - Parse the command-line to retrieve the information about the repository folder.

    Collaborators:
        - PythonEDA subclasses: They are notified back with the information retrieved from the command line.
    """

    def __init__(self):
        """
        Creates a new DomainRepositoryFolderCli instance.
        """
        super().__init__()
# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
