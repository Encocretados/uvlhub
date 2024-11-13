import logging

from flask import render_template, redirect, url_for, flash
from app.modules.community.models import Community
from app.modules.dataset.models import DataSet
from flask_login import login_required, current_user

from app.modules.community.forms import CommunityForm
from app.modules.community import community_bp
from app.modules.community.services import CommunityService
from app import db, community_members

community_service = CommunityService()

logger = logging.getLogger(__name__)

@community_bp.route("/community/list", methods=['GET'])
@login_required
def list_community():
    form = CommunityForm()
    communities = community_service.get_all_by_user(current_user.id)
    return render_template("community/list_communities.html", communities=communities, form=form)

@community_bp.route("/community/create", methods=['GET', 'POST'])
@login_required
def create_community():
    form = CommunityForm()
    if form.validate_on_submit():
        data = {
            "name": form.name.data,
            "description": form.description.data,
            "user": current_user
        }

        result = community_service.create_community(data=data)
        return community_service.handle_service_response(
            result=result,
            errors=form.errors,
            success_url_redirect='community.list_community',
            success_msg='Community created successfully',
            error_template='community/create_community.html',
            form=form
        )
    return render_template("community/create_community.html", form=form)

@community_bp.route("/community/<int:community_id>", methods=['GET'])
@login_required
def get_community(community_id):
    community = community_service.get_or_404(community_id)

    is_member = db.session.query(community_members) \
        .filter_by(user_id=current_user.id, community_id=community.id) \
        .first() is not None

    if not is_member:
        flash("You are not a member of this community", "error")
        return redirect(url_for("community.index"))
    return render_template("community/show_community.html", community=community)

@community_bp.route("/community/<int:community_id>/datasets", methods=["GET"])
@login_required
def show_community_datasets(community_id):
    # Obtener la comunidad
    community = Community.query.get_or_404(community_id)

    # Obtener los datasets asociados a la comunidad
    datasets = DataSet.query.filter_by(community_id=community_id).all()

    return render_template("community/community_datasets.html", community=community, datasets=datasets)
