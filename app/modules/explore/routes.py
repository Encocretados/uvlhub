from flask import render_template, request, jsonify

from app.modules.explore import explore_bp
from app.modules.explore.forms import ExploreForm
from app.modules.explore.services import ExploreService
from flask import Flask

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"

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

def apply_advanced_filter():
    filters = request.json
    results = ExploreService.advanced_filter(**filters)
    return jsonify(results)

@explore_bp.route('/explore', methods=['POST'])
def clear_filters():
    results = ExploreService.clear_filters()
    return jsonify(results)

if __name__ == '__main__':
    explore_bp.run(debug=True)
