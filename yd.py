#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  file   : yd.py
#  author : atupal
#
#  Copyright 2013 atupal [HUST university uniquestudio algorithm group] <me@atupal.org>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#  site: http://atupal.org

keyfrom = 'atupal-site'
key = '401682907'

import json
import urllib2
import urllib
import sys

def main():
    query = sys.argv[1]
    url = 'http://fanyi.youdao.com/openapi.do?keyfrom=' + keyfrom + '&key=' + key + '&type=data&doctype=json&version=1.1&q=' + urllib.quote(query)
    ret = json.load(urllib2.urlopen(url))
    for i in ret['translation']:
        print i

if __name__ == "__main__":
    main()
