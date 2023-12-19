#!venv/bin/python3
from flask import Blueprint, flash, redirect, render_template, url_for

core_bp = Blueprint("core", __name__)


@core_bp.route('/', strict_slashes=False)
def home():
    """Returns Home Page"""
    blogs = []
    from models import storage
    from models.blog import Blog
    for blog in storage.all(Blog).values():
        blog_dict = blog.to_dict()
        comments = []
        for comment in blog.comments:
            comment_dict = comment.to_dict()
            comment_dict['responses'] = [
                response.to_dict() for response in comment.responses]
            comments.append(comment_dict)
        blog_dict['comments'] = comments
        blogs.append(blog_dict)
    return render_template("home.html", blogs=blogs)


@core_bp.route('/post/<blog_id>')
def post(blog_id):
    # Find the blog with the specified ID
    from models import storage
    from models.blog import Blog
    selected_blog = storage.get(Blog, blog_id)

    if selected_blog:
        return render_template('post.html', blog=selected_blog)
    else:
        # Handle case where blog with specified ID is not found
        flash("Falled to Load Blog...", "danger")
        return redirect(url_for("home"))


@core_bp.route('/about', strict_slashes=False)
def about():
    """Returns About Page"""
    return render_template("about.html")