#!/usr/bin/env python3
import sys
import json


def get_id_map(test_list):
    id_map = {}
    for test in test_list:
        id_map[test['id']] = test
        if 'values' in test:
            id_map.update(get_id_map(test['values']))
    return id_map


def fill_test_values(tests, values):
    id_map = get_id_map(tests['tests'])

    for value in values['values']:
        id_map[value['id']]['value'] = value['value']


if __name__ == '__main__':
    values_file, tests_file, results_file = sys.argv[1:4]

    with open(values_file) as file:
        values = json.load(file)

    with open(tests_file) as file:
        tests = json.load(file)

    fill_test_values(tests, values)

    with open(results_file, 'w') as file:
        json.dump(tests, file, indent=4, ensure_ascii=False)
