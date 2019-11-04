
#4.7
def flatten(sequence):
    out = list()
    if isinstance(sequence, (list, tuple)):
        for x in sequence:
            if isinstance(x, (list, tuple)):
                tmp = flatten(x)
                out += tmp
            else:
                out.append(x)
    return out

if __name__ == "__main__":
    print(flatten([1,(2,3),[],[4,(5,6,7)],8,[9]]))