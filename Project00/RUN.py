import os

f=open('run_manim.bat','w')

py_file_name = 'test1.py'
pl = ' -pl'
pm = ' -pm'
str01 = 'python -m manim ' + py_file_name + pm
f.write(str01+'\n')
f.write("PAUSE")
f.close
os.system('run_manim.bat')



