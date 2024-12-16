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
document.addEventListener('DOMContentLoaded', function () {
    const publicationTypeData = JSON.parse(document.getElementById('publicationTypeData').textContent);

    const publicationLabels = Object.keys(publicationTypeData);
    const publicationCounts = Object.values(publicationTypeData);

    const publicationTypeConfig = {
        type: 'doughnut',
        data: {
            labels: publicationLabels,
            datasets: [{
                label: 'Publication Types',
                data: publicationCounts,
                backgroundColor: [
                    'rgba(75, 192, 192, 0.7)',
                    'rgba(255, 99, 132, 0.7)',
                    'rgba(54, 162, 235, 0.7)',
                    'rgba(255, 206, 86, 0.7)',
                    'rgba(153, 102, 255, 0.7)',
                ],
                borderColor: [
                    'rgba(75, 192, 192, 1)',
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(153, 102, 255, 1)',
                ],
                borderWidth: 1,
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                tooltip: {
                    callbacks: {
                        label: function (context) {
                            const label = context.label || '';
                            const value = context.raw || 0;
                            const total = publicationCounts.reduce((sum, count) => sum + count, 0);
                            const percentage = ((value / total) * 100).toFixed(2);
                            return `${label}: ${value} (${percentage}%)`;
                        }
                    }
                }
            }
        }
    };

    const publicationTypeCtx = document.getElementById('publicationTypeChart').getContext('2d');
    new Chart(publicationTypeCtx, publicationTypeConfig);
});
