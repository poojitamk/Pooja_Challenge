## SED Challenge
##Infrastructure
      
    • Create and deploy a running instance of a web server using a configuration management
    tool of your choice. The web server should serve one page with the following content.
        <html>
        <head>
        <title>Hello World</title>
        </head>
        <body>
        <h1>Hello World!</h1>
        </body>
        </html>
    • Secure this application and host such that only appropriate ports are publicly exposed and
    any http requests are redirected to https. This should be automated using a configuration
    management tool of your choice and you should feel free to use a self-signed certificate for
    the web server.
    • Develop and apply automated tests to validate the correctness of the server configuration.
  

#How to Run:

    Clone repo to your local machine
    Once git clone has completed, navigate into the directory via Terminal
    Procure 2-aws EC2 instances and install ansible uisng below link
    Download & Install required dependencies
      http://docs.ansible.com/ansible/latest/intro_installation.html
    While in SRE_Challenge directory... run: ansible-playbook playbook.yml
    Navigate to EC2-node instance in your browser of choice
    Note: Will redirect to https, but is currently using a self-signed certificate
