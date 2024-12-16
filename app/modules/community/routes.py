import logging

from flask import flash, redirect, render_template, request, url_for
from app.modules.dataset.services import DataSetService
from flask_login import current_user, login_required

from app import community_members, db
from app.modules.auth.models import User
from app.modules.community import community_bp
from app.modules.community.forms import CommunityForm, EditCommunityForm
from app.modules.community.models import Community
from app.modules.community.services import CommunityService
from app.modules.dataset.models import DSMetaData, DataSet

community_service = CommunityService()
dataset_service = DataSetService()

logger = logging.getLogger(__name__)


@community_bp.route("/community/list", methods=["GET"])
@login_required
def list_community():
    form = CommunityForm()
    communities = community_service.get_all_by_user(current_user.id)
    return render_template(
        "community/list_communities.html", communities=communities, form=form
    )


@community_bp.route("/community/create", methods=["GET", "POST"])
@login_required
def create_community():
    form = CommunityForm()
    if form.validate_on_submit():
        data = {
            "name": form.name.data,
            "description": form.description.data,
            "user": current_user,
        }

        result = community_service.create_community(data=data)
        return community_service.handle_service_response(
            result=result,
            errors=form.errors,
            success_url_redirect="community.list_community",
            success_msg="Community created successfully",
            error_template="community/create_community.html",
            form=form,
        )
    return render_template("community/create_community.html", form=form)


@community_bp.route("/community/<int:community_id>", methods=["GET"])
@login_required
def get_community(community_id):
    community = community_service.get_or_404(community_id)

    is_member = (
        db.session.query(community_members)
        .filter_by(user_id=current_user.id, community_id=community.id)
        .first()
        is not None
    )

    return render_template(
        "community/show_community.html", community=community, is_member=is_member
    )


@community_bp.route("/community/<int:community_id>/datasets", methods=["GET"])
@login_required
def show_community_datasets(community_id):
    # Obtener la comunidad
    community = Community.query.get_or_404(community_id)

    # Obtener todos los datasets de los usuarios de esta comunidad
    datasets = (
    DataSet.query.join(User)
    .join(community_members, community_members.c.user_id == User.id)
    .join(Community, community_members.c.community_id == Community.id)
    .filter(Community.id == community_id)
    .join(DSMetaData)
    .filter(DSMetaData.dataset_doi.isnot(None))
    .order_by(DataSet.created_at.desc())
    .all()
)


    return render_template(
        "community/community_datasets.html", community=community, datasets=datasets
    )


@community_bp.route("/community/<int:community_id>/join", methods=["POST"])
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

    return redirect(url_for("community.get_community", community_id=community_id))


@community_bp.route("/community/<int:community_id>/leave", methods=["POST"])
@login_required
def leave_community(community_id):
    community = Community.query.get_or_404(community_id)

    # Verificar si el usuario es miembro de la comunidad
    if current_user in community.members:
        community.members.remove(
            current_user
        )  # Eliminar al usuario de la lista de miembros
        db.session.commit()  # Guardar los cambios en la base de datos
        flash("You have successfully left the community.", "success")
    else:
        flash("You are not a member of this community.", "info")

    # Redirigir al usuario a la página de la comunidad
    return redirect(url_for("community.get_community", community_id=community_id))


@community_bp.route("/community/<int:community_id>/edit", methods=["GET", "POST"])
@login_required
def edit_community(community_id):
    community = Community.query.get_or_404(community_id)

    # Verificar si el usuario actual es el creador
    if community.creator_id != current_user.id:
        flash("You are not authorized to edit this community.", "danger")
        return redirect(url_for("community.show_community", community_id=community.id))

    form = EditCommunityForm(obj=community)  # Precargar datos actuales

    if form.validate_on_submit():
        community.name = form.name.data
        community.description = form.description.data
        try:
            community.save()
            flash("Community updated successfully!", "success")
            return redirect(
                url_for("community.show_community", community_id=community.id)
            )
        except Exception as e:
            db.session.rollback()
            flash("An error occurred while updating the community.", "danger")
            print(e)

    return render_template(
        "community/edit_community.html", form=form, community=community
    )


@community_bp.route("/community/<int:community_id>/delete", methods=["POST"])
@login_required
def delete_community(community_id):
    community = Community.query.get_or_404(community_id)

    # Verificar si el usuario actual es el creador
    if community.creator_id != current_user.id:
        flash("You are not authorized to delete this community.", "danger")
        return redirect(url_for("community.show_community", community_id=community.id))

    try:
        # Eliminar manualmente las relaciones en community_members
        community.members.clear()
        db.session.delete(community)
        db.session.commit()
        flash("Community deleted successfully.", "success")
        return redirect(url_for("community.list_community"))
    except Exception as e:
        db.session.rollback()
        flash("An error occurred while deleting the community.", "danger")
        print(e)
        return redirect(url_for("community.edit_community", community_id=community.id))
