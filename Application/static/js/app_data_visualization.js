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
    // const data_input = $('#data-input').val(); 

    // Render the chart by clicking the generate-chart button
    $('#chart-display-form').on('submit', function(event) {
        event.preventDefault(); // Prevent form submission
        
        
        // Obtain selected type of chart from formulary
        const chart_type = $('#chart-type').val();

        // Destroy the previous chart if it exists
        const chart_canvas = $('#data-chart');
        if (window.data_chart) {
            window.data_chart.destroy();
        }

        // Create the new chart
        const ctx = chart_canvas[0].getContext('2d'); // Access DOM element from jQuery object.
        window.data_chart = new Chart(ctx, {
            type: chart_type,  // You can change this to 'line', 'pie', etc.
            data: {
                labels: labels,
                datasets: [{
                    label: 'Product Prices',
                    data: data,
                    backgroundColor: [
                        'rgba(255, 28, 77, 0.68)',
                        'rgba(33, 139, 209, 0.73)',
                        'rgba(243, 182, 27, 0.82)',
                        'rgba(27, 243, 38, 0.82)',
                        'rgba(157, 27, 243, 0.82)',
                        'rgba(243, 182, 27, 0.82)',
                        'rgba(243, 182, 27, 0.82)',
                        'rgba(243, 182, 27, 0.82)',
                      ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                    ],
                    borderWidth: 1,
                }],
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                },
                plugins: {
                    legend: {
                      position: 'top',
                    },
                    title: {
                      display: true,
                      text: 'March New Prices',
                    },
                },
            }
        });
    });
});