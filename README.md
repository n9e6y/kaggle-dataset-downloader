# Kaggle Dataset Downloader

Kaggle Dataset Downloader is a simple Python tool that simplifies the process of downloading and previewing Kaggle datasets. It provides a command-line interface for easy dataset retrieval and preview.

## Project Structure

```
kaggle-dataset-downloader/
├── kaggle_downloader/
│   ├── __init__.py
│   ├── downloader.py
│   └── utils.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Features

- Download Kaggle datasets with a simple command
- Automatically extract downloaded files
- Preview CSV files in the dataset
- Utility functions for dataset handling

## Prerequisites

Before using Kaggle Dataset Downloader, ensure you have:

1. Python 3.7 or higher installed
2. Kaggle API credentials set up (instructions in the [Kaggle API documentation](https://github.com/Kaggle/kaggle-api#api-credentials))

## Installation

1. Clone this repository:
   ```
   gh repo clone n9e6y/kaggle-dataset-downloader
   cd kaggle-dataset-downloader
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To use the Kaggle Dataset Downloader, run this script with Python:

```
python -m kaggle_downloader/downloader owner/dataset-name [options]
```

Options:
- `-o`, `--output`: Specify the output directory (default: `./dataset_files`)
- `-p`, `--preview`: Preview the first few rows of each CSV file in the dataset


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to Kaggle for providing the API that makes this tool possible.
- Inspired by the data science community's need for streamlined dataset access.

## Contact

If you have any questions or feedback, please open an issue on this GitHub repository.