import tkinter as tk
from uploader import *
from news import *
from nlp import *
from threads_wrapper import *
from request import *
from login import *
import threading


# Define the main window
root = tk.Tk("")
root.geometry("800x600")
root.title("My News Analyzer")

# Add widgets to the main window
label = tk.Label(root, text="Welcome to News Analyzer!")
label.pack()

login_button = tk.Button(root, text="Log in!")
login_button.pack()

upload_button = tk.Button(root, text="File Upload", state="disabled")
upload_button.pack()

nlp_button = tk.Button(root, text="NLP Analysis", state="disabled")
nlp_button.pack()

ingest_button = tk.Button(root, text="Feed Ingester", state="disabled")
ingest_button.pack()

exit_button = tk.Button(root, text="Exit", command=root.destroy)
exit_button.pack()

# Define functions to handle user input
def on_login_click():
    login_button.config(state="disabled")
    upload_button.config(state="disabled")
    nlp_button.config(state="disabled")
    ingest_button.config(state="disabled")

    # Create a new thread for the login process (since login is frozen right now,
    # as json credentials not approved by Google Developers yet)
    login_thread = threading.Thread(target=login)
    login_thread.start()


def login():
    enable_functions()
    success = LogIn()
    if success:
        print("Login successful!")
   
def enable_functions():
    # Enable file upload button
    upload_button.config(state=tk.NORMAL)
    # Enable NLP analysis button
    nlp_button.config(state=tk.NORMAL)
    # Enable feed ingester button
    ingest_button.config(state=tk.NORMAL)

def on_upload_button_click():

    print("File Upload button clicked!")
    root.withdraw()  # hide the original interface
    upload_window = tk.Toplevel(root)  # create a new window for the upload frame
    upload_window.geometry("800x600")

    # create widgets for the new interface
    user_info_label = tk.Label(upload_window, text="Enter Username:")
    user_info_entry = tk.Entry(upload_window)
    file_info_label = tk.Label(upload_window, text="Enter Filepath:")
    file_info_entry = tk.Entry(upload_window)
    submit_button = tk.Button(upload_window, text="Submit")
    exit_button = tk.Button(upload_window, text="Exit")

    # grid the widgets to the new window
    user_info_label.grid(row=0, column=0, sticky=tk.W)
    user_info_entry.grid(row=0, column=1)
    file_info_label.grid(row=1, column=0, sticky=tk.W)
    file_info_entry.grid(row=1, column=1)
    submit_button.grid(row=2, column=1)
    exit_button.grid(row=4, column=1)

    # define the submit button click function
    def on_submit_button_click():
        username = user_info_entry.get()
        print("Username:", username)
        filename = file_info_entry.get()
        print("Filename / Filepath:", filename)

        # call uploader
        user = User(username)
        store_res = user.storeFile(filename)

        # to print results of upload
        result_label = tk.Label(upload_window, text=store_res)
        result_label.grid(row=3, column=1, pady=10)
        
    # define the exit button click function
    def on_exit_button_click():
        # destroy the upload frame and show the original interface
        upload_window.destroy()
        root.deiconify()

    submit_button.config(command=on_submit_button_click)
    exit_button.config(command=on_exit_button_click)

    # show the new interface
    upload_window.mainloop()



def on_nlp_button_click():

    print("NLP Analysis button clicked!")
    
    root.withdraw()  # hide the original interface
    upload_window = tk.Toplevel(root)  # create a new window for the upload frame
    upload_window.geometry("800x600")

    # create widgets for the new interface
    user_info_label = tk.Label(upload_window, text="Enter Username:")
    user_info_entry = tk.Entry(upload_window)
    file_info_label = tk.Label(upload_window, text="Enter Filepath:")
    file_info_entry = tk.Entry(upload_window)
    submit_button = tk.Button(upload_window, text="Submit")
    exit_button = tk.Button(upload_window, text="Exit")

    # grid the widgets to the new window
    user_info_label.grid(row=0, column=0, sticky=tk.W)
    user_info_entry.grid(row=0, column=1)
    file_info_label.grid(row=1, column=0, sticky=tk.W)
    file_info_entry.grid(row=1, column=1)
    submit_button.grid(row=2, column=1)
    exit_button.grid(row=3, column=1)

    # define the submit button click function
    def on_submit_button_click():
        username = user_info_entry.get()
        print("Username:", username)
        filename = file_info_entry.get()
        print("Filename / Filepath:", filename)

        # call uploader
        user = User(username)
        file, contents = user.uploadFile(filename)
        store_res = user.storeFile(filename)
        first_para_summary, keywords_top3, overall_sentiment, paragraph_count, word_count = analyze(file)

        # to print results of upload
        result_label = tk.Label(upload_window, text=store_res + "\nBrief summary below, enter database to view full analysis!", wraplength=400)
        result_label.grid(row=4, column=1, pady=10)
        summary_label = tk.Label(upload_window, text="Summary: " + str(first_para_summary), wraplength=400)
        summary_label.grid(row=6, column=1, pady=10)
        keywords_label = tk.Label(upload_window, text="Top 3 keywords: " + str(keywords_top3), wraplength=400)
        keywords_label.grid(row=5, column=1, pady=10)
        sentiment_label = tk.Label(upload_window, text="Overall sentiment: " + str(overall_sentiment), wraplength=400)
        sentiment_label.grid(row=10, column=1, pady=10)
        numpara_label = tk.Label(upload_window, text="Number of paragraphs: " + str(paragraph_count), wraplength=400)
        numpara_label.grid(row=11, column=1, pady=10)
        words_label = tk.Label(upload_window, text="Word count: " + str(word_count), wraplength=400)
        words_label.grid(row=112, column=1, pady=10)
        
    # define the exit button click function
    def on_exit_button_click():
        # destroy the upload frame and show the original interface
        upload_window.destroy()
        root.deiconify()

    submit_button.config(command=on_submit_button_click)
    exit_button.config(command=on_exit_button_click)

    # show the new interface
    upload_window.mainloop()


def on_ingest_button_click():
    print("Feed Ingester button clicked!")
    root.withdraw()  # hide the original interface
    upload_window = tk.Toplevel(root)  # create a new window for the upload frame
    upload_window.geometry("800x600")

    # create widgets for the new interface
    user_info_label = tk.Label(upload_window, text="Enter Username:")
    user_info_entry = tk.Entry(upload_window)
    file_info_label = tk.Label(upload_window, text="Enter URL (RSS or Atom):")
    file_info_entry = tk.Entry(upload_window)
    submit_button = tk.Button(upload_window, text="Submit")
    exit_button = tk.Button(upload_window, text="Exit")

    # grid the widgets to the new window
    user_info_label.grid(row=0, column=0, sticky=tk.W)
    user_info_entry.grid(row=0, column=1)
    file_info_label.grid(row=1, column=0, sticky=tk.W)
    file_info_entry.grid(row=1, column=1)
    submit_button.grid(row=2, column=1)
    exit_button.grid(row=3, column=1)

    # define the submit button click function
    def on_submit_button_click():
        username = user_info_entry.get()
        print("Username:", username)
        url = file_info_entry.get()
        print("URL (RSS or Atom):", url)

        # call uploader
        user = User(username)
        store_res = storeFeed(url, user)

        try:
            storeFeed(url, user)
        except ValueError as e:
            print("Error:", e)
            result_label = tk.Label(upload_window, text="Error:" + e)
            result_label.grid(row=3, column=1, pady=10)
        else:
            title, summary, _ = ingest_feed(url)
            result_label = tk.Label(upload_window, text="Feed ingest successful! Detailed results in database. Brief summary below:")
            result_label.grid(row=4, column=1, pady=10)
            title_label = tk.Label(upload_window, text="Title: " + str(title), wraplength=400)
            title_label.grid(row=5, column=1, pady=10)
            summary_label = tk.Label(upload_window, text="Summary: " + str(summary), wraplength=400)
            summary_label.grid(row=6, column=1, pady=10)

    # define the exit button click function
    def on_exit_button_click():
        # destroy the upload frame and show the original interface
        upload_window.destroy()
        root.deiconify()

    submit_button.config(command=on_submit_button_click)
    exit_button.config(command=on_exit_button_click)

    # show the new interface
    upload_window.mainloop()


login_button.config(command=on_login_click)
upload_button.config(command=on_upload_button_click)
nlp_button.config(command=on_nlp_button_click)
ingest_button.config(command=on_ingest_button_click)



# Start the GUI main loop
def main():
    root.mainloop()


if __name__ == "__main__":
    main()


