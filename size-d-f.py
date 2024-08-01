import os

def get_size(path):
    size = 0
    
    if os.path.isfile(path):
        size = os.path.getsize(path)
    else:
        for   dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                fp = os.path.join(dirpath, filename)
                if os.path.isfile(fp):
                    size += os.path.getsize(fp)
    
    return size
    
def get_size_format(b, factor=1024, suffix="B"):
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.0f}{unit}{suffix}"
        b /= factor
    return f"{b:.0f}Y{suffix}"

def main():
    pwd = os.getcwd()
    items = os.listdir(pwd)
    size_list = []
    
    for i in items:
        fp = os.path.join(pwd, i)
        size = get_size(fp)
        size_list.append((size,i))
        #print("{}\t{}".format(size, i))
    
    size_list.sort(key=lambda x: x[0], reverse=True)
    
    for size, i  in size_list:
        print("{}\t\t{}".format(get_size_format(size), i))
        
if __name__ == "__main__":
    main()
