import praw, smtplib,ssl
from email.message import EmailMessage
redditLink = "https://www.reddit.com"
text = "words.txt"
def get_submission_matches(text):
    sub = "subreddit"
    wordList = get_words_list(text)

    reddit = praw.Reddit(client_id=, client_secret=,

                 password=, user_agent=,

                 username=)

    subreddit = reddit.subreddit(sub)
    new_subreddit = subreddit.new(limit=20)

    outputSubmissions = []
    for submission in new_subreddit:
        if not (submission.stickied):
            for word in wordList:
                if word in submission.title.lower():
                    outputSubmissions.append(submission)
    return outputSubmissions


def get_words_list(text):
    words_list = []
    with open(text, 'r') as searchfiles:
        for line in searchfiles:
            lineStripped = line.strip()
            words_list.append(lineStripped)
    return words_list


def convert_submission_to_string(submissions):
    outString = ""
    for submission in submissions:
        outString += submission.title + "\n"
        outString += redditLink+submission.permalink + "\n\n"
    return outString


def filter_new_submissions(new_submissions):
    finalList = []
    for submission in new_submissions:
        current = redditLink + submission.permalink
        finalList.append(submission)
    return finalList

def get_email_list():
    email_list = []
    with open('emailList.txt', 'r') as searchfile:
        for line in searchfile:
            lineStripped = ''.join(line.split())
            lineStripped = lineStripped.split(",")
            email_list.append(lineStripped)
    return email_list

def mail(receiver_email, outString):
    port = 465
    sender_email =
    password = 

    if(len(outString) > 0):
        #mess = posts
        outString = outString.encode('ascii','ignore').decode('ascii')
        message = """\
        New Posts!

{}""".format(outString)
        msg = EmailMessage()
        msg["Subject"] = "Reddit Test"
        msg["From"] = sender_email
        msg["To"] = receiver_email
        msg.set_content(message)
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender_email, password)
            server.send_message(msg)
            #server.sendmail(sender_email,receiver_email,message)
def main(receiver_email):
    subreddit_submissions = get_submission_matches(text)
    filtered_submissions = filter_new_submissions(subreddit_submissions)
    if(len(filtered_submissions)!= 0):
        outputString = convert_submission_to_string(filtered_submissions)
        mail(receiver_email, outputString)

if __name__ == '__main__':
    email_list = get_email_list()
    for email in email_list:
        main(email[0])
