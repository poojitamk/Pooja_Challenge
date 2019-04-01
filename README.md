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

    1. Clone repo to your local machine
    2. Once git clone has completed, navigate into the directory via Terminal
    3. Procure 2-aws EC2 instances and install ansible uisng below link
          Download & Install required dependencies
            http://docs.ansible.com/ansible/latest/intro_installation.html
    4. While in Pooja_Challenge directory... run: ansible-playbook playbook.yml
    5. Navigate to EC2-node instance in your browser of choice
       Note: Will redirect to https, but is currently using a self-signed certificate
    
  
