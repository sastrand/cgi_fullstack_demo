# Full-stack Web Dev Lab

In this lab we'll use the...

We'll use the `public_html` directory provided by default in your Linux user profile home directory.    

The University's file system is virtualized in a couple of ways, so that directory is actually a symbolic link to the *actual* `public_html` directory in the solaris file system. If you need to re-create this sym link, you can read about how to do that [here](https://cat.pdx.edu/services/web/account-websites/).


## Setup

After cloning this repository, copy its contents to `public_html`    

`cp -r cgi_fullstack_demo/* ~/public_html/`

`cp cgi_fullstack_demo/.htaccess ~/public_html/`

Then, inside `public_html`:

  * Configure the permissions of all the files here to be readable and executable to the world (and writeable to you).       
    `chmod 755 *`

  * Create a python3 virtual environment.    
    `virtualenv -p python3 venv`

  * Activate it.    
    `source venv/bin/activate`

  * Install the requirements.    
    `pip install -r requirements.txt`

  * And start up the server.    
    `python3 myapp.py`
