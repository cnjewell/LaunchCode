class Post:
    def __init__(self, title, author, body):
        self.title = title
        self.author = author
        self.body = body
        self.likes = 0

    # Allow people to "like" posts, a la Facebook
    def like(self):
        self.likes += 1

    def __str__(self):
        return self.title + " by " + self.author


class VideoPost(Post):
    def __init__(self, title, author, url):
        super().__init__(title, author, None)
        self.video_url = url
        self.plays = 0

    # track plays of the video
    def play(self):
        self.plays += 1

    def __str__(self):
        return self.title + " played " + str(self.plays) + " times"

class LinkPost(Post):
    def __init__(self, title, author, url):
        super().__init__(title, author, None)
        self.clicks = 0
        self.url = url

    def __str__(self):
        return self.title + ": " + self.url

    def click(self):
        self.clicks += 1

class ImagePost(Post):
    def __init__(self, title, author, file_name):
        super().__init__(title, author, None)
        self.file_name = file_name

def main():
    vid_post = VideoPost("Little Scream - Love As a Weapon", "Chris Bay", "https://youtu.be/Tq4Vw4MB6eA")
    plain_post = Post("10 Best Albums of 2016", "Chris Bay", "1. Little Scream - Cult Following 2. ...")
    pic_post = ImagePost("Cats in space", "Crystal Martin", "spacecats.gif")
    url_post = LinkPost("LaunchCode's LC101", "LaunchCode Staff", "https://www.launchcode.org/lc101")

    vid_post.play()
    vid_post.play()
    url_post.click()

    print(vid_post)
    print(plain_post)
    print(pic_post)
    print(url_post)

if __name__ == "__main__":
    main()
