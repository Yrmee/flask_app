# Assignment: CD

## Back-end Development Final Assignment

Write a short 200/300-words report, which you discuss the following:

1. Name three components of your solution. <br>
Explain what they are and how they relate to each other. <br>
A 'component' can be anything from GitHub Actions or Bash to DigitalOcean and SSH.
2. Discuss three problems that you have encountered along the way. <br>
And how did you solved them?
3. (optional) Anything of note you want to share about the process of solving this assignment. <br><br>

---

### Report: Flask App continuous deployment on a VPS with Github Actions <br><br>

1. **Components**
    - Github Actions, is a feature of Github. Which is a way of automating tasks that come up as a result of writing code. For example; Running Tests on code everytime a new commit is pushed to Github to make sure everyting is working.
    - DigitalOcean, is an American multinational technology company and cloud service provider. There is also a platform where one can follow tutorials and read blogs. I used DigitalOcean to host a VPS for my flask app to run online with a droplet and read some tutorial documentations, which were very helpful.
    - SSH, short for Secure Shell. It is a method for secure remote login from one computer to another. For example; From a Local machine to a VPS. And it is a network communication protocol that enables two computers to communicate (transfer hypertext such as webpages) and share data. <br><br>

2. **Problems**
    - *Problem 1:* I got stuck in my own labyrinth of code of my project and in the server configuration settings of the droplet.
        - *Solution:* Start all over en build a brand new Flask App from scratch with a fresh created droplet. <br><br>
    - *Problem 2:* I had to execute commands manually in the ssh shell to see changes on the server after the 'auto' deploy and I wanted this to be automatic.
        - *Solution:* Creating a ```.sh``` file with a bash script that runs the commands with the deploy workflow to see automatic the changes on the server. (if tests are succesful) <br><br>
    - *Problem 3:* Defining and (re)Starting the systemd failed because of an issue/error with Gunicorn.
        - *Solution:* I had to change the location of Gunicorn with the nano-editor in the ```.service``` file and then ```systemctl enable --now``` the system to let Gunicorn run properly. <br><br>

3. **Optional Story**
    - I started with an old Flask App from our previous exercises, even though it didn't feel right from the start of this assignment to use this Flask App and I ignored all the red flags of it. (bad idea) Everything went pretty well, I understood what I was doing and where I was going. But a lot went wrong with auto deployment and refreshing the browser. I thought it is caused by some settings in the server configuration from the previous exercises (which may have not been the proper executions of those configurations at all, as I thought they were at this point) and so I decided to build a completely new Flask app from scratch with a new fresh droplet. I'd rather start over again than continue tinkering with my problem(s) in my project. <br><br>
    I watched many tutorials, read a lot of documentations and even read my own notes from months ago about this subject, just to go back to the understanding of the basics of building a (simple) Flask App. <br>
    I wanted to build something that I would be proud of and that would summarize my journey from what I've learned during this course. Now I even got do some Front-end stuff with this app ;). <br><br>
    I'm glad I started all over again. During the process I encountered things that suddenly fell into place, which I previously found so difficult and now understand better. Like; Writing tests with PyTest, NGINX&Gunicorn, Python itself and I have grown tremendously with the Command Line. I even like and find it easier to do everything via the Command Line nowadays. Which makes my life as a (junior) programmer so much easier now. <br><br>
    PS: I've had a lot of struggles with Python during this whole Back-end Dev Course, but I'm starting to get hope that we'll be friends someday. I do not give up.
