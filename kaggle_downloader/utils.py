import argparse

def setup_argparse():
    parser = argparse.ArgumentParser(description="Download Kaggle dataset files")
    parser.add_argument("dataset", help="Kaggle dataset in the format 'owner/dataset-name'")
    parser.add_argument("-o", "--output", default="./dataset_files", help="Output directory for downloaded files")
    parser.add_argument("-p", "--preview", action="store_true", help="Preview the first few rows of each CSV")
    return parser

def validate_dataset_name(dataset_name):
    if '/' not in dataset_name or len(dataset_name.split('/')) != 2:
        raise ValueError("Invalid dataset name. Format should be 'owner/dataset-name'")
    return dataset_name
