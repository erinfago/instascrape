prenote: when you see a command line argument don't type the "$" 

1) make sure you have python3 downloaded
	1a) to check, type python3 --version 
	1b) if not already installed, go to the link below and select the most recent version of python3

2) open terminal
	2a) if on a mac press command+space and type "terminal" and then press enter for easy open

3) $sudo easy_install pip

4) $sudo pip3 install selenium

5) make sure your chrome is up to date with the most current version
	5a) to check this open chrome, press the Chrome tab at the top, and select "About Chrome". This will show you what version you currently have and can update from here

6) go to the website below and download the stable version of chrome driver
https://sites.google.com/a/chromium.org/chromedriver/home
	6a) when the .exe file is done downloading, double-click the icon and then close the terminal when it says "Chrome driver successfully started 

7) make sure insta.py knows the PATH for the chrome driver 

	7a) click and drag the chrome driver executable onto the terminal to show its path; cut this information
	7b) open insta.py and paste your path on line 26 where it says "YOUR PATH HERE"
	7c) save the file

8) go back to terminal and type $python3 insta.py 

9) follow the prompts in the terminal

10) Know that you're valid regardless of who follows you