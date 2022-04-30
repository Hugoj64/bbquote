from mlproject.distance import haversine

def test_float():
    assert type (haversine(48.865070, 2.380009,48.852472071224774, 2.3338034067084314)) == float
