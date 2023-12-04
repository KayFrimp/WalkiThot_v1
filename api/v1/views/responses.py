#!venv/bin/python3
"""Response RESTFul API Definition"""
from flask import abort, jsonify, request
from api.v1.views import app_views
from models import storage
from models.comment import Comment
from models.response import Response


@app_views.route('/comments/<comment_id>/responses', methods=['GET'])
def fetch_responses(comment_id):
    """API Fetches all responses by comment_id"""
    comment = storage.get(Comment, comment_id)
    if not comment:
        abort(404)
    responses = [response.to_dict() for response in comment.responses]
    return jsonify(responses)


@app_views.route('/responses', methods=['GET'])
def fetch_all_responses():
    """API Fetches all Response objects in DB"""
    responses = [
        response.to_dict() for response in storage.all(Response).values()]
    return jsonify(responses)


@app_views.route('/responses/<response_id>',
                 methods=['DELETE'], strict_slashes=False)
def delete_response(response_id):
    """API deletes Response object by id"""
    response = storage.get(Response, response_id)
    if not response:
        abort(404)
    storage.delete(response)
    storage.save()
    return jsonify({}), 200


@app_views.route('/comments/comment_id/responses',
                 methods=['POST'], strict_slashes=False)
def create_response(comment_id):
    """API creates a new Response object in DB"""
    comment = storage.get(Comment, comment_id)
    if not comment:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'reply' not in request.get_json():
        abort(400, 'Missing reply')
    attributes = request.get_json()
    response = Response(**attributes)
    response.comment_id = comment_id
    storage.new(response)
    storage.save()
    return jsonify(response.to_dict()), 201


@app_views.route('/responses/<response_id>',
                 methods=['PUT'], strict_slashes=False)
def update_response(response_id):
    """API updates Response object by id"""
    response = storage.get(Response, response_id)
    if not response:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    attributes = request.get_json()
    for key, value in attributes.items():
        if key not in ['id', 'comment_id', 'created_at', 'updated_at']:
            setattr(response, key, value)
        response.save()
        return jsonify(response.to_dict()), 200
