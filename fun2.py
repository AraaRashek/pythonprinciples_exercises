

def mid(st):
    letters = list(st)
    length = len(letters)
    if length % 2 == 1:
        med_index = int(((length/2)-0.5))
        return letters[med_index]

    else:
        return ''
        
        
# def mid(string):
#     if len(string) % 2 == 0:
#         return ""
#     return string[len(string)//2]


if __name__ == "__main__":
    stl = mid('abc')
