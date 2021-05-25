# GUI-Calculator
Python program to create a Graphical User Interface based Standard Calculator using Tkinter module.
<hr>
Python offers multiple options for developing a GUI (Graphical User Interface). Out of all the GUI methods, Tkinter is the most commonly used method. It is a standard Python interface to the Tk GUI toolkit shipped with Python. Python with Tkinter outputs the fastest and easiest way to create GUI applications. Creating a GUI using Tkinter is an easy task.

Every tkinter program has the following common steps involved:-

<ol><li>Importing the tkinter module</li>
  <li>Create the container window and define its properties (color and properties etc.)</li>
  <li>Add widgets to the container window</li>
  <li>Apply the event Triggers on the widgets</li>
<li>So here we shall create a GUI based standard calculator using the Python Tkinter module, which can perform basic arithmetic operations addition, subtraction, multiplication, and division.</li></ol>
<hr>
Function description:-

<ul><li><b>press(num)</b> - This function will be executed when a digit or a decimal point button will be pressed. This function simply updates the expression by concatenatenating the parameter passed num with the global variable expression declared above.</li>
  <li><b>equalpress()</b> - This function will be executed when equals button will be pressed. Here try and except block is used to handle errors like division by zero , incomplete expression etc. The expression stored in expression variable is then evaluated using inbuilt eval() function of Python and stored in variable total which is then updated and the expression is cleared.</li>
  <li><b>clear()</b> - This function will be executed when the clear button will be pressed. This function simply clears the expression and updates it.</li>
  <li><b>main()</b> - We shall be cresting our containing window and add required buttons and other widgets. Below is the code for creation of window, adding titile of the window and specifing size of the window. we shall add a Text entry where our expression will be added and also create a StringVar() named equation. The Tkinter StringVar helps you manage the value of a widget such as a Label or Entry more effectively. Now since our expression entry and grid are set we shall keep on adding buttons. Once we have added buttons for 1,2,3,4,5,6,7,8,9,0,+,-,*,/,. and have provided them different colors for aome visual appeal. You may change them as per your wish.</li></ul>
<hr>
Finally we need to start our GUI application. So the mainloop() function is used for the purpose. This function is an infinite loop which is used to run the application, it will wait for an event to occur and process the event as long as the window is not closed.

<img src="https://user-images.githubusercontent.com/70680058/119518239-fac62b00-bd95-11eb-89a9-72c6fde0f563.png" align="center">

