from flask import render_template, request, jsonify

from app.modules.explore import explore_bp
from app.modules.explore.forms import ExploreForm
from app.modules.explore.services import ExploreService

from flask import Blueprint, request, jsonify
from .services import ExploreService



@explore_bp.route('/ai/explore', methods=['POST'])
def explore_assistant():
    query = request.json.get('query', '')
    response = ExploreService().generate_analysis(query)
    return jsonify({'response': response})


@explore_bp.route('/explore', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        query = request.args.get('query', '')
        form = ExploreForm()
        return render_template('explore/index.html', form=form, query=query)

    if request.method == 'POST':
        criteria = request.get_json()
        datasets = ExploreService().filter(**criteria)
        return jsonify([dataset.to_dict() for dataset in datasets])
