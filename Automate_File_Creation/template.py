import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(levelname)-s %(message)s')
logger = logging.getLogger(__name__)

projectName = "rocketScience"
list_of_files = [
    
    f"src/{projectName}/__init__.py",
    f"src/{projectName}/models/models.py",
    f"src/{projectName}/database/database.py",
    f"src/{projectName}/models/__init__.py",
    f"src/{projectName}/database/__init__.py",
    f"src/{projectName}/app.py",
    f"src/{projectName}/logger.py",
    "requirements.txt",
    "setup.py",
    
]
for files in list_of_files:
    filepath = Path(files)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        
    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating Empty Directory: {filepath}")
        
    else:
        logging.info(f"{filename} already exists")
    