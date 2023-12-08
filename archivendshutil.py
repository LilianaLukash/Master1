import shutil
from pathlib import Path

def create_backup(path, file_name, employee_residence):
    current_directory = Path.cwd()
    path = Path(path)
    path1 = current_directory/ path / file_name
    with open(path1, "wb") as fh:
        for key, value in employee_residence.items():
            line = str(key)+" " + str(value) +"\n"
            fh.write(line.encode())
    archive_name = shutil.make_archive(path / 'backup_folder', 'zip', path)


create_backup('path', 'employee_data.txt', {'John Doe': '123 Main St', 'Jane Smith': '456 Elm St'})