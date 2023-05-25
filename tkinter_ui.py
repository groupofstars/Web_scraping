import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

class App:
    def __init__(self, master):
        self.input_label = tk.Label(master, text="Enter URL:")
        self.input_label.grid(row=0, column=0, pady=5, sticky=tk.W)

        self.input_entry = tk.Entry(master, width=40)
        self.input_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        self.search_button = tk.Button(master, text="Search", command=self.search_url)
        self.search_button.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)

        self.function_label = tk.Label(master, text="Function:")
        self.function_label.grid(row=1, column=0, pady=5, sticky=tk.W)

        self.function_combobox = ttk.Combobox(master, values=["None", "h1", "h2", "h3", "comments", "other special"])
        self.function_combobox.current(0)
        self.function_combobox.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        self.result_label = tk.Label(master, text="Results:")
        self.result_label.grid(row=2, column=0, pady=5, sticky=tk.W)

        self.result_listbox = tk.Listbox(master, width=60, height=10)
        self.result_listbox.grid(row=3, column=0, columnspan=3, padx=5, pady=5, sticky=tk.W+tk.E)

        self.delete_button = tk.Button(master, text="Delete", state=tk.DISABLED, command=self.delete_url)
        self.delete_button.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)

        self.update_button = tk.Button(master, text="Update", state=tk.DISABLED, command=self.update_url)
        self.update_button.grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

        self.save_button = tk.Button(master, text="Save", state=tk.DISABLED, command=self.save_results)
        self.save_button.grid(row=4, column=2, padx=5, pady=5, sticky=tk.W)

        self.result_listbox.bind('<Double-Button-1>', self.enable_buttons)
        self.result_listbox.bind('<ButtonRelease-1>', self.click_url)

        self.results = {}

    def search_url(self):
        url = self.input_entry.get()
        function = self.function_combobox.get()

        # Do something with the URL and function
        # Then add the results to the listbox with its corresponding index stored in the self.results dictionary
        index = self.result_listbox.index(tk.END)
        self.results[index] = {"url": url, "function": function}
        self.result_listbox.insert(tk.END, f"Result {index+1}")

        # Enable save button
        self.save_button.config(state=tk.NORMAL)

    def enable_buttons(self, event):
        self.delete_button.config(state=tk.NORMAL)
        self.update_button.config(state=tk.NORMAL)

    def click_url(self, event):
        selected_item = self.result_listbox.curselection()
        if selected_item:
            index = selected_item[0]
            url = self.results[index]["url"]
            print(f"Opening URL: {url}") # Replace this line with your code to open the URL in a browser

    def delete_url(self):
        selected_item = self.result_listbox.curselection()
        if selected_item:
            index = selected_item[0]
            self.result_listbox.delete(index)
            del self.results[index]
            for i in range(index, self.result_listbox.size()):
                self.results[i] = self.results[i+1]
            self.results.pop(self.result_listbox.size(), None)

    def update_url(self):
        selected_item = self.result_listbox.curselection()
        if selected_item:
            index = selected_item[0]
            self.result_listbox.itemconfigure(index, bg='yellow')
            new_url = "http://newurl.com" # Replace this line with your code to prompt the user for a new URL
            self.results[index]["url"] = new_url
            self.result_listbox.delete(index)
            self.result_listbox.insert(index, f"Result {index+1}")

    def save_results(self):
        data = []
        for index in self.results:
            data.append([self.results[index]["url"], self.results[index]["function"]])
        df = pd.DataFrame(data, columns=['URL', 'Function'])
        df.to_excel('results.xlsx', index=False)

root = tk.Tk()
root.title("URL Search Results")

app = App(root)

root.mainloop()