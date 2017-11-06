import apiCall

def test_getUserComments():
    assert len(apiCall.getUserComments('vocabbottester', 0))==1