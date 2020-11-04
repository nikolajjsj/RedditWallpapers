import praw
import requests
from secrets import client_id, secret

sub = "wallpaper"


def main():
    # Instance of reddit object from PRAW
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=secret,
        user_agent="Python script: v1.0.0 (by u/niko2931)"
    )

    for submission in reddit.subreddit(sub).hot(limit=10):
        imageUrl = submission.url
        imageName = imageUrl.split("/")[-1]
        downloadWallpaper(imageUrl, imageName)


def downloadWallpaper(imageUrl, imageName):
    response = requests.get(imageUrl)
    file = open(imageName, "wb")
    file.write(response.content)
    file.close()


if __name__ == "__main__":
    main()
