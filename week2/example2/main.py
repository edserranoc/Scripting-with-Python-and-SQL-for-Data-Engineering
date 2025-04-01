import os

def main():
    for root, directories, files in os.walk("/workspaces/Scripting-with-Python-and-SQL-for-Data-Engineering/"):
        #print (f"Root: {root}")
        #print(f"Directories {directories}")
        #print(f"files {files}")
        for _file in files:
            absolute_path = os.path.join(root,_file)
            print(f"File path: {absolute_path}")


if __name__ == '__main__':
    main()
