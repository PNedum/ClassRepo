from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox


# This defines the SWAP function. The SWAP function takes an array with two indexes and swaps the array items of the given indexes with each other.
def SWAP(TAM, i, j):
    # temp saves the value of TAM[i]
    temp = TAM[i]
    # TAM[i] is replaced with TAM[j]
    TAM[i] = TAM[j]
    # TAM [j] is then replaced with temp
    TAM[j] = temp
    # The array TAM is then returned as the output
    return TAM


# This defines the function that sorts the string into Ts, then As, then Ms.
def Sort_TAM(string):

    # Since the string has an '#' at its end, it removed and then the string is converted to an array.
    TAMUK = list(string[0:(len(string) - 1)])

    # The length of the array is gotten which tells how many items are in the list.
    n = len(TAMUK)

    # Next a counter and two pointers are initialized. T_ptr tracks the number of Ts while M_ptr tracks the number of Ms in the array.
    T_ptr = 0

    # This counter keeps track of all the items seen and swaps if necessary.
    counter = 0

    # M_ptr is initialized from the index of the last element in the array as the Ms will commence from there
    # and go in decrementing order till all the Ms are placed.
    M_ptr = n - 1

    # The while loop runs check every item in the array.
    # It adds a constraint that the counter should be less than M_ptr, the pointer that tracks M.
    # This ensures that it stops when all the Ts and Ms are fully sorted.
    while (counter <= M_ptr):
        # This takes care of the Ts. If the item seen is a T, it is swapped with the item with the index of T_ptr, by calling the SWAP function, putting it in the right place.
        # Then the counter is incremented to see the next item. T_ptr is also incremented as the first T is in the right place.
        if TAMUK[counter] == 'T':
            SWAP(TAMUK, T_ptr, counter)
            T_ptr += 1
            counter += 1

        # Next if the next item is an 'A' then the counter simply increments and goes on to the next item.
        elif TAMUK[counter] == 'A':
            counter += 1

        # This statement takes care of the Ms as when you take care of Ts and As, only Ms remain.
        # If the item seen is an M, it is swapped with the item with the index of M_ptr, by calling the SWAP function, putting it in the right place.
        # Then M_ptr is also decremented as the first M is in the right place in preparation for the next M.
        else:
            SWAP(TAMUK, counter, M_ptr)
            M_ptr -= 1

    # This appends the '#' removed initially back to the array
    TAMUK.append('#')

    # What is returned is a list of all the items in the array TAMUK
    return TAMUK


# This builds the GUI interface for the algorithm.
if __name__ == '__main__':
    # This calls the GUI package Tkinker
    root = Tk()

    # This builds the dimensions of the GUI
    root.geometry('1000x300')

    # This titles the GUI
    root.title("TAMi, the T-A-M Sorting Genius")

    # This code builds the font and size. We use calibri of size 14.
    titleFont = font.Font(family=" Calibri ", size=14)

    # This gives the title of the interface and where it is placed.
    title = Label(root, text="TAMi, the T-A-M Sorting Genius", font=titleFont)
    title.pack(side=TOP)

    # This function covers what will be done when the introduction button is pressed. It simply prints a description of the program.
    def intro():
        res = "This quantum computing program was designed to take a string of three letters (T,M and A), \nentered in any random order, and sorts them as followes: T's first, A's second and M's last."
        print(res)
        lbl.configure(text=res, font=titleFont)

    # This defines a function that gets value from the entry text and uses the Sort_TAM function to sort it accordingly. It then returns the sorted value.
    def click_sort():
        value = txt_entry.get()

        # This deals for cases where nothing is entered.
        if value == '':
            result = "Here you go feeble human, I managed to sort your chaotic string  \'#\''"
        else:
            result = Sort_TAM(value)
        print(*result)
        lbl.configure(text=result, font=titleFont)

    # This prompts the uses to enter the string
    prompt = Label(root, text=" Give me a string of A, M and T's and I will sort it for you.")
    prompt.pack(side=TOP)

    # This defines a text input window to receive the string.
    txt_entry = Entry(root, bd=1)
    txt_entry.pack(side=TOP)

    # This button when clicked gives the user an introduction of what the application does.
    intro_button = ttk.Button(root, text="About", width=20, command=intro)
    intro_button.pack(side=TOP)

    # This builds the sorting button.
    sort_button = ttk.Button(root, text="Sort", width=20, command=click_sort)
    sort_button.pack(side=TOP)

    # This builds a button that exits the program
    exit_button = ttk.Button(root, text="Exit", width=20, command=exit)
    exit_button.pack(side=TOP)

    # This text changes to print the results.
    lbl2 = Label(root, text=" ")
    lbl2.pack(side=TOP)

    lbl = Label(root, text=" ")
    lbl.pack(side=TOP)


    # This keeps Tkinter running
    root.mainloop()
