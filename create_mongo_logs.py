#!/usr/bin/env python2

import argparse
import yaml
import subprocess
import json

from pymongo import MongoClient, errors as py_errors
from shutil import copyfile, rmtree
from os import path, mkdir, system
from sys import argv


def run_commands(db):
    #
    for i in xrange(10):
        db.foo.insert({'field_a': 1, 'field_b': 2, 'field_c': i})

    for i in xrange(5):
        db.foo.find_one({'field_c': i})


def generate_logs(versions, output_dir, jscript):
    """
    generate_logs:  Main routine. Will take a dictionary (versions) with information on each version to run and save the
    logs to the output_directory

    :param versions:
    :param output_dir:
    :return:
    """
    # TODO: read configuration from file and add user defined parameters from the command line.
    with open('./mongod.conf', 'rt') as stream:
        yaml_data = yaml.safe_load(stream)

    # For all versions...
    for version in versions:
        print 'Version is %s ' % version['name']

        mongo_conf_file_name = path.join(output_dir, 'mongo-'+version['name']+'.conf')
        with open(mongo_conf_file_name, 'wt') as mongo_conf:
            # TODO: add cmd line params
            # ...
            yaml.safe_dump(yaml_data, mongo_conf)

        # Kill mongod if running
        system("killall -9 mongod")

        # nuke the db path
        db_path = yaml_data['storage']['dbPath']
        rmtree(db_path, ignore_errors=True)
        mkdir(db_path)

        # mongod binary
        bin_cmd = path.join(version['path'], 'mongod')

        # Start a mongod process, with the command line
        mongod = subprocess.Popen(bin_cmd + ' -f ' + mongo_conf_file_name, shell=True)
        print 'Starting process with PID %d' % mongod.pid

        if jscript:
            # run script
            mongo_cmd = path.join(version['path'], 'mongo')
            mongo = subprocess.Popen(mongo_cmd + ' < ' + jscript, shell=True)
            mongo.wait()
        else:
            try:
                client = MongoClient('localhost', 27017)
                db = client.test
                run_commands(db)
            except py_errors.ConnectionFailure:
                print 'Error trying to connect client to mongod process.'

        system("killall -9 mongod")

        mongod.terminate()

        mongo_log_file_name = path.join(output_dir, 'mongo-'+version['name']+'.log')
        system_log = yaml_data['systemLog']['path']

        if path.exists(system_log):
            copyfile(system_log, mongo_log_file_name)
        else:
            print 'Could not find log at "%s"'% system_log
    return 0


def read_versions(file_name):

    if path.exists(file_name):
        with open(file_name) as json_data:
            v = json.load(json_data)
            return v
    else:
        return None


if __name__ == "__main__":
    # parser = argparse._()

    # --mongod_conf defaults to ./mongod.conf
    # --versions_file  required.
    # --output_dir  defaults to .
    # --extra_mongod_config  defaults to None
    # --jscript defaults to None

    parser = argparse.ArgumentParser(description='Create mongod.log files for different versions of mongod.')
    parser.add_argument('-m', '--mongo_config',
                        help='Path to mongod.conf with configuration. Default is ./mongod.conf',
                        default='./mongod.conf')
    parser.add_argument('-v', '--versions',
                        help='Path to json file with versions. Default is ./versions.json',
                        default='./versions.json')
    parser.add_argument('-o', '--output_dir',
                        help='Path to directory where logs will be stored. Defaults to .',
                        default='.')
    parser.add_argument('-j', '--jscript',
                        help='Path to javascript file to execute.')

    config = parser.parse_args(argv[1:])

    versions = read_versions(config.versions)

    if versions:
        generate_logs(versions, config.output_dir, config.jscript)
    else:
        print 'Versions could not be read from "%s"' % config.versions
