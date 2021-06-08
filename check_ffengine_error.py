import os
import pandas as pd

'''
error_type: Include mostly error keywords. if a error not in error_type, the error will be recorded in 'other_error.csv' file.
            If you find new error type in you jobs, and you don't want to see it in 'other_error.csv' file, you can add the error keyword to 'error_type'.
            When you add new errors, you should pay attention to adding the words and the symbol that is close to the keyword
job_type: all ffengine job types
'''
error_type = ["Exception:",'KeyError:','TypeError:','ZeroDivisionError:']
job_type = ['charge_fitting','conformation','intra_fitting','frag']


def count_error(path):
    charge_fitting_error = []
    conformation_error = []
    intra_fitting_error = []
    frag_error = []
    otrher_error = []

    folders = os.listdir(path)
    for folder in folders:
        sub_path = os.path.join(path,
                                folder)  # /zfs/AIRFLOW/logs/number_11-17_chengchengzhao_20210528101049/frag_FRSIMZWJVMLPAI-UHFFFAOYSA-N
        sub_folder = os.listdir(sub_path)
        if len(sub_folder) > 0:
            sub_foleder_1 = sub_folder[-1]
            path_end = os.path.join(sub_path,
                                    sub_foleder_1)  # frag_FRSIMZWJVMLPAI-UHFFFAOYSA-N/2021-05-28T02:10:49+08:00
            end_files = os.listdir(path_end)
            if len(end_files) == 4:
                file_path = os.path.join(path_end, end_files[-1])
                with open(file_path) as f:
                    lines = f.readlines()
                for line in lines:
                    flag = False
                    words = line.split()
                    for word in words:
                        if word in error_type:
                            if "charge_fitting" in folder:
                                charge_fitting_error.append([folder, line])
                                flag = True
                                break
                            elif "conformation_" in folder:
                                conformation_error.append([folder, line])
                                flag = True
                                break
                            elif "intra_fitting_" in folder:
                                intra_fitting_error.append([folder, line])
                                flag = True
                                break
                            else:
                                frag_error.append([folder, line])
                                flag = True
                                break
                    if flag:
                        break
                    if line == lines[-1]:
                        otrher_error.append([folder, line])

    if len(charge_fitting_error) > 0:
        dataframe = pd.DataFrame(charge_fitting_error)
        dataframe.to_csv('charge_fitting_error.csv', index=False, sep=',')
    if len(conformation_error) > 0:
        dataframe = pd.DataFrame(conformation_error)
        dataframe.to_csv('conformation_error.csv', index=False, sep=',')
    if len(intra_fitting_error) > 0:
        dataframe = pd.DataFrame(intra_fitting_error)
        dataframe.to_csv('intra_fitting_error.csv', index=False, sep=',')
    if len(frag_error) > 0:
        dataframe = pd.DataFrame(frag_error)
        dataframe.to_csv('frag_error.csv', index=False, sep=',')
    if len(otrher_error) > 0:
        dataframe = pd.DataFrame(otrher_error)
        dataframe.to_csv('otrher_error.csv', index=False, sep=',')



if __name__ == '__main__':

    '''
    the path is where your all '.log' files are located.
    '''
    path = '/zfs/AIRFLOW/logs/number_11-17_chengchengzhao_20210528101049'

    count_error(path)

