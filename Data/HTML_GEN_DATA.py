# -*- coding: utf-8 -*-
# @Author: Nichsen   https://github.com/Nichsen 
# @Date:   2021-10-07 18:24:20
# @Last Modified by:   Nichsen   https://github.com/Nichsen 
# @Last Modified time: 2021-10-07 18:47:50
HEAD = '''<html>
<head>
  <link rel="stylesheet" href="styles.css">
</head>
    <body>    
       <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.1.6/Chart.bundle.min.js"></script>
<!--<canvas id="myChart" width="400" height="400"></canvas>-->
<h1> COVID-19 Germany </h1>
<div class="chart-container" style="position: center; height:40vh; width:85vw">
    <canvas id="myChart"></canvas>
</div>
<script>
var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: '''

#now labels array

MIDDLE1 =''',
        datasets: [{
            label: 'Active',
            data: '''

# now data 1            

MIDDLE2 = ''',
            backgroundColor: [
                'rgba(0, 255, 0, 0.2)',
            ],
            borderColor: [
                'rgba(0, 255, 0, 1)',
            ],
            borderWidth: 1
        },
        {label: 'Infectedt',
            data: '''

#now data 2

MIDDLE3 = ''',
            backgroundColor: [
                'rgba(255, 0, 10, 0.2)',
            ],
            borderColor: [
                'rgba(255, 0, 10, 1)',
            ],
            borderWidth: 1
        },
        {label: 'Deaths',
            data: '''

#now data 3
END = ''',
            backgroundColor: [
                'rgba(25, 25, 25, 0.9)',
            ],
            borderColor: [
                'rgba(25, 25, 25, 1)',
            ],
            borderWidth: 1
        }
        ]
    },
    options: {
        legend: {
            labels: {
                fontColor: "white",
                fontSize: 20
            }
        },
        scales: {
            yAxes: [
                {gridLines: { zeroLineColor: '#ffffff', color:   '#ffffff'},
                ticks: {fontColor: "white", beginAtZero: true}
            }],
            xAxes: [{gridLines: { zeroLineColor: '#c3c3c3', color:   '#101010'},
                ticks: { fontColor: "white",
                    beginAtZero: true
                }
            }]
        }
    }
});
</script>

</body>
</html>'''