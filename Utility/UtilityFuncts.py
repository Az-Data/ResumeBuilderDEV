
import os
import datetime
import pytz


# relevant folder paths
Resume_components_folder_path = 'Resume Components'
jobAd_path = 'Job Ads/New Ad'
Output_folder_path = "Output"


def empty_Resume_Components_and_Output_folder():
    """
    deleting all the files and folders in the Resume Components folder and Ouput folder
    """

    # Get a list of all subdirectories in the folder
    Resume_Components_dir = [d for d in os.listdir(Resume_components_folder_path) if os.path.isdir(os.path.join(Resume_components_folder_path, d))]

    print("Emptying Resume Components")
    for subdir in Resume_Components_dir:
        # get the list of files from that directory
        file_list = os.listdir(os.path.join(Resume_components_folder_path, subdir))

        # Delete each file
        for file_name in file_list:
            file_path = os.path.join(Resume_components_folder_path, subdir, file_name)
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        
        folder_path = os.path.join(Resume_components_folder_path, subdir)
        os.rmdir(folder_path)
        print(f"Deleted folder: {folder_path}")
    
    Output_dir = [d for d in os.listdir(Output_folder_path) if os.path.isdir(os.path.join(Output_folder_path, d))]

    print("Emptying Ouput folder")
    for subdir in Output_dir:
        # get the list of files from that directory
        file_list = os.listdir(os.path.join(Output_folder_path, subdir))

        # Delete each file
        for file_name in file_list:
            file_path = os.path.join(Output_folder_path, subdir, file_name)
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        
        folder_path = os.path.join(Output_folder_path, subdir)
        os.rmdir(folder_path)
        print(f"Deleted folder: {folder_path}")



def create_job_folders():
    """
    Create a folder for each job ad in the Job Ads Folder and also in the Outputs folder
    """

    # Get the Sydney timezone
    sydney_timezone = pytz.timezone('Australia/Sydney')

    # Get the current local time and date
    current_dt = datetime.datetime.now(sydney_timezone)

    formatted_dt = current_dt.strftime("%Y-%m-%d_%H-%M-%S")

    # Print the current local time and date

    file_list = [file for file in os.listdir(jobAd_path) if file.endswith('.txt')]

    folder_prefix = [filename.split(".", 1)[0] for filename in file_list]

    for fp in folder_prefix:
        os.makedirs('/'.join([Resume_components_folder_path, fp + "_" + formatted_dt]))
        os.makedirs('/'.join([Output_folder_path, fp + "_" + formatted_dt]))


def obtain_ad_folder_dict():
    """
    gets a dictionary of {ad_file : ad_folder}
    """
    file_list = [file for file in os.listdir(jobAd_path) if file.endswith('.txt')]

    folder_prefix = [filename.split(".", 1)[0] for filename in file_list]

    # Get a list of all subdirectories in the folder
    subdirectories = [d for d in os.listdir(Resume_components_folder_path) if os.path.isdir(os.path.join(Resume_components_folder_path, d))]

    ad_folder_dict = {}

    for fp in folder_prefix:
        matching_list = [string for string in subdirectories if fp in string]
        ad_folder_dict[".".join([fp, 'txt'])] = matching_list[0]
    
    return ad_folder_dict

