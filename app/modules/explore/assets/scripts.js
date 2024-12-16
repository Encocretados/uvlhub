document.addEventListener('DOMContentLoaded', () => {
    // Ejecutar consulta inicial
    send_query();

    // Añadir evento a los filtros para aplicar automáticamente
    const filters = document.querySelectorAll('#filters input, #filters select, #filters [type="radio"]');
    filters.forEach(filter => {
        filter.addEventListener('input', send_query);
    });

    // Añadir evento al botón "Apply Filters"
    const applyFiltersButton = document.getElementById('apply-filters');
    if (applyFiltersButton) {
        applyFiltersButton.addEventListener('click', send_query);
    }

    // Añadir evento al botón "Clear Filters"
    const clearFiltersButton = document.getElementById('clear-filters');
    if (clearFiltersButton) {
        clearFiltersButton.addEventListener('click', (e) => {
            e.preventDefault(); // Evitar el comportamiento predeterminado
            clearFilters(); // Llamar a la función de limpiar filtros
        });
    }

    // Manejar parámetros de consulta inicial desde la URL
    const urlParams = new URLSearchParams(window.location.search);
    const queryParam = urlParams.get('query');
    if (queryParam && queryParam.trim() !== '') {
        const queryInput = document.getElementById('query');
        queryInput.value = queryParam;
        queryInput.dispatchEvent(new Event('input', { bubbles: true }));
    }
});

function send_query() {
    console.log("Iniciando consulta...");

    document.getElementById('results').innerHTML = '';
    document.getElementById("results_not_found").style.display = "none";

    const csrfToken = document.getElementById('csrf_token')?.value || '';

    // Obtener criterios de búsqueda con los nuevos filtros
    const searchCriteria = {
        csrf_token: csrfToken,
        query: document.querySelector('#query').value,
        publication_type: document.querySelector('#publication_type').value,
        sorting: document.querySelector('[name="sorting"]:checked')?.value,
        tags: document.querySelector('#tags').value.split(',').map(tag => tag.trim()), // Obtener los tags
        author_name: document.querySelector('#author_name').value.trim(), // Obtener el nombre del autor
        after_date: document.querySelector('#after_date').value || null,
        before_date: document.querySelector('#before_date').value || null,
        min_size: parseFloat(document.querySelector('#min_size').value) || null,
        max_size: parseFloat(document.querySelector('#max_size').value) || null
    };

    console.log("Criterios de búsqueda:", searchCriteria);

    // Realizar la solicitud POST
    fetch('/explore', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(searchCriteria),
    })
        .then(response => {
            if (!response.ok) {
                throw new Error("Error en la respuesta de la solicitud");
            }
            return response.json();
        })
        .then(data => {
            mostrarResultados(data);
        })
        .catch(error => {
            console.error("Error en la solicitud fetch:", error);
        });
}

function mostrarResultados(data) {
    const resultsContainer = document.getElementById('results');
    const resultCount = data.length;
    const resultText = resultCount === 1 ? 'dataset' : 'datasets';

    document.getElementById('results_number').textContent = `${resultCount} ${resultText} found`;

    if (resultCount === 0) {
        document.getElementById("results_not_found").style.display = "block";
        return;
    }

    document.getElementById("results_not_found").style.display = "none";

    // Crear y mostrar las tarjetas de los datasets
    data.forEach(dataset => {
        const card = document.createElement('div');
        card.className = 'col-12';
        card.innerHTML = `
            <div class="card">
                <div class="card-body">
                    <h3><a href="${dataset.url}">${dataset.title}</a></h3>
                    <p class="text-secondary">${formatDate(dataset.created_at)}</p>
                    <p>${dataset.description}</p>
                    <a href="${dataset.url}" class="btn btn-primary btn-sm">View dataset</a>
                    <a href="/dataset/download/${dataset.id}" class="btn btn-secondary btn-sm">Download (${dataset.total_size_in_human_format})</a>
                </div>
            </div>
        `;
        resultsContainer.appendChild(card);
    });
}

function clearFilters() {
    console.log("Restableciendo filtros...");

    // Resetear la consulta de búsqueda
    document.querySelector('#query').value = "";

    // Resetear tipo de publicación y ordenamiento
    document.querySelector('#publication_type').value = "any";
    document.querySelectorAll('[name="sorting"]').forEach(option => {
        option.checked = option.value === "newest";
    });

    // Resetear filtros de fechas, tamaños y autor
    document.querySelector('#after_date').value = "";
    document.querySelector('#before_date').value = "";
    document.querySelector('#min_size').value = "";
    document.querySelector('#max_size').value = "";
    document.querySelector('#author_name').value = "";  // Resetear el nombre del autor

    // Ejecutar una nueva consulta con los filtros restablecidos
    send_query();
}

function formatDate(dateString) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString('en-US', options);
}