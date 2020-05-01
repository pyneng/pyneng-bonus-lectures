"""
Filter to convert results from network device show commands obtained from ios_command,
eos_command, et cetera to structured data using TextFSM templates.
"""
import os
from textfsm import clitable


def get_template_dir():
    """Find and return the ntc-templates/templates dir."""
    try:
        template_dir = os.environ["NET_TEXTFSM"]
        index = os.path.join(template_dir, "index")
        if not os.path.isfile(index):
            # Assume only base ./ntc-templates specified
            template_dir = os.path.join(template_dir, "templates")
    except KeyError:
        # Construct path ./templates
        current_dir = os.path.abspath(".")
        template_dir = os.path.join(current_dir, "templates")

    index = os.path.join(template_dir, "index")
    if not os.path.isdir(template_dir) or not os.path.isfile(index):
        msg = """
Valid ntc-templates not found, please install https://github.com/networktocode/ntc-templates
and then set the NET_TEXTFSM environment variable to point to the ./ntc-templates/templates
directory."""
        raise ValueError(msg)
    return template_dir


def get_structured_data(raw_output, platform, command):
    """Convert raw CLI output to structured data using TextFSM template."""
    template_dir = get_template_dir()
    index_file = "index"  # CHANGED
    textfsm_obj = clitable.CliTable(index_file, template_dir)
    if platform:
        attrs = {"Command": command, "Platform": platform}
    else:
        attrs = {"Command": command}
    try:
        # Parse output through template
        textfsm_obj.ParseCmd(raw_output, attrs)
        return clitable_to_dict(textfsm_obj)
    except CliTableError:
        return raw_output


def clitable_to_dict(cli_table):
    """Converts TextFSM cli_table object to list of dictionaries."""
    headers = list(map(str.lower, cli_table.header))
    return [dict(zip(headers, row)) for row in cli_table]


def net_textfsm_parse(output, command, platform=None):
    """Process config find interfaces using ip helper."""
    try:
        output = output["stdout"][0]
    except (KeyError, IndexError, TypeError):
        pass
    return get_structured_data(output, platform, command)


class FilterModule(object):
    """Filter to convert results from network device show commands obtained from ios_command,
    eos_command, et cetera to structured data using TextFSM templates."""

    def filters(self):
        return {
            "parse_textfsm": net_textfsm_parse,
        }

