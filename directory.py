# import os 

# dir=("AIPA")
# try:
#     os.makedirs(dir) 
#     print(f'folder created : {dir}')
# except FileExistsError:
#     print(f'folder already exist.')
# finally:
#     print("code is executed.")

# cur_name="ddddd"
# new_name="kevin"
# try:
#     os.rename(cur_name,new_name)
# except FileNotFoundError:
#     print("the directory not found")

# import shutil

# dir_del="kevin"
# try:
#     shutil.rmtree(dir_del)
#     print("Directory Deleted")
# except FileNotFoundError:
#     print("Folder does not existed")
# except PermissionError:
#     print("Permission denied ")
# except Exception as e:
#     print(f'An error occurred :{e}')

# import os 

# dir="DIVAKAR"
# try:
#     os.makedirs(dir,exist_ok=True)
#     file_name="books.txt"
#     file_path=os.path.join(dir,file_name)
#     with open(file_path,"w")as file:
#         file.write("hi ra varun unga onga vadu raa bamchik .")
#         print(f"file: '{file_name}'created successfully in {dir}'")
# except FileNotFoundError as e:
#     print(f"An Error occurred")


# import os 

# dir="."

# with os.scandir(dir)as entries:
#     print(f"Contents of the folder are :{dir}'")
#     for entry in entries:
#         print(entry.name)


# dir=os.listdir()
# print("Contents in folder are  : ",dir)

# dir=os.getcwd()
# print("Working folder is :",dir)

# import shutil

# dir_copy="DIVAKAR"
# try:
#     shutil.copytree(dir_copy,"abc ")
#     print("Directory  copied successfully")
# except Exception as e:
#     print(f"An error occured  ")

# dir_move="DIVAKAR"
# try:
#     shutil.move(dir_move,"abc")
#     print("Directory moved successfully ")
# except Exception as e:
#     print(f"An error occurred: {e}")

# dir_del="DIVAKAR"
# try:
#     shutil.rmtree(dir_del,"abc")
#     print("Directory Deleted ")
# except FileNotFoundError:
#     print(f"Folder does not exist")
# except PermissionError:
#     print(f"Access denied ")
# except Exception as e:
#     print(f'An error occurred')