const top_ten_json = JSON.parse(document.getElementById("population").innerText);
const fem_json = JSON.parse(document.getElementById("female-population").textContent)
const mal_json = JSON.parse(document.getElementById("male-population").textContent);
const ages = JSON.parse(document.getElementById("ages").textContent);

const remaining = 100 - Object.values(top_ten_json).reduce((tot, num) => tot + num);

var ctx = document.getElementById('top-ten-pop').getContext('2d');
var topTenChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: Object.keys(top_ten_json),
        datasets: [
            {
                label: 'Top ten most populous states (%)',
                data: Object.keys(top_ten_json).map(x => top_ten_json[x]),
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            },
        ]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true,
            },
        },
    }
});


ctx = document.getElementById('gender-per-state').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: Object.keys(fem_json),
        datasets: [{
            label: 'Female (%)',
            data: Object.keys(fem_json).map(x => fem_json[x]),
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
        },
        {
            label: 'Male (%)',
            data: Object.keys(mal_json).map(x => mal_json[x]),
            backgroundColor: 'rgba(255, 132, 132, 0.2)',
            borderColor: 'rgba(255, 132, 132, 1)',
            borderWidth: 1
        }
        ]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true,
                stacked: true,
            },
            x: {
                max: 100,
                stacked: true,
            },
        },
    }
});

ctx = document.getElementById('gender-ratio').getContext('2d');
var genderRatio = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["Female", "Male"],
        datasets: [{
            label: "Percentage",
            data:
                [
                    Number(document.getElementById('fem-percent').textContent),
                    Number(document.getElementById('male-percent').textContent),
                ],
            backgroundColor:
                [
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 132, 132, 0.2)',
                ],
            borderColor:
                [
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 132, 132, 1)',
                ],
            borderWidth: 1
        },
        ]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true,
            },
            x: {
                max: 100,
            },
        },
        indexAxis: 'y',
    }
});

ctx = document.getElementById('age-range').getContext('2d');
var ageRange = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: Object.keys(ages),
        datasets: [{
            label: 'Population by age',
            data: Object.keys(ages).map(x => ages[x]),
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            borderColor: 'rgba(54, 162, 235, 1)',
            borderWidth: 1
        },
        ]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true,
                max: 100,
            },
        },
    }
});

ctx = document.getElementById('name-ratio').getContext('2d');
var nameRatio = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ["First names", "Last names"],
        datasets: [{
            label: 'Beginning in A-M',
            data: [
                Number(document.getElementById('first-am').textContent),
                Number(document.getElementById('last-am').textContent),
            ],
            backgroundColor:
                [
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                ],
            borderColor:
                [
                    'rgba(54, 162, 235, 1)',
                    'rgba(54, 162, 235, 1)',
                ],
            borderWidth: 1,
            stack: 'Stack 0',
        },
        {
            label: 'Beginning in A-Z',
            data: [
                Number(document.getElementById('first-nz').textContent),
                Number(document.getElementById('last-nz').textContent),
            ],
            backgroundColor:
                [
                    'rgba(255, 132, 132, 0.2)',
                    'rgba(255, 132, 132, 0.2)',
                ],
            borderColor:
                [
                    'rgba(255, 132, 132, 1)',
                    'rgba(255, 132, 132, 1)',
                ],
            borderWidth: 1,
            stack: 'Stack 1',
        },
        ]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true,
                max: 100,
            },
        },
    }
});