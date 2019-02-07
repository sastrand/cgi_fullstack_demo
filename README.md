# Full-stack Web Dev Lab

## The resources we've got
The College of Engineering and Computer Science IT Department (the CAT) maintains an Apache web server that hosts the `public_html` directory present by default in everyone's file system.  

You can find it at `~/public_html`.  

The user file system is virtualized in a couple of ways, so that directory is a symbolic link to the *actual* `public_html` directory in the solaris file system. If you need to re-create this sym link, you can read about how to do that [here](https://cat.pdx.edu/services/web/account-websites/).

## How we're going to use them

In this directory you can place an `index.html` file that will be sent out to anyone who sends a `GET` request to `http://web.cecs.pdx.edu/~<your_user_name>`.

You can put all kinds of awesome front-end code here and it will be sent off and rendered in a client's browser, but if you want to run a back-end web server to dynamically serve web pages based on user input, that takes a bit more configuration.

In particular, we'll need to make use of the support for Common Gateway Interfaces (CGI) offered by the CAT. In a CGI configuration, a `.htaccess` file tells the web server to run a given application whenever it receives a request at this location, pass the request it received to the running application, wait for the application to generate a response, and then serve that response back to the client.

In this lab, `myapp.py` is a Python Flask server. `myapp.cgi` is a very small Python program that invokes this app. And the `.htaccess` file tells the University's Apache server to run `myapp.cgi` whenever it receives a request for a resource at this location, to pass that request to `myapp.cgi`, and serve the result back to the user.

## Setup

After cloning this repository, copy its contents to `public_html`    

`cp -r cgi_fullstack_demo/* ~/public_html/`

`cp cgi_fullstack_demo/.htaccess ~/public_html/`

In the `.htaccess` file, replace my username with yours.

Then, inside `public_html`:

  * Configure the permissions of all the files here to be readable and executable to the world (and writeable to you).       
    `chmod 755 *`    
    `chmod 755 .htaccess`

  * Create a python3 virtual environment.    
    `virtualenv -p python3 venv`

  * Activate it.    
    `source venv/bin/activate`

  * Install the requirements.    
    `pip install -r requirements.txt`

## Next steps

Project 0: Modify this web app to record the names of visitors and return a list of past vistors below the greeting to each new visitor.

Project 1: Modify this web app to take two numbers and return their sum.

Project 2: Build a web app for a diner that allows customers to place orders off the menu. On the main page of the app, list each menu item and provide an input box for a customer to select how many of that item they'd like to order. On the back-end send an email to the diner with each request.

## Further reading

For more information about front-end code (HTML, CSS and JavaScript), the [Mozilla Develop Network](https://developer.mozilla.org/en-US/docs/Learn) is an excellent resource.  

For more information about Python flask and the jinja template system, the flask [docs](http://flask.pocoo.org/docs/1.0/) are a great place to start.

To send an email through a python application, check out the [`smtplib`](https://docs.python.org/2/library/smtplib.html) package and this [tutorial](http://naelshiab.com/tutorial-send-email-python/).


## Debugging

The Flask option `debug = True` is set in this application. This won't help with debugging the application when run through a CGI, but it will help debug it locally.

Among other things, the debug flag tells your server to return full error messages to the client when errors arise. This additional information available to the client is a security risk, and so you should remove this `debug = True` flag if you start to use this app for anything beyond this lab.

To run your server locally and take advantage of this debug mode, you'll need to run it on your own computer on be on a CAT-supported computer. Then you run the application and open the URL it provides in the command line output.  

`python3 myapp.py`
