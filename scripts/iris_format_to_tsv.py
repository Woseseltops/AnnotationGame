import os

def iris_format_to_tsv(source_folder_path,goal_file_path,labels_for_classes):

    goalfile = open(goal_file_path,'w')

    for filename in os.listdir(source_folder_path):

        file_content = open(source_folder_path + filename).read().replace('\n',' ')
        annotated_class = filename.split('_')[0]

        goalfile.write(file_content+'\t'+str(labels_for_classes[annotated_class])+'\n')

if __name__ == '__main__':

    SOURCE_FOLDER_PATH = '/home/wessel/Downloads/Prep/'
    GOAL_FILE_PATH = 'stimuli.txt' #Just put it next to the script
    LABELS_FOR_CLASSES = {'dream':1,"reddit":2,"prosebox":2}

    iris_format_to_tsv(SOURCE_FOLDER_PATH,GOAL_FILE_PATH,LABELS_FOR_CLASSES)