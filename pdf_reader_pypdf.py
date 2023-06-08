# This pdf reader reads Arabic properly but has problems when both RTL and LTR languages exist
# pypdf==3.4.1
from pypdf import PdfReader

reader = PdfReader("/mnt/D/Upwork/Ali-UAE/shared_folder_reader/sample_files/sample-arabic.pdf")
full_text = ""
for page in reader.pages:
    full_text += page.extract_text() + "\n"
print(full_text)

with open('/mnt/D/Upwork/Ali-UAE/shared_folder_reader/arabicpdfreaderout.txt', 'w+') as f:
    f.writelines(full_text)

