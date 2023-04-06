# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            if item.name != "Sulfuras":
                item.sell_in -= 1

            if item.name == "Aged Brie":
                if item.sell_in < 0:
                    item.quality += 2
                else:
                    item.quality += 1

            elif item.name == "Backstage passes":
                if item.sell_in <= 0:
                    item.quality = 0
                elif item.sell_in <= 5:
                    item.quality += 3
                elif item.sell_in <= 10:
                    item.quality += 2
                else:
                    item.quality += 1

            elif item.name == "Conjured":
                item.quality -= 2
            elif item.name != "Sulfuras":
                item.quality -= 1

            item.quality = max(0, item.quality)

            if item.name != "Sulfuras":  
                item.quality = min(50, item.quality)

            if item.sell_in < 0 and item.name != "Aged Brie":
                if item.name == "Conjured":
                    item.quality -= 2
                elif item.name != "Sulfuras":
                    item.quality -= 1

                item.quality = max(0, item.quality)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
