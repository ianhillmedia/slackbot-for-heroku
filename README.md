# slackbot for heroku
A basic Slackbot in Python that can be deployed and run continuously on Heroku. The Slackbot searches for and responds to keywords. Code from and all praise and thanks to Buzzfeed Open Labs: https://github.com/buzzfeed-openlab/simple-slack-bot. I re-created it here so I could add more specific instructions on how to deploy it based on my experience as a novice who does not know Python. Read: Anybody can do this!

Questions or want to ask me about my experiences deploying this? Ping me at @ianhillmedia on Twitter.

STEP-BY-STEP DIRECTIONS ON HOW TO USE AND DEPLOY:

Download and install the Heroku CLI from https://devcenter.heroku.com/articles/heroku-cli

Download the code from Github. Move it into a folder on your desktop. This folder will be the Directory for your Slackbot.

In Slack, click the name of your team to get the dropdown menu. In the menu, click Apps and Integrations. 

Then click Build > Make a Custom Integration > Bots. Give your bot a username and click Add Bot Integration.

From the next screen, copy the API Token into a .txt file on your desktop. Click Save Integration.

Now we're going to leave Slack. Go to Heroku.com and, if you haven't already, create an account.

In Heroku, create a new app and give it a name. Click Create App.

You'll be taken to your app's dashboard. Click the Settings tab. In the Config Variables section, click Reveal Config Vars.

Add a new variable. In the KEY field, type API_TOKEN. In the value field, paste in the API Token you copied from your bot in Slack. Click Add.

Now we're going to leave Heroku. In a Mac, open Terminal; in Windows, open a Command Line (http://www.computerhope.com/issues/chusedos.htm)

Chnage your command to the Slackbot Directory (folder) on your desktop by typing cd ~/DIRECTORY LOCATION/ and clicking enter. Example: cd ~/Desktop/SLACKBOT/

Copy the API Token from your bot. In your command line, type echo "API_TOKEN = YOURAPITOKEN" > .env 

Hit enter. Nothing should happen in your command line, and you probably won't see a new file in your Slackbot Directory. That's OK!

Go back to your Heroku dashboard. Click the Deploy tab.

Scroll to the Deploy Using Heroku Git tab. Follow the instructions for typing commands in your command line to deploy your bot. NOTE: Your command line will already be in your Slackbot Directory, so you can skip the Heroku deploy command that starts with cd.

In your command line, type heroku ps:scale worker=1

Click Enter.

IT'S ALIVE! Your bot should be working. In Slack, invite your bot to a channel and see if it responds to commands. The default command is knock knock. You do not have to mention your bot by name - just type the command!

Is it not working? In your command line, type heroku logs and click enter. See what the logs say - that should tell you where the error is.

OTHER USEFUL INFO:

DON'T update your bot's code in a .txt file. Formatting issues can occur. Instead, download Python from https://www.python.org/downloads/ and use IDLE.

The bot commands are in run.py. Just update the text in quotes that you see in pairs["help"] = "YOUR INSTRUCTIONS HERE". Copy that line and add new commands and responses to customize your bot!

Want to update your Slackbot's code on Heroku? In your command line, type the following, hitting enter after every command:

`heroku login (you will be prompted to enter your heroku credentials)

cd ~/YOURSLACKBOTDIRECTORY/

git add .

git commit -m “COMMENT WITH YOUR CHANGE”

git push heroku master

heroku ps:scale worker=1`

Want your bot to mention a specific user in a response?

Go to: https://api.slack.com/docs/oauth-test-tokens and get an API token for your team.

Go to https://slack.com/api/users.list?token=YOURAPITESTTOKEN (pasting in your API token where it says YOURAPITESTTOKEN)

Do a CTRL + F or a CMND + F and search for the user's username.

When you find your user, look for their Slack User ID. It will start with @U, it looks like @U1A2B3C4G5. Copy the User ID.

Open run.py in IDLE. Add their User ID to your response in carats. The final code will look something like:
pairs["hello"] = "Thanks for your request! If <<@U1A2B3C4G5>> is working, he will reply and say hi!"

