from pprint import pprint

import zen
import time
import unittest


def loader(key):
    with open("../../test-data/" + key, "r") as f:
        return f.read()


class ZenEngine:
    def test_decision_using_loader(self):
        engine = zen.ZenEngine({"loader": loader})
        r1 = engine.evaluate(
            "credit-analysis.tw.json",
            {"input": 5},
            {"trace": True}
        )
        pprint(r1)


if __name__ == '__main__':
    ZenEngine().test_decision_using_loader()
