def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    k = 0
    for i in data:
        if i.isdigit():
            k += 1
    b = len(data)-k
    return [k]+[b]
data = open('txt_file/data05.txt').read()
print(main(data))