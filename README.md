# python_automation
Learning Python Automation from "FreeCodeCamp" video:
- Youtube Link: [!https://www.youtube.com/watch?v=PXMJ6FS7llk](https://www.youtube.com/watch?v=PXMJ6FS7llk)

## Project 1: Basic Table Extraction
1. Extracting tables from wikipedia.
2. Extracting tables from PDF files.

## Project 2: XPATH and Selenium
1. Install the python package "pyinstaller" to making executable python files:
```bash
pip install pyinstaller
```
2. Converting ".py" file into ".exe":
```bash
pyinstaller --onefile --add-binary "/usr/lib/x86_64-linux-gnu/libcrypto.so.3:." --add-binary "/usr/lib/x86_64-linux-gnu/libssl.so.3:." news-headlines-script.py
```
3. Making a cron job using the following commands:
```bash
crontab -e
```
4. Setting date & time to the cron job using the following syntax:
```text
# time formate 24-hour
# m h dom mon dow   command
53 22 * * * /home/<username>/python_code/python_automation/project_2/dist/news-headlines-script
```
5. For testing crontab scheduling date & time using [CrontabGuru](https://crontab.guru/).

## Project 3: Automate Excel Report
The following the order of the files:
```text
1. pivot-table.py
2. add-chart.py
3. apply-formula.py
4. formate.py
5. pivot-to-report.py
6. automate-excel.py
```

- Converting ".py" file into ".exe":
```bash
pyinstaller --onefile --add-binary "/usr/lib/x86_64-linux-gnu/libcrypto.so.3:." --add-binary "/usr/lib/x86_64-linux-gnu/libssl.so.3:." automate-excel.py
```

## Project 4: Whatsapp Automation
