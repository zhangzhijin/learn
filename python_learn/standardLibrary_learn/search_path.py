import sys,os
path=sys.path
print( path)
#current file dir
path_str=os.path.abspath(sys.argv[0]);
print("path_str:"+path_str)
path_win=os.path.dirname(path_str);
print("path_win:"+path_win)
path_module=os.path.join(path_win, 'modules')
print("path_module:"+path_module)

sys.path.insert(0,path_win)
print( sys.path)



