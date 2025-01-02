
const borderColor = ['rgba(54, 162, 235, 1)', 'rgba(255, 99, 132, 1)','rgba(255, 159, 64, 1)','rgba(153, 102, 255, 1)']
const backgroundColor = ['rgba(54, 162, 235, 0.5)', 'rgba(255, 99, 132, 0.5)','rgba(255, 159, 64, 0.5)','rgba(153, 102, 255, 0.5)']

const diagram = new Chart(document.querySelector('#diagram'), {
    type: 'bar',
    data: {
        labels: ['Средний балл', 'Желаемый балл', 'Следование трекеру(%)', 'Оценка успеваемости'],
        datasets: [{
        label: '',
        data: [78, 90, 45, 64, 100],
        borderWidth: 3,
        borderColor,
        backgroundColor,

        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            },
            x: {
                ticks: {
                    font: {
                        weight: "bold",
                        size: 15,
                        family: "Montserrat",
                    },
                }
            }
        },
        plugins: {
            legend: { display: false }
        }
    },
    });