
'''
Explanation: Functions are provided which support file copying and removal
link:https://docs.python.org/3/library/shutil.html
'''

import shutil
if(len(fileList)>0):
  for file in fileList:
    try:
      print(file)
      shutil.move("/dbfs{}{}".format(input_folder,file),"/dbfs{}processed/Processed_{}".format(input_folder,file))
    except Exception as e:
      print(e)
      print("failed for :",file)
print("================== Initial load complete and files has been moved to processed folder ==================")
