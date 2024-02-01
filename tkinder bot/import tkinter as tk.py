import faulthandler
faulthandler.enable()
import tkinter as tk
from tkinter import messagebox
import webbrowser
import random
import secrets
import string
import pyttsx3
root = tk.Tk()
from tkinter import *
import time
#root=Tk()
#root.title('Bg setting')
#img=PhotoImage(file='hi.png')
#Label(root, image=img).pack()
txt_speech = pyttsx3.init()
root.geometry("800x900")
time.sleep(2)
root.title("Chatbot(call me sunny)")

# Create a label for chat history
history_label = tk.Label(root, text="Chat History")
history_label.pack()
# Create a text widget for chat history
history_text = tk.Text(root, height=20, width=60 )
history_text.pack()

# Create a scrollbar for chat history
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
history_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=history_text.yview)

# Create a label for user input
input_label = tk.Label(root, text="Enter your message:")
input_label.pack()

# Create an entry widget for user input
input_entry = tk.Entry(root, width=50)
input_entry.pack()
emotions = ["iam depressed","give me some advice","advice","will you be my friend","can i share my feelings","i want to share my story","i want to share my feelings"," can you me by friend"]
# Define a function to handle user input and display chatbot response
def handle_user_input():
    user_input = input_entry.get()
    if user_input == '':
        messagebox.showwarning("Warning", "Please enter a message")
        return
    add_message_to_chat_history("You", user_input)
    if user_input in emotions:
        response = emotion(user_input)
    else: 
        response = generate_chatbot_response(user_input)
    add_message_to_chat_history("Chatbot", response)
    input_entry.delete(0, tk.END)

# Create a button for user to submit input
button = tk.Button(root, text="Send", command=handle_user_input)
button.pack()
def generate_password():
    chars: str = string.ascii_letters + string.digits + string.punctuation
    password: str = ''.join(secrets.choice(chars) for _ in range(20))
    print("generated password:",password)
button = tk.Button(root, text="generate", command=generate_password)
button.pack()
def search_google():
        user_input = input_entry.get()
        if user_input == '':
            messagebox.showwarning("Warning", "Please enter a message")
            return
        url = f"https://www.google.com/search?q={user_input}"
        webbrowser.open_new_tab(url)
        #result_label.config(text="Search results opened in your web browser")

def view():
    url ="https://grow.google/certificates/interview-warmup/"
    webbrowser.open_new_tab(url)
def checkg():
    url ="https://www.security.org/how-secure-is-my-password/"
    webbrowser.open_new_tab(url)

button=tk.Button(root,text="search",command=search_google)
button.pack()        
# Define a function to add message to chat history
def add_message_to_chat_history(sender, message):
    history_text.config(state=tk.NORMAL)
    if sender == "You":
        history_text.insert(tk.END, sender + ": " + message + "\n", "blue")
    else:
        history_text.insert(tk.END, sender + ": " + message + "\n", "red")
 
history_text.config(state=tk.DISABLED)

    # Scroll down to the bottom of the chat history
history_text.see(tk.END)

    # Clear the input field
input_entry.delete(0, tk.END)

# Create tags for different message senders to apply different colors to their messages
history_text.tag_configure("blue", foreground="blue")
history_text.tag_configure("black", foreground="black")
def emotion(user_input):
    #if "iam sad" in user_input():
        #return"I'm sorry to hear that. Can you tell me more about how you're feeling?"
    #user_input = input_entry.get()
    if user_input == '':
            messagebox.showwarning("Warning", "Please enter a message")
            return
    else:
        reply=["It's okay to reach out for help, and it doesn't mean you're burdening anyone. You deserve to feel better, and there are people who can help you.","Remember, you're not alone and there are people who care about you and want to support you.","How about we start by finding a therapist for you? They can help you work through your feelings and find ways to cope.","No darkness lasts forever. And even there, there are stars.","Even if things were broken right now. Sometimes it was the cracks that let the light in.","Keep yourself busy if you want to avoid depression. For me, inactivity is the enemy."]
        return random.choice(reply)         



def speech():
     user_input = input_entry.get()
     if user_input == '':
        messagebox.showwarning("Warning", "Please enter a message")
        return
     txt_speech.say(user_input) # Say the input text
     txt_speech.runAndWait()

button = tk.Button(root,text='Convert',command=speech)
button.pack()    
#def open_url():
   # user=input("enter the topic:")
    #for i in search(user,tld="com",num=10,stop=10,pause=2 ):
        #print(i) 
greetings = ["hello", "hi", "hey", "greetings", "sup","hi there"]
responses = ["hi there", "hello", "I'm glad you're talking to me", "hey", "how's it going?"]
profile=["profile","who created you","owner's profile"]
owner_profile = ["name:yogeshwar","email:22pc39@psgtech.ac.in","ph-no:7867037922"]
training=["train me","interview warmup","train me for an interview","interview training"]
pass1=["check my password","password","check how strong is my password","how muck time will take crack my password"]
# Define a function to generate chatbot response
def generate_chatbot_response(user_input):
    # Insert your chatbot logic here
    # This is just a simple example
    if '||' in user_input:
        function.update_responses()
    elif user_input.lower() in greetings:
        return random.choice(responses)
    elif "search" in user_input.lower():
        search_google()
    elif user_input.lower() in profile :
        return random.choice(owner_profile)
    elif user_input.lower() in training:
        view()
    elif user_input.lower() in pass1:
        checkg()    
    elif "vanakkam" in user_input.lower():
         return "vanakkam,better we can continue with english "
    elif "generate" in user_input.lower():
        generate_password(20)
    elif "Convert" in user_input.lower():
        speech()
    #elif user_input.lower() in emotions:
        #return "ok"
    elif "how are you" in user_input.lower():
        return "I'm doing well, thank you. How can I assist you?"
    else:
        return "I'm sorry, I didn't understand your question."
root.mainloop()
