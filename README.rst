---------
Git clone
---------

    git clone https://github.com/csarcom/blog.git

------------
Dcoker build
------------

    docker build -t csarcom/blog:latest .

----------
Docker run
----------

    docker run -it -p 8000:8000 -v /$(pwd):/app csarcom/blog
