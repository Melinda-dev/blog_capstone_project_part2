from flask import Flask, render_template
import requests


app = Flask(__name__)
blog_url = f"https://api.npoint.io/eb6cd8a5d783f501ee7d"
posts = requests.get(blog_url)
all_posts = posts.json()
print(all_posts)

@app.route("/")
def get_all_posts():
    return render_template("index.html", all_posts=all_posts)

@app.route("/post/<int:index>")
def each_post(index):
    for blog_post in all_posts:
        if blog_post["id"] == index:
            my_post = blog_post
            print(my_post['title'])
    return render_template("post.html", post=my_post)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__=="__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)