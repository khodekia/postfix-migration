
# Postfix Migration

This repository contains a Python script to assist in migrating email data from MDaemon to Postfix. The script processes directories of email files, removes empty files, and modifies IMAP files to prepare them for import into the Postfix mail system.

## Features

- Removes all empty files from the specified directory
- Removes all non-`.msg` files from the specified directory
- Modifies IMAP files to ensure proper content formatting
- Imports emails into the Postfix mail system

## Usage

To use the script, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/khodekia/postfix-migration.git
    cd postfix-migration
    ```

2. Run the script:
    ```bash
    python migrate.mdeamon.py /path/to/directory
    ```

    **Note:** The script will prompt for confirmation before removing files and modifying IMAP files.

## Script Details

The main script, `migrate.mdeamon.py`, performs the following tasks:

- Checks the provided directory for empty files and removes them.
- Removes all files except `.msg` files in the specified directory.
- Modifies IMAP files to ensure proper formatting.
- Uses `zmmailbox` to create folders and add messages to the Postfix mail system.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, please open an issue in this repository.

---

You can now add this content to a `README.md` file in your repository. Let me know if you need any further changes or assistance!
