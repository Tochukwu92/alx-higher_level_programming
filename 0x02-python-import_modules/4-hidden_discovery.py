#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for arr in dir(hidden_4):
        if arr[0] != '_' and arr[1] != '_':
            print(arr)
