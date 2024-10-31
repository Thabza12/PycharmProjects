import os
# from Augmentation import Augmentation


class ProcessFile:

    def __init__(self, source_folder, target_folder):
        self.source_folder = source_folder
        self.target_folder = target_folder

    def process(self):
        try:
            for path, dir, files in os.walk(self.source_folder):
                if files:
                    for file in files:
                        print(file)
                        # if not os.path.isfile(self.target_folder + file):
                        # os.rename(path + '\\' + file, self.target_folder + file)

            print("files transferred")
        except Exception as e:
            print(e)


image_annotation = ProcessFile(
    source_folder=r'C:\Users\SaneleCele-PurpleWir\PycharmProjects\process_files\Image_Annotations' + '\\',
    target_folder=r'C:\Users\SaneleCele-PurpleWir\PycharmProjects\process_files\processed' + '\\processed')

image_files = ProcessFile(
    source_folder=r'C:\Users\SaneleCele-PurpleWir\PycharmProjects\process_files\dataset' + '\\',
    target_folder=r'C:\Users\SaneleCele-PurpleWir\PycharmProjects\process_files\processed' + '\\processed'
)

ProcessFile.process(image_annotation)
ProcessFile.process(image_files)
