#!/usr/bin/env python

import unittest

from flickrapi import shorturl

class ShortUrlTest(unittest.TestCase):
    '''Tests the shorturl module.'''

    def test_encoding(self):
        '''Test ID to Base58 encoding.'''

        self.assertEqual(shorturl.encode('4325695128'), '7Afjsu')
        self.assertEqual(shorturl.encode('2811466321'), '5hruZg')

    def test_decoding(self):
        '''Test Base58 to ID decoding.'''

        self.assertEqual(shorturl.decode('7Afjsu'), '4325695128')
        self.assertEqual(shorturl.decode('5hruZg'), '2811466321')

    def test_short_url(self):
        '''Test photo ID to short URL conversion.'''

        self.assertEqual(shorturl.url('4325695128'),
                'http://flic.kr/p/7Afjsu')
        self.assertEqual(shorturl.url('2811466321'),
                'http://flic.kr/p/5hruZg')
