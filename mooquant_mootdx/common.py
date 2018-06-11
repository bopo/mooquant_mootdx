# MooQuant MooTDX module
#
# Copyright 2011-2015 Gabriel Martin Becedillas Ruiz
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Modified from MooQuant mootdx and Xignite modules

"""
.. moduleauthor:: Mikko Gozalo <mikgozalo@gmail.com>
"""
import datetime

import mooquant.logger
from mooquant.utils import dt
from mootdx import quotes, reader

logger = mooquant.logger.getLogger("mootdx")


def utcnow():
    return dt.as_utc(datetime.datetime.utcnow())


class MooTdxError(Exception):
    def __init__(self, message, response):
        Exception.__init__(self, message)


def get_quotes(currency_pair, category=9, offset=10):
    try:
        client = quotes.Quotes()
        result = client.bars(
            symbol=currency_pair,
            category=category,
            offset=offset)
    except BaseException:
        raise MooTdxError('Problem fetching quotes')

    return result


def get_reader(currency_pair):
    try:
        client = reader.Reader(tdxdir='/Volumes/BOOTCAMP/new_tdx')
        result = client.daily(symbol='600036')
    except BaseException:
        raise MooTdxError('Problem fetching readers')
