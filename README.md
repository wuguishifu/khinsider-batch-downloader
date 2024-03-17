# Khinsider Batch Downloader

## How to use

1. Clone the GitHub repository using the following command

    ```bash
    git clone https://github.com/wuguishifu/khinsider-batch-downloader
    ```

2. Open a terminal and navigate to the project root directory

    ```bash
    cd khinsider-batch-downloader
    ```

3. Install the dependencies. You will need Beautifulsoup4 and Requests

    ```bash
    pip install requests beautifulsoup4
    ```

4. Run the main script. It will prompt you to enter a directory name to save the files (within this project's root folder) and the link to the Khinsider album page.

    ```bash
    python script.py
    Enter the directory to save the files: <enter your directory>
    Enter the URL of the album: <enter the Khinsider album URL>
    ```

5. The files will be downloaded to the specified directory.

## Renaming Files (for Plex or other media servers)

1. Navigate to the project root directory

    ```bash
    cd khinsider-batch-downloader
    ```

2. Depending on the filename format of the current files, you may have to modify `rename.py` to fit your needs. By default, it replaces the first instance of "." with " -". This converts names like "1. Title Theme" to "1 - Title Theme".

3. Run the rename script. It will prompt you to enter the directory name in which the files are located.

    ```bash
    python rename.py
    ```
