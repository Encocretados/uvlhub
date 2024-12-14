from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from app.modules.dashboard import dashboard_bp
from app.modules.dataset.services import DataSetService

datasetservice = DataSetService()


@dashboard_bp.route('/dashboard', methods=['GET'])
def index():
    return render_template('index.html')