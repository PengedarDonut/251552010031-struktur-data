class Undo_Redo:
    def __init__(self):
        self.contents = ""
        self.undo_stack = []

    def write(self, teks):
        self.undo_stack.append(self.contents)
        self.contents += teks

    def undo(self):
        if len(self.undo_stack) > 0:
            self.contents = self.undo_stack.pop()
            self.contents = self.contents

            print("Undo berhasil. Konten saat ini:", self.contents)
        else:
            print("Tidak ada aksi untuk di-undo.")

        self._lihat_konten()

    def _lihat_konten(self):
        print(f"   [ Teks Aktif  ] : '{self.contents}'")
        print(f"   [ Undo Stack  ] : {self.undo_stack}")
        print("-" * 50)


# Simulasi penggunaan

editor = Undo_Redo()
editor.write("Hello, ")
editor.write("world!")
editor.write(" This is a simple undo-redo system.")

editor.undo()  # Menghapus " This is a simple undo-redo system."
editor.undo()  # Menghapus "world!"
editor.undo()  # Menghapus "Hello, "
editor.undo()  # Tidak ada aksi untuk di-undo
