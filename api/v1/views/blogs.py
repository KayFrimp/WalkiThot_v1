#!venv/bin/python3
"""USER RESTFul API Definitions"""
from flask import Blueprint, abort, jsonify, render_template, request


blog_bp = Blueprint("blogs", __name__)

@blog_bp.route('/write', methods=['GET'], strict_slashes=False)
def write():
    """API Renders the Write Page"""
    return render_template("write.html")


@blog_bp.route('/blogs', methods=['GET'], strict_slashes=False)
def fetch_all_blogs():
    """API Fetches all blogs in DB"""
    from models import storage
    from models.blog import Blog
    blogs = []
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
    return jsonify(blogs)


@blog_bp.route('/users/<user_id>/blogs',
                 methods=['GET'], strict_slashes=False)
def fetch_all_user_blogs(user_id):
    """API Fetches all blogs by user_id in DB"""
    from models import storage
    from models.blog import User
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    blogs = [blog.to_dict() for blog in user.blogs]
    return jsonify(blogs)


@blog_bp.route('/blogs/<blog_id>', methods=['GET'], strict_slashes=False)
def fetch_blog(blog_id):
    """API Fetches Blog object by id"""
    from models import storage
    from models.blog import Blog
    blog = storage.get(Blog, blog_id)
    if not blog:
        abort(404)
    return jsonify(blog.to_dict())


@blog_bp.route('/blogs/<blog_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_blog(blog_id):
    """API deletes Blog object by id"""
    from models import storage
    from models.blog import Blog
    blog = storage.get(Blog, blog_id)
    if not blog:
        abort(404)
    storage.delete(blog)
    storage.save()
    return jsonify({}), 200


@blog_bp.route('/users/<user_id>/blogs',
                 methods=['POST'], strict_slashes=False)
def create_blog(user_id):
    """API creates a new Blog object in DB"""
    from models import storage
    from models.blog import Blog
    from models.user import User
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'title' not in request.get_json():
        abort(400, 'Missing title')
    if 'content' not in request.get_json():
        abort(400, 'Missing content')
    attributes = request.get_json()
    blog = Blog(**attributes)
    blog.user_id = user_id
    storage.new(blog)
    storage.save()
    return jsonify(blog.to_dict()), 201


@blog_bp.route('/blogs/<blog_id>',
                 methods=['PUT'], strict_slashes=False)
def update_blog(blog_id):
    """API updates Blog object by id"""
    from models.user import User
    from models import storage
    from models.blog import Blog
    blog = storage.get(Blog, blog_id)
    if not blog:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    attributes = request.get_json()
    for key, value in attributes.items():
        if key not in ['id', 'user_id', 'created_at', 'updated_at']:
            setattr(User, key, value)
        blog.save()
        return jsonify(blog.to_dict()), 200
