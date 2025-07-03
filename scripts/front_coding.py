def front_coding(words):
    """
    Compresses a list of words using front coding.
    Args:
        words (list of str): The list of words to compress.
    Returns:
        list of str: The compressed list of words.
    """
    words.sort()
    compressed = []
    for i in range(len(words)):
        if i == 0:
            compressed.append(f"0|{words[i]}")
        else:
            prev = words[i - 1]
            curr = words[i]
            # find longest common prefix
            prefix_len = 0
            while prefix_len < min(len(prev), len(curr)) and prev[prefix_len] == curr[prefix_len]:
                prefix_len += 1
            suffix = curr[prefix_len:]
            compressed.append(f"{prefix_len}|{suffix}")
    return compressed
