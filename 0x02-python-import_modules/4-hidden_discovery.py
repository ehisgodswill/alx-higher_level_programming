#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    nameArr = dir(hidden_4)
    for name in nameArr:
        if name[:2] != "__":
            print(name)
