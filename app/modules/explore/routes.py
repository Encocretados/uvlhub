from flask import render_template, request, jsonify
from datetime import datetime

from app.modules.explore import explore_bp
from app.modules.explore.forms import ExploreForm
from app.modules.explore.services import ExploreService

@explore_bp.route('/explore', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # Extrae parámetros de consulta desde la URL
        query = request.args.get('query', '')
        after_date = request.args.get('after_date')
        before_date = request.args.get('before_date')
        sorting = request.args.get('sorting', 'newest')
        publication_type = request.args.get('publication_type', 'any')
        tags = request.args.getlist('tags')
        author_name = request.args.get('author_name', '').strip()

        # Validar y ajustar las fechas proporcionadas
        if after_date:
            try:
                after_date = datetime.strptime(after_date, '%Y-%m-%d').replace(hour=0, minute=0, second=0)
                print(f"after_date ajustado: {after_date}")
            except ValueError:
                after_date = None

        if before_date:
            try:
                before_date = datetime.strptime(before_date, '%Y-%m-%d').replace(hour=23, minute=59, second=59)
                print(f"before_date ajustado: {before_date}")
            except ValueError:
                before_date = None

        # Llama al servicio para obtener datasets filtrados
        datasets = ExploreService().filter(
            query=query,
            sorting=sorting,
            publication_type=publication_type,
            tags=tags,
            after_date=after_date,
            before_date=before_date,
            author_name=author_name
        )

        # Renderiza el formulario y los resultados
        form = ExploreForm()
        return render_template('explore/index.html', form=form, query=query, datasets=datasets)

    if request.method == 'POST':
        # Procesa el cuerpo JSON recibido
        criteria = request.get_json()
        after_date = criteria.get('after_date')
        before_date = criteria.get('before_date')
        author_name = criteria.get('author_name', '').strip()

        # Convierte las fechas si están presentes
        if after_date:
            try:
                after_date = datetime.strptime(after_date, '%Y-%m-%d').replace(hour=0, minute=0, second=0)
                print(f"after_date procesado: {after_date}")
            except ValueError:
                print("after_date tiene un formato inválido")
                after_date = None

        if before_date:
            try:
                before_date = datetime.strptime(before_date, '%Y-%m-%d').replace(hour=23, minute=59, second=59)
                print(f"before_date procesado: {before_date}")
            except ValueError:
                print("before_date tiene un formato inválido")
                before_date = None

        # Actualiza el criterio de búsqueda con las fechas procesadas
        criteria['after_date'] = after_date
        criteria['before_date'] = before_date
        criteria['author_name'] = author_name

        # Ejecuta el filtro y devuelve los resultados como JSON
        datasets = ExploreService().filter(**criteria)
        return jsonify([dataset.to_dict() for dataset in datasets])
