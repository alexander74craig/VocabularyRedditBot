import travisTest

def test_Addition():
    assert travisTest.addition(1,2)==3
def test_AdditionLarge():
    assert travisTest.addition(100000,700000)==800000
