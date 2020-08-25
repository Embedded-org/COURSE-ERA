import sys
import os
print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', sys.argv)
path=sys.argv[1]  #"E:\\STOCKMARKET"
# r=root, d=directories, f = files
for root, dirs, files in os.walk(path, topdown=True):
    print("root is",root)
    #print(os.path.join(root, name))
    print("dirs is",dirs)
    for name in files:
        #print(os.path.join(root, name))
        print("files is",name)
