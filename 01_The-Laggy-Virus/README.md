# The Laggy Virus
The Laggy Virus is my first Python homemade virus. It is **not** destructive by itself tho it opens some malicious content with the webbrowser module.

## How does it strike?
This virus strikes by causing tons of lag into the computer, by just simply opening infinite instances of Windows File Explorer and Windows Settings App (the Metro one - not the Control Panel) and opening more than 20000 malware websites (I took the list from a GitHub repo - you can go look it yourself).

It also opens some random pop-ups and minimizes every app you open, so don't even try to call the Task Manager.

Truly xD...

## Requirements
The only non-standard module required to run this code is *pyautogui*.