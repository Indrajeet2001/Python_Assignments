
class BookStore:
    NoOfBooks = 0

    def __init__(self, A, B):
        self.Name = A
        self.Author = B
        BookStore.NoOfBooks += 1

    def Display(self):
        print("Name is : ",self.Name)
        print("Author is : ",self.Author)
        print("No of Books are : ",BookStore.NoOfBooks)

def main():
    
    Obj1 = BookStore("Linux System Programming", "Robert Love")

    Obj1.Display()

    Obj2 = BookStore("C Programming", "Dennis Ritchie")

    Obj2.Display()

if __name__ == "__main__":
    main()