import logging

from flask import render_template, redirect, url_for, flash, request
from app.modules.auth.models import User
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

    return render_template("community/show_community.html", community=community, is_member=is_member)

@community_bp.route("/community/<int:community_id>/datasets", methods=["GET"])
@login_required
def show_community_datasets(community_id):
    # Obtener la comunidad
    community = Community.query.get_or_404(community_id)
    
    # Obtener todos los datasets de los usuarios de esta comunidad
    datasets = (
        DataSet.query.join(User)
        .join(community_members)
        .filter(community_members.c.community_id == community_id)
        .filter(DataSet.publico == True)
        .all()
    )
    return render_template("community/community_datasets.html", community=community, datasets=datasets)

@community_bp.route('/community/<int:community_id>/join', methods=['POST'])
@login_required
def join_community(community_id):
    community = Community.query.get_or_404(community_id)

    # Si ya está autenticado, unirlo a la comunidad
    if current_user not in community.members:
        community.members.append(current_user)  # Agregar usuario como miembro
        db.session.commit()
        flash("You have successfully joined the community!", "success")
    else:
        flash("You are already a member of this community.", "info")
    
    return redirect(url_for('community.get_community', community_id=community_id))

@community_bp.route('/community/<int:community_id>/leave', methods=['POST'])
@login_required
def leave_community(community_id):
    community = Community.query.get_or_404(community_id)

    # Verificar si el usuario es miembro de la comunidad
    if current_user in community.members:
        community.members.remove(current_user)  # Eliminar al usuario de la lista de miembros
        db.session.commit()  # Guardar los cambios en la base de datos
        flash("You have successfully left the community.", "success")
    else:
        flash("You are not a member of this community.", "info")

    # Redirigir al usuario a la página de la comunidad
    return redirect(url_for('community.get_community', community_id=community_id))

