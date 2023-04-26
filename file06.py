def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    k = []
    h = data.split()
    for i in h:
        k.append(len(i))
        
    return k
    
data = open('txt_file/data06.txt').read()
print(main(data))

# Read data from file