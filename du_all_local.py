#!/usr/bin/env python

######################################################################
#
#
######################################################################

from __future__ import print_function

import json
import os


class Mountpoint:
    def __init__(self, line):
        data = line.split()
        self.device = data[0]
        self.total = int(data[1])
        self.used = int(data[2])
        self.avail = int(data[3])
        self.usedPerc = int(data[4].replace('%', ''))
        self.path = data[5]

    def usedPercentageString(self):
        return "%d" % self.usedPerc

    def shouldBeReported(self):
        return (self.device.startswith('/') and
                not self.device.startswith('/dev/loop'))


def getDfLines():
    cmd = "df -Pl 2>/dev/null"
    output = os.popen(cmd).read()
    output = output.strip()
    lines = output.split("\n")
    return lines[1:] # skip header


def getCounters(lines):
    prefix = 'system.disk.'
    counters = {}
    for line in lines:
        mountpoint = Mountpoint(line)
        if mountpoint.shouldBeReported():
            key = "%sused_percentage:%s" % (prefix, mountpoint.path)
            counters[key] = mountpoint.usedPercentageString()
    return counters


def getCountersAsJson(lines):
    counters = getCounters(lines)
    return json.dumps(counters)


if __name__ == "__main__":
    lines = getDfLines()
    jsonOutput = getCountersAsJson(lines)
    print(jsonOutput)

