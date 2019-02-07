# Full-stack Web Dev Lab

In this lab we'll use the...

The University's file system is virtualized in a couple of ways, so avoid re-creating some symbolic links, we'll use the `public_html` directory they provide by default in your user profile home directory.    

If you do need to re-create it, you can read about how to do that [here](https://cat.pdx.edu/services/web/account-websites/)


## Step 1: Clone this repository and copy the files inside it to your `public_html` dir

`cp -r cgi_fullstack_demo/* ~/public_html/`

`cp cgi_fullstack_demo/.htaccess ~/public_html/`

Then, inside `public_html`:

Configure the permissions of all the files here to be readable and executable to the world (and writeable to you): `chmod 755 *`

Create a python3 virtual environment with: `virtualenv -p python3 venv`

Activate it: `source venv/bin/activate`

Install the requirements: `pip install -r requirements.txt`

And start up the server: `python3 myapp.py`
