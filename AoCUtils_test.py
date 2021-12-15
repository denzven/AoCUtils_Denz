import AoCUtilsDenz as AocUtils
import time
import os

from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)


StartTime = time.time()
AocUtils.BoilerPlate(os.environ['SessionID'])
EndTime = time.time()
print(f"Execution time: {EndTime - StartTime}")
