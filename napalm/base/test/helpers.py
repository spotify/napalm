"""Several methods to help with the tests."""


def test_model(model, data):
    """Return if the dictionary `data` complies with the `model`."""
    # Access the underlying schema for a TypedDict directly
    annotations = model.__annotations__
    if model.__total__:
        same_keys = set(annotations.keys()) == set(data.keys())
    else:
        same_keys = set(data.keys()) <= set(annotations.keys())

    if not same_keys:
        print(
            "model_keys: {}\ndata_keys: {}".format(
                sorted(annotations.keys()), sorted(data.keys())
            )
        )

    correct_class = True
    for key in data.keys():
        correct_class = isinstance(data[key], annotations[key]) and correct_class
        if not correct_class:
            print(
                "key: {}\nmodel_class: {}\ndata_class: {}".format(
                    key, annotations[key], data[key].__class__
                )
            )

    return correct_class and same_keys
