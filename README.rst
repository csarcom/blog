-------------
Personal blog
-------------

Git clone::
    
    git clone https://github.com/csarcom/blog.git
    cd blog/

Build::
    
    docker pull ghost

Running::

    docker run --name some-ghost -p 8080:2368 -v /$(pwd):/var/lib/ghost -d ghost



