import os

def search(path, indent=""):
    ret = ""
    tlines = 0
    tcomments = 0
    files = 0
    for i, n in enumerate(os.listdir(path)):
        if n[-3:] == ".py" or n[-4:] == ".pyw":
            files += 1
            with open(os.path.join(path, n), "r") as f:
                content = f.read().split("\n")
                
            lines = 0
            comments = 0
            for i, l in enumerate(content):
                line = l.strip(" ")
                if len(line) > 1:
                    if line[0] == "#":
                        comments += 1
                    else:
                        lines += 1
                        
            tlines += lines
            lines = indent + "Lines: " + str(lines) + "\n"
            tcomments += comments
            comments = indent + "Comments: " + str(comments) + "\n"
            ret += indent + n + "\n" + lines + comments + "\n"
        
            
        elif os.path.isdir(os.path.join(path, n)):
            if n != "Modules":
                level = search(os.path.join(path, n), indent=indent + "    ")
                if level[0] != "":
                    ret += indent + n + os.sep + "\n\n"
                    ret += level[0]
                    tlines += level[1]
                    tcomments += level[2]
    if tlines > 1 and files > 1:               
        ret += indent + "Total lines: " + str(tlines) + "\n"
        ret += indent + "Total comments: " + str(tcomments) + "\n\n\n"
    return ret, tlines, tcomments

path = input("Path to search ")
if path == "":
    path = "."
print(search(path)[0])
input("Press enter to exit. ")
    
