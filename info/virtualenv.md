# Virtualenv

Installing every Python package globally via the OS-bound package manager is often a path of sadness and pain. You'll get a ton of bloat, and versioning mismatches. Wouldn't it be so much better if you could just have a different local installs of Python that:

1. Don't require admin rights to install extra packages into
2. Could be activated and deactivated as needed

Well, this dream is a reality! There's an awesome tool for Python developers called `virtualenv` that offers just this functionality!

### Installing `Virtualenv`

To install `virtualenv`, run the following commands:

    sudo apt-get install python-setuptools python-pip
    sudo pip install virtualenv

### Using Virtualenv

`virtualenv` takes a folder and installs a local copy of python there, as well as the Python-package manager `pip`.

Let's walk through a potential use-case for `virtualenv`.

> I want to experiment with creating graphs of data using python. So I create a new folder called `graphing_projects` and head inside.

> I've decided that the graphing library I want to use is the `matplotlib`
> library. *However*, I know that `matplotlib` is really large, and I may not
> want to install it into the global system. Instead, I want to install a
> local copy that I can just delete when I no longer need it. This is where
> `virtualenv` comes in.

> To set up a local installation, I create a new directory that will hold my "virtual-environment".

    
    test_user@server:~/graphing_projects$ mkdir venv
    test_user@server:~/graphing_projects$ virtualenv venv/
    New python executable in venv/bin/python
    Installing Setuptools..............................................................................................................................................................................................................................done.
    Installing Pip.....................................................................................................................................................................................................................................................................................................................................done.
    test_user@server:~/graphing_projects$

> Now that I have a virtual environment set up, I activate it:

    test_user@server:~/graphing_projects$ source venv/bin/activate
    (venv)test_user@server:~/graphing_projects$ which python
    /home/test_user/graphing_projects/venv/bin/python

>> **NOTICE**: The `source` command is required to activate the virtualenv.

> As you can see, `python` is now the python installation found in the virtualenv. 

> When I am done installing and working in the virtualenv and want to get back the my standard configuration, I deactivate it:

    (venv)test_user@testServer:~/graphing_projects$ deactivate 
    test_user@testServer:~/graphing_projects$ 


