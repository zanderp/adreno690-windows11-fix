# GPU Fix for Adreno 690 unsuported display panel Windows 11 ARM

This project aims to fix the freezes caused by replacing the LCD panel on various laptops that use the Adreno680/690 graphics board since the windows provided driver is not 100% compatible. ( EG.: Samsung Galaxy Book GO 5G)
The application engages the GPU in the background by continuously running a minimal OpenGL task. It includes a system tray icon to indicate its status and allows you to exit the application from the tray menu.

## Features

- **Background GPU Task**: Runs a low-intensity OpenGL task to engage the GPU.
- **System Tray Icon**: Adds a system tray icon with a tooltip and an "Exit" option.
- **Executable Build**: Can be packaged into a standalone `.exe` using PyInstaller.
- **Automatic Builds with GitHub Actions**: Configured to build the executable on GitHub whenever changes are pushed.

## Prerequisites

- **Python 3.11** or compatible version.
- **Required Python Packages**:
  - Install dependencies with:
    ```bash
    pip install pyglet pystray pillow
    ```

## Usage

To run the script directly:

```bash
python gpu_try.py
```

### Running the Script in the Background

To run the script without opening a console window:

1. Use `pythonw`:
   ```bash
   pythonw gpu_try.py
   ```
2. Or package it as an executable (see below).

### Adding to Startup

If you want this application to start automatically on Windows boot:

1. **Batch File (For Startup Folder)**:
   - Create a batch file with the following content:
     ```batch
     @echo off
     start "" pythonw "C:\path\to\gpu_try.py"
     ```
   - Place this batch file in the Startup folder:
     - Press **Win + R**, type `shell:startup`, and press **Enter** to open the Startup folder.
     - Copy the batch file into this folder.

2. **Task Scheduler (For System Startup)**:
   - For pre-login startup, use Task Scheduler:
     - Open **Task Scheduler** > **Create Task**.
     - Set **Trigger** to **At startup**.
     - Set **Action** to **Start a Program** and use `pythonw` with the path to `gpu_try.py`.

## Packaging as an Executable

To build a standalone `.exe` file:

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Run PyInstaller with the following command:
   ```bash
   pyinstaller --noconsole --onefile --hidden-import=pystray --hidden-import=PIL gpu_try.py
   ```

   or include the full path as below

    ```bash
    "C:\Users\{user}\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\PyInstaller\__main__.py" --noconsole --onefile --hidden-import=pystray --hidden-import=PIL gpu_try.py
    ```

3. The executable will be created in the `dist` folder.

## Installing the Executable to Run at Startup

To make the application run automatically at Windows startup, you can either manually add it to the Startup folder or use the provided batch script.

### Method 1: Manual Installation

1. Press **Win + R**, type `shell:startup`, and press **Enter**. This opens the Startup folder.
2. Copy the `gpu_try.exe` file (located in the `dist` folder after building with PyInstaller) into this folder.

### Method 2: Automatic Installation with Batch Script

We’ve included a batch script named `install_startup.bat` to automate the setup.

1. Ensure the `gpu_try.exe` file is in the `dist` folder, in the same directory as `install_startup.bat`.
2. Double-click `install_startup.bat` to run it. The script will copy `gpu_try.exe` to the Startup folder.
3. After running, you should see a message confirming that the executable has been installed to startup.

### Verifying the Startup Entry

1. Open **Task Manager** by pressing **Ctrl + Shift + Esc**.
2. Go to the **Startup** tab and confirm that `gpu_try.exe` is listed and enabled.

Now, the application will automatically run in the background every time Windows starts.


## GitHub Actions Setup for Automated Builds

This project includes a GitHub Actions workflow to automatically build the executable on each push.

### Setting up GitHub Actions

1. In your repository, create the following file: `.github/workflows/build.yml`

2. Add the following configuration to `build.yml`:

   ```yaml
   name: Build Executable

   on:
     push:
       branches:
         - main
     pull_request:
       branches:
         - main

   jobs:
     build:
       runs-on: windows-latest

       steps:
         - name: Checkout code
           uses: actions/checkout@v2

         - name: Set up Python
           uses: actions/setup-python@v2
           with:
             python-version: '3.11'

         - name: Install dependencies
           run: |
             python -m pip install --upgrade pip
             pip install pyinstaller pystray pillow

         - name: Build executable with PyInstaller
           run: |
             pyinstaller --noconsole --onefile --hidden-import=pystray --hidden-import=PIL gpu_try.py

         - name: Upload executable as artifact
           uses: actions/upload-artifact@v2
           with:
             name: gpu_try_executable
             path: dist/gpu_try.exe
   ```

3. Commit and push this file to your repository.

4. On each push to `main`, GitHub Actions will build the executable and make it available under **Artifacts** in the Actions tab.

## Troubleshooting

- **Error with `pyinstaller` command**: Ensure `pyinstaller` is installed. If not recognized, try running it with:
  ```bash
  python -m PyInstaller ...
  ```

- **Executable Not Running as Background**: Ensure you’re using `pythonw` or the `--noconsole` option with PyInstaller.

## License

This project is licensed under the MIT License.
