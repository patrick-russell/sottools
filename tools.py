"""
    tools.py
    ~~~~~~~~

    Contains the various user facing tools  on the site

    :copyright: © 2018 by Patrick Russell
    :license: MIT, see LICENSE for more details.
"""

from collections import defaultdict
from sotgame import sot


def rollup_loot():
    """Big function to roll up loot data
    """
    pass


def add_amounts():
    pass


def median_amounts():
    pass


def mean_amounts():
    pass


def process_loot(form_data):
    """Do the actual math to estimate loot value

    :param MultiDict form_data: `form` attribute from the `Flask.request
    object

    MultiDIct can hold a list of values for a given key::

        d = MultiDict([('loot_options', 'bluage'),
                       ('loot_options', 'cherow'),
                       ('loot_count', '2'),
                       ('loot_count', '5')])

    """

    data = defaultdict(int)
    lists = []
    for k, v in form_data.lists():
        if k == 'csrf_token':
            continue
        else:
            lists.append(v)
    for i, j in zip(*lists):
        data[i] += int(j)
    loot = {}
    items = sot.items
    for k, v in data.items():

        loot[k] = {'count': v,
                   'median': round(items[k]['median'] * v, 2),
                   'average': round(items[k]['average'] * v, 2),
                   'standard deviation': round(items[k]['stdev'] * 2),
                   'name': items[k]['item']}
    count = sum([v['count'] for k, v in loot.items()])
    median = sum([v['median'] for k, v in loot.items()])
    average = sum([v['average'] for k, v in loot.items()])
    stdev = sum([v['standard deviation'] for k, v in loot.items()])
    totals = {'median': median,
              'average': average,
              'stdev': stdev,
              'count': count}
    return loot, totals
