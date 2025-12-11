# CODECRAFT_CS_01

🔐 Caesar Cipher – Encryption & Decryption (GUI Application)

This project is a simple yet effective Caesar Cipher Encryption & Decryption Tool built using Python and Tkinter.
It allows users to encrypt and decrypt messages using a shift-based substitution cipher, one of the earliest and simplest encryption techniques.

The GUI makes the tool easy to use for beginners and is perfect for learning basic cryptography concepts.

🚀 Features

✔ User-friendly GUI built using Tkinter & ttk
✔ Supports Encryption and Decryption
✔ Accepts custom shift value
✔ Handles uppercase, lowercase, and non-alphabet characters
✔ Clean output display
✔ Input validation with proper error handling
✔ Clear button to reset all fields
✔ Exit button included
✔ Lightweight and easy to run


📂 Project Structure
Caesar-Cipher-GUI/
│
├── main.py              # Main application code
├── README.md            # Documentation
└── screenshot.png       # App screenshot (optional)

🧠 How the Caesar Cipher Works

The Caesar Cipher shifts each alphabetic character by a fixed number (shift value):

Encryption:
EncryptedChar = (OriginalChar + Shift) % 26

Decryption:
DecryptedChar = (OriginalChar - Shift) % 26

Non-alphabet characters (numbers, symbols, spaces) remain unchanged.

Example:
Shift = 3
HELLO → KHOOR

🛠️ Technologies Used

Python 3

Tkinter (GUI)

ttk Widgets

Built-in libraries only — no external dependencies

📥 Installation & Running the Application
1️⃣ Clone the repository
git clone https://github.com/yourusername/Caesar-Cipher-GUI.git

2️⃣ Navigate to project folder
cd Caesar-Cipher-GUI

3️⃣ Run the application
python main.py


That's it — the GUI will open instantly!

🎮 How to Use

Enter the message in the input box

Enter a shift value (an integer)

Click:

Encrypt → to convert plaintext into ciphertext

Decrypt → to reverse ciphertext into plaintext

View results in the output box

Press Clear to reset all fields

Press Exit to close the application

📌 Code Overview
🔹 caesar_encrypt()

Handles encryption by shifting characters forward.

🔹 caesar_decrypt()

Handles decryption by shifting characters backward.

🔹 encrypt_text() / decrypt_text()

Connects GUI buttons with cipher logic.

🔹 Tkinter GUI

Includes:

Text fields

Buttons

LabelFrames

Clean layout with ttk styling

🔧 Future Enhancements (Optional section)

You can extend this project by adding:

Brute-force decryption (auto shift finder)

Dark mode UI

CustomTkinter modern GUI

Rotating shift wheel animation

Hacker-style theme

Export encrypted text to a file

Vigenère cipher support

🤝 Contributing

Pull requests are welcome!
Feel free to open issues for improvements or bugs.

📜 License

This project is open source and available under the MIT License.
