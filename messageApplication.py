from tkinter import *
from customtkinter import *

def binary(number: int) -> str:
    return bin(number)[2:]

def binary_to_decimal(binary: str) -> int:
    return int(binary, 2)
class MessageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Message Encryption and Decryption")
        self.root.geometry("650x480+400+100")
        self.root.config(bg="misty rose")
        self.root.resizable(False, False)


        set_appearance_mode("light")
        set_default_color_theme("blue")


        info = CTkLabel(root, text="Look at terminal to show encrypted code", font=("arial", 20, "bold"), text_color="deep sky blue")
        info.place(x=160, y=5)
        self.__create_frames()
        self.__create_buttons()


    def __create_frames(self):

        self._frame1 = Frame(self.root, bg="silver", width=300, height=400, relief=RIDGE,
                             highlightbackground="gray63", highlightthickness=5)
        self._frame1.grid(row=0, column=0, padx=25, pady=50)


        self._frame2 = Frame(self.root, bg="silver", width=300, height=400, relief=RIDGE,
                             highlightbackground="gray63", highlightthickness=5)
        self._frame2.grid(row=0, column=1, padx=25, pady=50)


        self._textbox_frame1_1 = CTkTextbox(self._frame1, width=250, height=100)
        self._textbox_frame1_1.pack(padx=10, pady=10)

        self._textbox_frame1_2 = CTkTextbox(self._frame1, width=250, height=100)
        self._textbox_frame1_2.pack(padx=10, pady=10)
        self._textbox_frame1_2.configure(state=DISABLED)

        user1 = CTkLabel(self._frame1, text="User-1", font=("arial", 16, "bold"), text_color="blue")
        user1.pack()


        self._textbox_frame2_1 = CTkTextbox(self._frame2, width=250, height=100)
        self._textbox_frame2_1.pack(padx=10, pady=10)

        self._textbox_frame2_2 = CTkTextbox(self._frame2, width=250, height=100)
        self._textbox_frame2_2.pack(padx=10, pady=10)
        self._textbox_frame2_2.configure(state=DISABLED)

        user2 = CTkLabel(self._frame2, text="User-2", font=("arial", 16, "bold"), text_color="blue")
        user2.pack()

    def __create_buttons(self):
        button_frame1 = CTkButton(self._frame1, text="Send", command=self.__send_from_frame1)
        button_frame1.pack(pady=10)

        button_frame2 = CTkButton(self._frame2, text="Send", command=self.__send_from_frame2)
        button_frame2.pack(pady=10)

        clear = CTkButton(self.root, text="Clear", command=self.__clear)
        clear.grid(row=1, column=0)

        close = CTkButton(self.root, text="Close", command=self.__close)
        close.grid(row=1, column=1)

    def __encrypt(self, message: str) -> list:
        message = message[::-1]
        encrypted_message = []
        for i in message:
            encrypted_message.append(binary(ord(i)))
        return encrypted_message

    def __decrypt(self, message: list) -> str:
        decrypted_message = ""
        for i in message:
            decrypted_message += chr(binary_to_decimal(i))
        decrypted_message = decrypted_message[::-1]
        return decrypted_message

    def __send_from_frame1(self):
        message = self._textbox_frame1_1.get("0.0", END).strip()
        if message:
            encrypted_message = self.__encrypt(message)
            print("from user-1 : ", end="")
            for i in encrypted_message:
                print(i, end="")
            print()
            decrypted_message = self.__decrypt(encrypted_message)
            self._textbox_frame2_2.configure(state=NORMAL)
            current_text = self._textbox_frame2_2.get("0.0", END)
            self._textbox_frame2_2.delete("0.0", END)
            self._textbox_frame2_2.insert("0.0", current_text + decrypted_message + "\n\n")
            self._textbox_frame2_2.configure(state=DISABLED)
            self._textbox_frame1_1.delete("0.0", END)
            return decrypted_message

    def __send_from_frame2(self):
        message = self._textbox_frame2_1.get("0.0", END).strip()
        if message:
            encrypted_message = self.__encrypt(message)
            print("from user-2 : ", end="")
            for i in encrypted_message:
                print(i, end="")
            print()
            decrypted_message = self.__decrypt(encrypted_message)
            self._textbox_frame1_2.configure(state=NORMAL)
            current_text = self._textbox_frame1_2.get("0.0", END)
            self._textbox_frame1_2.delete("0.0", END)
            self._textbox_frame1_2.insert("0.0", current_text + decrypted_message + "\n\n")
            self._textbox_frame1_2.configure(state=DISABLED)
            self._textbox_frame2_1.delete("0.0", END)

    def __clear(self):
        self._textbox_frame1_2.configure(state=NORMAL)
        self._textbox_frame2_2.configure(state=NORMAL)
        self._textbox_frame1_1.delete("0.0", END)
        self._textbox_frame2_1.delete("0.0", END)
        self._textbox_frame1_2.delete("0.0", END)
        self._textbox_frame2_2.delete("0.0", END)
        self._textbox_frame1_2.configure(state=DISABLED)
        self._textbox_frame2_2.configure(state=DISABLED)

    def __close(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    app = MessageApp(root)
    root.mainloop()
