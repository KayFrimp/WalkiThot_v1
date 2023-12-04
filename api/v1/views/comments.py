#!venv/bin/python3
"""Comment RESTFul API Definition"""
from flask import abort, jsonify, request
from api.v1.views import app_views
from models import storage
from models.blog import Blog
from models.comment import Comment


@app_views.route('/blogs/<blog_id>/comments', methods=['GET'])
def fetch_comments(blog_id):
    """API Fetches all comments by blog_id"""
    blog = storage.get(Blog, blog_id)
    if not blog:
        abort(404)
    comments = [comment.to_dict() for comment in blog.comments]
    return jsonify(comments)


@app_views.route('/comments', methods=['GET'])
def fetch_all_comments():
    """API Fetches all Comment objects in DB"""
    comments = []
    for comment in storage.all(Comment).values():
        comment_dict = comment.to_dict()
        comment_dict['responses'] = [
            response.to_dict() for response in comment.responses]
        comments.append(comment_dict)
    return jsonify(comments)


@app_views.route('/comments/<comment_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_comment(comment_id):
    """API deletes Comment object by id"""
    comment = storage.get(Comment, comment_id)
    if not comment:
        abort(404)
    storage.delete(comment)
    storage.save()
    return jsonify({}), 200


@app_views.route('/blogs/<blog_id>/comments',
                 methods=['POST'], strict_slashes=False)
def create_comment(blog_id):
    """API creates a new Comment object in DB"""
    blog = storage.get(Blog, blog_id)
    if not blog:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'comment' not in request.get_json():
        abort(400, 'Missing email')
    attributes = request.get_json()
    comment = Comment(**attributes)
    comment.blog_id = blog_id
    storage.new(comment)
    storage.save()
    return jsonify(comment.to_dict()), 201


@app_views.route('/comments/<comment_id>',
                 methods=['PUT'], strict_slashes=False)
def update_comment(comment_id):
    """API updates Comment object by id"""
    comment = storage.get(Comment, comment_id)
    if not comment:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    attributes = request.get_json()
    for key, value in attributes.items():
        if key not in ['id', 'blog_id', 'created_at', 'updated_at']:
            setattr(comment, key, value)
        comment.save()
        return jsonify(comment.to_dict()), 200
