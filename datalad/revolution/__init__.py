"""DataLad demo extension"""

__docformat__ = 'restructuredtext'

from .version import __version__

# defines a datalad command suite
# this symbold must be indentified as a setuptools entrypoint
# to be found by datalad
command_suite = (
    # description of the command suite, displayed in cmdline help
    "DataLad revolutionary command suite",
    [
        # specification of a command, any number of commands can be defined
        (
            # importable module that contains the command implementation
            'datalad.revolution.revsave',
            # name of the command class implementation in above module
            'RevSave',
            # optional name of the command in the cmdline API
            'rev-save',
            # optional name of the command in the Python API
            'rev_save'
        ),
        (
            'datalad.revolution.revcreate',
            'RevCreate',
            'rev-create',
            'rev_create'
        ),
        (
            'datalad.revolution.revstatus',
            'RevStatus',
            'rev-status',
            'rev_status'
        ),
        (
            'datalad.revolution.revrun',
            'RevRun',
            'rev-run',
            'rev_run'
        ),
    ]
)
