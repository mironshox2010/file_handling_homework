def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    d = []
    for i in data:
        if i.isdigit():
            d.append(i)
    return d
data = open('txt_file/data03.txt').read()
print(main(data))