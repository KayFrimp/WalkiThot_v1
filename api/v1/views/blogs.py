#!venv/bin/python3
"""USER RESTFul API Definitions"""
from flask import abort, jsonify, request
from api.v1.views import app_views
from models import storage
from models.blog import Blog
from models.user import User


@app_views.route('/blogs', methods=['GET'], strict_slashes=False)
def fetch_all_blogs():
    """API Fetches all blogs in DB"""
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


@app_views.route('/users/<user_id>/blogs',
                 methods=['GET'], strict_slashes=False)
def fetch_all_user_blogs(user_id):
    """API Fetches all blogs by user_id in DB"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    blogs = [blog.to_dict() for blog in user.blogs]
    return jsonify(blogs)


@app_views.route('/blogs/<blog_id>', methods=['GET'], strict_slashes=False)
def fetch_blog(blog_id):
    """API Fetches Blog object by id"""
    blog = storage.get(Blog, blog_id)
    if not blog:
        abort(404)
    return jsonify(blog.to_dict())


@app_views.route('/blogs/<blog_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_blog(blog_id):
    """API deletes Blog object by id"""
    blog = storage.get(Blog, blog_id)
    if not blog:
        abort(404)
    storage.delete(blog)
    storage.save()
    return jsonify({}), 200


@app_views.route('/users/<user_id>/blogs',
                 methods=['POST'], strict_slashes=False)
def create_blog(user_id):
    """API creates a new Blog object in DB"""
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


@app_views.route('/blogs/<blog_id>',
                 methods=['PUT'], strict_slashes=False)
def update_blog(blog_id):
    """API updates Blog object by id"""
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
