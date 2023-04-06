# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("Aged Brie", items[0].name)
        self.assertEquals(1, items[0].quality)

        
if __name__ == '__main__':
    unittest.main()
