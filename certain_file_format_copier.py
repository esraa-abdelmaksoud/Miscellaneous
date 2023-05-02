import os
import shutil

def main():
    root_path = '/home/erp-frappe/frappe-bench'
    path_list = []

    try:
        dest_path = os.mkdir('/home/erp-frappe/html_files')
        dest_path = '/home/erp-frappe/html_files'
    except:
        dest_path = '/home/erp-frappe/html_files'

    doc_path = os.path.join(dest_path, 'html_files_paths.txt')

    for root, _, files in os.walk(os.path.abspath(root_path)):
        for file in files:
            cur_path = os.path.join(root, file)
            if cur_path[-4:] == 'html' or cur_path[-3:] == 'htm':
                path_list.append(cur_path)

    with open(doc_path, 'w+') as f:
        for temp_path in path_list:
            try:
                _, tail = os.path.split(temp_path)
                shutil.copyfile(temp_path,os.path.join(dest_path,tail))
            except:
                pass
            f.writelines(temp_path)

if __name__ == '__main__':
    main()
