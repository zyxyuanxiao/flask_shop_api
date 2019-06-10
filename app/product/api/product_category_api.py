from flask import jsonify, request
from flask.views import MethodView
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required
from app import app
from app.constants import Message
from app.helpers import validator
from app.product.category.models import ProductCategory


class ProductCategoryApi(MethodView):
    @cross_origin()
    @jwt_required
    def get(self):
        page = request.args.get('page')
        id = request.args.get('id')
        if id:
            category = ProductCategory.get_by_id(id)
            result = category.__dict__
            del result['_sa_instance_state']
            return jsonify(result), 200
        categories = ProductCategory.get_all(page)
        return jsonify(categories), 200

    @cross_origin()
    @jwt_required
    def post(self):
        body = request.data
        keys = ['name']
        if not body:
            validated = validator.field_validator(keys, {})
            if not validated["success"]:
                app.logger.warning('{}: \n {}'.format(Message.VALIDATION_ERROR, body))
                return jsonify(validated['data']), 400
        if request.is_json:
            body = request.get_json()
            validated = validator.field_validator(keys, body)
            if not validated["success"]:
                app.logger.warning('Field validation error: \n {}'.format(body))
                return jsonify(validated['data'])
            name = body['name']
            category = ProductCategory(name=name)
            try:
                category.create(category)
                app.logger.debug(Message)
                return jsonify(), 201
            except Exception as e:
                app.exception("Error occurred. {}".format(str(e)))
                return jsonify(message="Could not save record!"), 400
        else:
            app.logger.warning('Content type header IS not application/json')
            return jsonify(message='Content-type header is not application/json'), 400

    @cross_origin()
    @jwt_required
    def put(self):
        return jsonify(), 200

    @cross_origin()
    @jwt_required
    def delete(self):
        return jsonify(), 200


app.add_url_rule('/product/category/', view_func=ProductCategoryApi.as_view('product-categories'),
                 methods=['GET', 'POST', 'PUT','DELETE'])