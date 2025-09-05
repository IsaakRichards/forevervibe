import subprocess
import sys

def install_and_import(package):
    """
    Checks if a Python module is installed and if not, installs it.
    
    Args:
        package (str): The name of the package to install.
    """
    try:
        # Attempt to import the package
        __import__(package)
        print(f"'{package}' is already installed.")
    except ImportError:
        print(f"'{package}' not found. Installing now...")
        try:
            # Use a subprocess to run the pip install command
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"Successfully installed '{package}'.")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while installing '{package}': {e}")
            print("Please try running the script with administrator/superuser privileges if the issue persists.")
    

