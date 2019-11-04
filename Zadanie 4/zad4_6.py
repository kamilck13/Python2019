#4.6
def sum_seq(sequence):
    out = 0;
    if isinstance(sequence, (list, tuple)):
        for x in sequence:
            out += int(sum_seq(x))
    else:
        return sequence
    return out

if __name__ == "__main__":
    print(sum_seq([[],[4],(1,2),[3,4],(5,6,7)]))