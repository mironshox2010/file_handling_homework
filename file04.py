def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    k = []
    for mir in data:
        if not mir.isdigit():
            k.append(mir)
    return k

data = open('txt_file/data04.txt').read()
print(main(data))
