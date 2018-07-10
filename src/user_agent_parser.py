"""
This module parses all the input user-agent lines from the stdin.
"""

import sys
from user_agents import parse


def get_dict(user_agent_line):
    """This function parses given user-agent line into a dict of Device, OS and Browser.

    :param user_agent_line: user-agent line.
    :type user_agent_line: str.
    :return: dict.
    """
    parsed = parse(user_agent_line)
    return {'Device': parsed.device.family, 'OS': parsed.os.family, 'Browser': parsed.browser.family}


for line in sys.stdin:
    contents = line.split('\t')
    city = contents[0]
    ua_items = get_dict(contents[1])
    print(city, ua_items['Device'], ua_items['OS'], ua_items['Browser'], sep='\t')
