# WhatsappQuoteSender
I  made a small pyautogui script that will check for new whatsapp messages(predefined) and then react with an appropriate response

To use the script, download the whole repository and run main.py. You need to have the following modules:
- pyautogui
- random
- time
- requests

After you start the script you have 5 seconds to move the mouse to the position on screen where the new message will show up. After that you will move the mouse to where the second conversation could be, this is for the times you receive two new messages in seperate chats.

To calibrate this script let someone send you the word 'Quote' and then make a screenshot of this word in the new message box. Save this image as Quote.png.
If you also want to respond to Name, the repeat this step. If you want to implement other words copy this step but with your word.

The code will search for these new messages where you placed the mouse. If you added a word, copy the code in the forloop under QuoteList = findNewMessage({YourWordHere}).
To get the appropriate message create a function that will return your desired message as string.
Then in the forloop replace getQuote() from sendMessage(Location, getQuote()) to your function. Restart the code and you bot will also react on these messages.
