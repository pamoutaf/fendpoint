# fendpoint
Find endpoints in files

## Description:
This tool can be used to search for potential endpoints in a JavaScript file, usually retrieved using Chrome DevTools.

### Steps to retrieve a JavaScript or html file:
1. Open Chrome and navigate to the target website.
2. Right-click anywhere on the page and select **Inspect**.
3. Go to the **Sources** tab.
4. Click on the JavaScript file (e.g., `index.js`, `script.js`, etc.).
5. Right-click the file and choose **Open in New Tab**.
6. Copy and paste the content of the file into a new file on your machine.

### Example Usage:
```sh
python fendpoint.py -f p0pcycle_javascript.txt
```


