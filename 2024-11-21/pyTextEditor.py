import os

class CommandLineEditor:
    def __init__(self):
        self.content = []
        self.filename = None

    def run(self):
        print("Welcome to the Command pyTextEditor")
        print("Type '?save' to save the file, '?exit' to exit.")
        while True:
            command = input("")
            if command == "?exit":
                break
            elif command == "?save":
                self.save_file()
            else:
                self.insert_text(command)

    def insert_text(self, text):
        # 将输入的文本添加到内容中，这里简单处理，实际可以更复杂
        self.content.append(text)

    def save_file(self):
        if self.filename is None:
            self.filename = input("Enter filename to save: ")
        with open(self.filename, 'w') as file:
            file.write("\n".join(self.content))
        print(f"File saved as {self.filename}")

if __name__ == "__main__":
    editor = CommandLineEditor()
    editor.run()
