document.addEventListener('DOMContentLoaded', function () {
    const totalViews = JSON.parse(document.getElementById('totalViews').textContent);
    const totalDownloads = JSON.parse(document.getElementById('totalDownloads').textContent);

    // Calcular el porcentaje de descargas frente a las vistas
    const downloadPercentage = ((totalDownloads / totalViews) * 100).toFixed(2);

    const data = {
        labels: ['Total Views', 'Total Downloads'],
        datasets: [{
            label: 'Métricas',
            data: [totalViews, totalDownloads],
            backgroundColor: ['#17a2b8', '#dc3545']
        }]
    };

    const config = {
        type: 'bar',
        data: data,
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function (context) {
                            // Mostrar el porcentaje en el tooltip de "Total Downloads"
                            if (context.label === 'Total Downloads') {
                                return `${context.label}: ${context.raw} (${downloadPercentage}%)`;
                            }
                            return `${context.label}: ${context.raw}`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    ticks: {
                        font: {
                            size: 16,
                            weight: 'bold'
                        },
                        color: '#333'
                    }
                },
                y: {
                    beginAtZero: true,
                    ticks: {
                        font: {
                            size: 14,
                            weight: 'normal'
                        }
                    }
                }
            }
        }
    };

    const ctx = document.getElementById('viewsDownloadsChart').getContext('2d');
    new Chart(ctx, config);

    const percentageElement = document.createElement('p');
    percentageElement.textContent = `Percentage of Downloads vs Views: ${downloadPercentage}%`;
    percentageElement.className = 'text-center text-secondary mt-3';
    document.getElementById('viewsDownloadsChart').parentElement.appendChild(percentageElement);
});
document.addEventListener('DOMContentLoaded', function () {
    const totalFeatureModelViews = JSON.parse(document.getElementById('totalFeatureModelViews').textContent);
    const totalFeatureModelDownloads = JSON.parse(document.getElementById('totalFeatureModelDownloads').textContent);

    // Calcular el porcentaje de descargas frente a las vistas para Feature Models
    const featureModelDownloadPercentage = totalFeatureModelViews > 0
        ? ((totalFeatureModelDownloads / totalFeatureModelViews) * 100).toFixed(2)
        : 0;

    const featureModelData = {
        labels: ['Total Views', 'Total Downloads'],
        datasets: [{
            label: 'Feature Model Metrics',
            data: [totalFeatureModelViews, totalFeatureModelDownloads],
            backgroundColor: [
                'rgba(59, 125, 221, 0.7)', // Azul semitransparente
                'rgba(240, 100, 100, 0.7)' // Rojo semitransparente
            ],
            borderColor: [
                'rgba(59, 125, 221, 1)', // Azul fuerte
                'rgba(240, 100, 100, 1)' // Rojo fuerte
            ],
            borderWidth: 1
        }]
    };

    const featureModelConfig = {
        type: 'bar',
        data: featureModelData,
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function (context) {
                            // Mostrar el porcentaje en el tooltip de "Total Downloads"
                            if (context.label === 'Total Downloads') {
                                return `${context.label}: ${context.raw} (${featureModelDownloadPercentage}%)`;
                            }
                            return `${context.label}: ${context.raw}`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    ticks: {
                        font: {
                            size: 14,
                            weight: 'bold'
                        },
                        color: 'var(--bs-gray-800)'
                    }
                },
                y: {
                    beginAtZero: true,
                    ticks: {
                        font: {
                            size: 12,
                            weight: 'normal'
                        },
                        color: 'var(--bs-gray-800)'
                    },
                    grid: {
                        color: 'rgba(0, 0, 0, 0.05)'
                    }
                }
            }
        }
    };

    const featureModelCtx = document.getElementById('featureModelChart').getContext('2d');
    new Chart(featureModelCtx, featureModelConfig);

    const featureModelPercentageElement = document.createElement('p');
    featureModelPercentageElement.textContent = `Percentage of Downloads vs Views: ${featureModelDownloadPercentage}%`;
    featureModelPercentageElement.className = 'text-center text-secondary mt-3';
    document.getElementById('featureModelChart').parentElement.appendChild(featureModelPercentageElement);
});
