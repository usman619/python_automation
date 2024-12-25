# python_automation
Learning Python Automation from "FreeCodeCamp" video:
- Youtube Link: [!https://www.youtube.com/watch?v=PXMJ6FS7llk](https://www.youtube.com/watch?v=PXMJ6FS7llk)
## Project 1: Basic Table Extraction
- Extracting tables from wikipedia.
- Extracting tables from PDF files.
## Project 2: XPATH and Selenium
- Install the python package "pyinstaller" to making executable python files:
```bash
pip install pyinstaller
```
- Converting ".py" file into ".exe":
```bash
pyinstaller --onefile --add-binary "/usr/lib/x86_64-linux-gnu/libcrypto.so.3:." --add-binary "/usr/lib/x86_64-linux-gnu/libssl.so.3:." news-headlines-script.py
```
- Making a cron job using the following commands:
```bash
crontab -e
```
- Setting date & time to the cron job using the following syntax:
```text
# time formate 24-hour
# m h dom mon dow   command
53 22 * * * /home/username/python_code/python_automation/project_2/dist/news-headlines-script
```
- For testing crontab scheduling date & time using [CrontabGuru](https://crontab.guru/).