"""DynamoDB table definitions"""
import json
from app import app, dynamo

sottools_sot_loot = dict(
    TableName='sottools_sot_loot',
    KeySchema=[
        {
            'AttributeName': 'loot_item',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'origin',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'sale_outpost',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'amount',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'loot_item',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'origin',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'sale_outpost',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'amount',
            'AttributeType': 'N'
        }
    ],
    ProvisionedThroughput={'ReadCapacityUnits': 5,
                           'WriteCapacityUnitys': 5
                           })

sottools_sot_loot_data = dict(
    TableName='sottools_sot_loot_data',
    KeySchema=[
        {
            'AttributeName': 'loot_item',
            'KeyType': 'HASH',
        },
        {
            'AttributeName': 'count_value',
            'KeyType': 'RANGE'
        },
        {
            'AttributeName': 'sum_value',
            'KeyType': 'RANGE'
        },
        {
            'AttributeName': 'median_value',
            'KeyType': 'RANGE'
        },
        {
            'AttributeName': 'mean_value',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'loot_item',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'count_value',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'sum_value',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'median_value',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'mean_value',
            'AttributeType': 'N'
        }
    ],
    ProvisionedThroughput={'ReadCapacityUnits': 5,
                           'WriteCapacityUnitys': 5
                           })

dyanamo_tables = [sottools_sot_loot, sottools_sot_loot_data]

with open('sot.json', 'r') as f:
    data = json.load(f)
    sottools_sot_loot_values = {
        'loot_item': data['items'],
        'origin': [location.keys()[0] for location in data['locations']],
        'sale_outpost': [outpost.keys()[0] for outpost in data['outposts']],
    }


def create_tables():
    with app.app_context():
        dynamo.create_all()
