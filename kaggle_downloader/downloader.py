import os
import kaggle
import pandas as pd
from .utils import setup_argparse


def download_and_extract(dataset, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Downloading dataset: {dataset}")
    kaggle.api.dataset_download_files(dataset, path=output_dir, unzip=True)
    
    for file in os.listdir(output_dir):
        if file.endswith('.zip'):
            os.remove(os.path.join(output_dir, file))

def preview_csv(file_path):
    df = pd.read_csv(file_path)
    print(f"\nPreview of {os.path.basename(file_path)}:")
    print(df.head())
    print("\n" + "="*50 + "\n")

def main():
    parser = setup_argparse()
    args = parser.parse_args()

    try:
        download_and_extract(args.dataset, args.output)
        print(f"Files downloaded and extracted to: {args.output}")

        if args.preview:
            for file in os.listdir(args.output):
                if file.endswith('.csv'):
                    preview_csv(os.path.join(args.output, file))
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()