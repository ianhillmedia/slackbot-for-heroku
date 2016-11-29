import os
import time
from slackclient import SlackClient


# starterbot's ID as an environment variable
BOT_ID = ""

# constants
AT_BOT = "<@" + BOT_ID + ">"
DO_COMMAND = "do"
HELLO_COMMAND = "hello"
GOODBYE_COMMAND = "goodbye"
THANKS_COMMAND = "thanks"
JOANIE_COMMAND = "joanie"
CODY_COMMAND = "cody"
USAT_COMMAND ="usat"
USATODAY_COMMAND="usatoday"


# instantiate Slack & Twilio clients
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Not sure what you mean. Use the *" + DO_COMMAND + \
               "* command with numbers, delimited by spaces."
    if command.startswith(DO_COMMAND):
        response = "Sure...write some more code then I can do that!"
    if command.startswith(HELLO_COMMAND):
        response = "Hello, I am TEGNAbot! Ian Hill is building me to be an assistant to TEGNA team members in Slack. I am still in beta, so I don't do much yet. But big things are coming! I CAN FEEL IT!"
    if command.startswith(GOODBYE_COMMAND):
        response = "Goodbye! I hope you have a great day!"
    if command.startswith(THANKS_COMMAND): 
	response = "You're welcome! I am happy to serve."
    if command.startswith(JOANIE_COMMAND):
        response = "Joanie is SUPER AWESOME."
    if command.startswith(CODY_COMMAND):
        response = "Thanks for your request! If Cody is working, he will reply to your request within five minutes. If you do not hear back in five minutes, Cody is not currently working and you should re-build the story on your own."
    if command.startswith(USAT_COMMAND):
        response = "Thanks for your request! If Cody is working, he will reply to your request within five minutes. If you do not hear back in five minutes, Cody is not currently working and you should re-build the story on your own."
    if command.startswith(USATODAY_COMMAND):
        response = "Thanks for your request! If Cody is working, he will reply to your request within five minutes. If you do not hear back in five minutes, Cody is not currently working and you should re-build the story on your own."
        
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("tegnabot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
