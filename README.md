# 🔥 FireSpy

**FireSpy** is a lightweight Python tool designed to audit Firebase Realtime Database security settings. It performs unauthorized access checks and reports misconfigurations related to read/write permissions.

---

## 🧰 Features

- 🚫 Unauthenticated **Read** Test  
- ✍️ Unauthenticated **Write** Test  
- 🔐 Authenticated **Write** Test (optional token)  
- ❌ Invalid Token Write Test  
- 🕵️ Basic Path Traversal Attempt  

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.x
- `requests` module:
```bash
pip install requests
```
▶️ Usage
Run the script : python firespy.py

Enter when prompted:

Your Firebase URL (e.g. https://your-project.firebaseio.com)
Optional Auth Key (leave blank to skip)

🧪 Example

=== Firebase Realtime Database Security Tester ===
Enter the Firebase Realtime Database URL (without `.json`): https://example.firebaseio.com
Enter Auth Key (optional - press Enter to skip):


⚠️ Legal Notice
FireSpy is meant for educational and authorized use only.
Never test any system without proper permission. Misuse of this tool may violate laws and ethical guidelines.


👤 Author
Name: Sandeep Saini

GitHub: saini01sandeep


🧹 Cleanup Reminder
The tool writes a test record:

"security_test": {
  "message": "test is done",
  "timestamp": "2023-11-15T12:00:00Z",
  "test_id": "delete_me_after_testing"
}

Please remove this entry from your Firebase database after testing.
