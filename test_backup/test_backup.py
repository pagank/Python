import os
import os.path

class FileBackup(object):
    """ text file back up """

    def __init__(self, src, dist):

        self.src = src
        self.dist = dist

    def read_files(self):
        """ raed files from src directory """

        ls = os.listdir(self.src)
        #print(ls)
        for f in ls:
            self.backup_file(f)

    def backup_file(self, file_name):
        """ processing backup file """
        if not os.path.exists(self.dist):
            print("Directories not found. Creating directories...")
            os.makedirs(self.dist)
            print("Directories created !")

        full_src_path = os.path.join(self.src, file_name)
        full_dist_path = os.path.join(self.dist, file_name)

        if os.path.isfile(full_src_path) and os.path.splitext(full_src_path)[-1].lower() == ".txt":
            print(">>> Backing up '{0}' !".format(file_name))
            with open(full_dist_path, "w", encoding="utf-8") as f_dist:
                with open(full_src_path, "r", encoding="utf-8") as f_src:
                    while True:
                        result = f_src.read(100)
                        if not result:
                            break
                        f_dist.write(result)
                    f_dist.flush()
                print("Finished Back up '{0}' >>>".format(file_name))

        else:
            print("'{0}' is not text file, skip ---".format(file_name))


if __name__ == "__main__":
    # src_path = "C:\\Users\\zeqianliu\\Documents\\python\\test_backup\\src"
    # dist_path = "C:\\Users\\zeqianliu\\Documents\\python\\test_backup\\dist"
    dir_path = os.path.dirname(os.path.abspath(__file__))
    # print(dir_path)
    src_path = os.path.join(dir_path, "src")
    dist_path = os.path.join(dir_path, "dist")

    bak = FileBackup(src_path, dist_path)
    bak.read_files()