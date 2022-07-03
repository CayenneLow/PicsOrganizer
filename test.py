import unittest
import json

from script import createLookUp

expected = {
    "2022": {
        "Jun": [
            "./input/Batch1/IMG_0042.HEIC",
            "./input/Batch1/IMG_0042.mov",
            "./input/Batch1/IMG_0043.HEIC",
            "./input/Batch1/IMG_0043.mov"
        ]
    },
    "2020": {
        "Mar": [
            "./input/Batch2/5793B00C-F8EF-4C6A-949F-D4BAAB93A2D3.jpg",
            "./input/Batch1/IMG_9478.PNG",
            "./input/Batch1/IMG_9480.PNG",
            "./input/Batch1/IMG_9481.HEIC",
            "./input/Batch2/IMG_9482.HEIC",
            "./input/Batch2/IMG_9483.HEIC",
            "./input/Batch2/IMG_9484.HEIC"
        ],
        "Apr": [
            "./input/Batch1/IMG_9699.PNG",
            "./input/Batch1/IMG_9700.PNG",
            "./input/Batch2/IMG_9701.HEIC",
            "./input/Batch2/IMG_9702.HEIC",
            "./input/Batch2/IMG_9705.PNG",
            "./input/Batch2/IMG_9710.HEIC",
            "./input/Batch2/IMG_9717.HEIC"
        ]
    }
}

class Test(unittest.TestCase):
    def runTest(self):
        actual, totalCount = createLookUp()
        self._sortLookups(actual)
        self._sortLookups(expected)
        self.maxDiff = None
        for year in expected.keys():
            self.assertTrue(year in actual.keys())
            for month in expected[year].keys():
                self.assertTrue(month in actual[year].keys())
                self.assertListEqual(expected[year][month], actual[year][month])

    def _sortLookups(self, lookUp):
        for year in lookUp:
            for month in lookUp[year]:
                lookUp[year][month] = sorted(lookUp[year][month])
    
    def _printDict(self, dict):
        print(json.dumps(dict, indent=4))


unittest.main()