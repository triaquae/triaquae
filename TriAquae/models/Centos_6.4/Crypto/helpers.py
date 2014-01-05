def split_len(seq, length):
    return [seq[i:i+length] for i in range(0, len(seq), length)]