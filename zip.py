import os
import zipfile
import argparse

def zip_directory(directory_path, zip_path):
    """将目录压缩为 ZIP 文件"""
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, directory_path)
                zipf.write(file_path, arcname)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="压缩指定文件夹为 zip 文件")
    parser.add_argument("-s", "--folder", help="需要压缩的文件夹路径")
    parser.add_argument("-t", "--zipfile", help="目标压缩文件（.zip）路径")
    args = parser.parse_args()

    zip_directory(args.folder, args.zipfile)