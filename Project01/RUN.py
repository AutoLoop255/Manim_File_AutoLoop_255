import os

f=open('run_manim.bat','w')

py_file_name = 'main.py'
pl = ' -pl'
pm = ' -pm'
str01 = 'python -m manim ' + py_file_name + pl
f.write(str01+'\n')
f.write("PAUSE")
f.close
os.system('run_manim.bat')



