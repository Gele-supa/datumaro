#!/usr/bin/env python3

import os

def main():
    # YOLO Dataset Merge Script in Python
    # This script provides customized commands to create Datumaro projects, import YOLO datasets,
    # merge them, and export the merged dataset in YOLO format.

    # Step 1: Collect Information from the User
    print("\nStep 1: Collect Dataset Information")
    yolo_data1 = input("Enter the path to the first YOLO dataset directory: ")
    project1 = input("Enter a name for the Datumaro project for the first dataset (e.g., drones_project): ")

    yolo_data2 = input("Enter the path to the second YOLO dataset directory: ")
    project2 = input("Enter a name for the Datumaro project for the second dataset (e.g., valentines_chocolates_project): ")

    merged_project = input("Enter a name for the merged Datumaro project (e.g., merged_yolo_project): ")
    exported_yolo = input("Enter a directory name for exporting the merged dataset in YOLO format (e.g., exported_yolo_dataset): ")

    # Step 2: Instructions to Initialize Datumaro Projects
    print("\nStep 2: Initialize Datumaro Projects")
    print("You need to initialize separate Datumaro projects for each dataset before importing data.")
    print(f"Use the following commands to create the projects:")
    print(f"datum project create -o {project1}")
    print(f"datum project create -o {project2}")

    # Step 3: Import YOLO Datasets into Datumaro Projects
    print("\nStep 3: Import YOLO Datasets into Datumaro Projects")
    import_command1 = f"datum source add -f yolo {yolo_data1} -p {project1} -n source_{project1}"
    import_command2 = f"datum source add -f yolo {yolo_data2} -p {project2} -n source_{project2}"
    print(f"To import the YOLO datasets, use the following commands:\n{import_command1}\n{import_command2}")

    # Step 4: Merge YOLO Projects
    print("\nStep 4: Merge YOLO Projects")
    merge_command = f"datum merge --output-dir {merged_project} {project1} {project2}"

    # Optional: Customize Merge Parameters
    customize_merge = input("Would you like to specify custom merge parameters (y/n)? ")
    if customize_merge.lower() == "y":
        merge_policy = input("Enter merge policy (e.g., union, intersect): ")
        iou_threshold = input("Enter IoU threshold (e.g., 0.6): ")
        groups = input("Enter groups (e.g., 'class1,class2,...'): ")
        merge_command = (
            f"datum merge --output-dir {merged_project} --merge-policy {merge_policy} "
            f"--iou {iou_threshold} --groups '{groups}' {project1} {project2} -- --save-media"
        )
    else:
        merge_command += " -- --save-media"

    print(f"\nTo merge the projects, use the following command:\n{merge_command}")

    # Step 5: Export the Merged Project to YOLO Format
    print("\nStep 5: Export the Merged Project to YOLO Format")
    export_command = (
        f"datum convert -i {merged_project} --output-format yolo -o {exported_yolo} "
        f"-- --save-media "
    )
    print(f"To export the merged project to YOLO format, use the following command:\n{export_command}")

    # Instructions to the user
    print("\nYou have successfully generated the commands to merge your YOLO datasets.")
    print("Use the commands above as a reference to replace directories with your own datasets in future workflows.")

if __name__ == "__main__":
    main()
