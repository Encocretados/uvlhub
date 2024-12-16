from flask import render_template
from app.modules.dashboard import dashboard_bp
from app.modules.dashboard.services import DashboardService

dashboard_service = DashboardService()


@dashboard_bp.route('/dashboard', methods=['GET'])
def index():
    dashboard_data = dashboard_service.get_dashboard_data()

    return render_template('dashboard/index.html', data=dashboard_data)
