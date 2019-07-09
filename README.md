![alt text](https://github.com/J216/simple_tag_replace/raw/master/jsi-logo-256.png "JSI Logo")
# jbutton
Take in command and have it on a button in a window

Here is a video giving 3 examples of how to use this.
https://youtu.be/1X8VKYXqEyA

## Examples:

jbutton ding

jbutton 'ping example.com -c 1' green

jbutton '/home/user/restart_services.sh' yellow

This python script takes whatever command you provide and attaches it to abutton you can press in a window/GUI
You can create as many buttons as you like.
To add colors or different buttons and a png of the image that has the name you would like to give it followed by "-button.png"
If you add a button that is an image of ice, name the image ice-button.png and store it in the same folder a jbutton.py, then to use this new button:

jbutton "echo 'Water has frozen'" ice

If you want to use this with out having to specify the full path consider doing this: 

ln -s /location/of/jbutton.py /usr/bin/jbutton
