Certainly! Here's the same content formatted for Notion, using a structure that works well in Notion’s markdown-style editor:

---

# Microsoft Edge Automation Script

This script automates some actions using Microsoft Edge and Google searches. It takes email and password pairs from a `data.json` file, opens the Edge browser, logs in to Bing Rewards, and performs Google searches.

---

## Important Notes (Please Read Carefully!)

### **Warning**
Once the steps below are completed, **you will not be able to save your site settings in Microsoft Edge**. This is due to enabling the **Clear site data on close** feature. Please ensure that you are okay with losing your browsing data each time the browser is closed.

### **How to Enable "Clear site data on close" in Microsoft Edge**
1. Open **Microsoft Edge**.
2. Click the **three-dot menu** in the upper-right corner of the browser window and select **Settings**.
3. Under **Privacy, search, and services**, scroll down to the **Clear browsing data** section.
4. Click on **Choose what to clear every time you close the browser**.
5. Toggle **Cookies and other site data** to **On**.
6. Once this is done, **you will lose all your site data upon closing the browser**.

After completing the steps above, proceed with the setup and usage of the automation script.

---

## Setup

### 1. Clone the Repository

```
git clone https://github.com/yourusername/repository-name.git
cd repository-name
```

### 2. Install Dependencies

Ensure you have Python installed on your system. You will also need to install the required packages. You can do this by running:

```
pip install -r requirements.txt
```

### 3. Create and Configure `data.json`

The script reads from a `data.json` file for the login credentials. This file must be structured like the following:

```json
[
  {
    "email": "your-email@example.com",
    "password": "yourpassword"
  }
]
```

#### **Important:** Ensure that the account entered in `data.json` is already created on Microsoft and that **two-factor authentication is disabled**. This script does not support accounts with two-factor authentication enabled.

### 4. Run the Script

Once the dependencies are installed and `data.json` is configured, you can run the script:

```
python stript.py
```

This will launch Microsoft Edge, log into Bing Rewards, and perform the necessary actions as defined in the script.

---

## Script Functionality

### 1. **Loading Data from JSON**
The script loads the `data.json` file to get the list of email/password pairs for login.

### 2. **Login to Microsoft Edge**
The script will:
- Open Microsoft Edge using the subprocess module.
- Navigate to the Bing Rewards login page.
- Enter the email and password from `data.json`.
- Perform some Google searches.

### 3. **Performing Google Searches**
The script will:
- Generate a random search term.
- Open Google and search using the generated random string.
- Repeat this process for a total of 9 searches.

---

## `requirements.txt`

The list of dependencies you need to include in your `requirements.txt` file.

---

## Troubleshooting

- **Issue:** The script doesn't launch Microsoft Edge.
  - **Solution:** Ensure you have Microsoft Edge installed and that the command to launch it (`subprocess.run(["start", "msedge", "--in", "https://rewards.bing.com/welcome"], shell=True)`) works in your terminal.

- **Issue:** The coordinates are incorrect or out of range.
  - **Solution:** The script includes a coordinate scaling function (`scale_coordinates`) to adjust for different screen resolutions. If your screen resolution is vastly different from the base resolution (1366x768), you may need to adjust the coordinates.

---

## License

MIT License

---

### Happy automating!

---
