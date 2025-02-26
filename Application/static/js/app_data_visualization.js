$(document).ready(function() {
    // Obtaining data (Database query, API call, hardcoded dataset)
    const dataset = [
        { label: 'Jamon', value: 150 },
        { label: 'CocaCola', value: 35 },
        { label: 'Pan Bimbo', value: 42 },
        { label: 'Chicle', value: 2 },
        { label: 'May', value: 5 },
        { label: 'June', value: 6 },
        { label: 'July', value: 7 },
        { label: 'August', value: 8 },
        { label: 'September', value: 9 },
        { label: 'October', value: 10 },
        { label: 'November', value: 11 },
        { label: 'December', value: 12 }
    ]

    // Extract labels and values from the dataset
    const labels = dataset.map(item => item.label);
    const data = dataset.map(item => item.value);

    // Render the chart
    const ctx = document.getElementById('data-chart').getContext('2d');
    const dataChart = new Chart(ctx, {
        type: 'line',  // You can change this to 'line', 'pie', etc.
        data: {
            labels: labels,
            datasets: [{
                label: 'Months Order',
                data: data,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
});