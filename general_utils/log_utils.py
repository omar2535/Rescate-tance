import os


def do_rollover(max_logfiles_to_keep: int, orig_file_name: str) -> None:
    """Performs log rotations
    main.log -> main-1.log
    main-1.log -> main-2.log
    main-2.log -> main-3.log
    ...
    main-10.log gets deleted

    Args:
        max_logfiles_to_keep (int): Maximum number of logfiles to keep
        orig_file_name (str): Log file name
    """
    file_extension = orig_file_name.split(".")[-1]
    file_path_without_extension = "".join(orig_file_name.split(".")[0:-1])
    for index in range(max_logfiles_to_keep, -1, -1):
        cur_file_name = f"{file_path_without_extension}-{index}.{file_extension}"
        if index == 10 and os.path.isfile(cur_file_name):
            os.remove(cur_file_name)
            continue
        elif index == 0 and os.path.isfile(orig_file_name):
            new_file_name = f"{file_path_without_extension}-{index+1}.{file_extension}"
            os.rename(orig_file_name, new_file_name)
        elif os.path.isfile(cur_file_name):
            new_file_name = f"{file_path_without_extension}-{index+1}.{file_extension}"
            os.rename(cur_file_name, new_file_name)
