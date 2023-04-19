def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    lst = data.split(',')
    ans = []  
    for i in lst: 
        ans.append(int(i))
    return ans
s = open('txt_file/data01.txt').read()
print(main(s))