option = {
  	color: ['#3e6591', '#eb7d22', '#d73f45', '#d73f45', '#d73f45'],
  	grid: {
      	left: 250
    },
    xAxis: {
      	axisLine: {
          	lineStyle: {color: '#ccc'}
        },
      	axisLabel: {
          	textStyle: {color: '#777'}
        }
    },
    yAxis: [{
      	inverse: true,
      	splitLine: {
          	show: true
        },
      	axisTick: {
          	length: 100,
          	lineStyle: {color: '#ccc'}          
        },
      	axisLine: {
          	lineStyle: {color: '#ccc'}
        },
        data: ['-', '-', '-', '-', '-', '-']      
    }, {
      	name: '                     ',
      	nameLocation: 'start',      
      	nameTextStyle: {
          	fontWeight: 'bold'
        },
	    position: 'left',
      	offset: 130,
      	axisLine: {
          	onZero: false,
          	show: false          
        },
      	axisTick: {
          	length: 70,
          	inside: true,
          	lineStyle: {color: '#ccc'}
        },      
      	axisLabel: {
          	inside: true
        },      
      	inverse: true,      
      	data: ['', '', '', '', '', '']
    }, {
      	name: '                算法指标',
      	nameLocation: 'start',
      	nameTextStyle: {
          	fontWeight: 'bold'
        },      
		position: 'left',
      	offset: 220,
      	axisLine: {
          	onZero: false,
          	show: false
        },
      	axisTick: {
          	length: 100,
          	inside: true,
          	lineStyle: {color: '#ccc'}          
        },
      	axisLabel: {
          	inside: true
        },
      	inverse: true,
      	data: ['F1core', 'Precision', 'Accuracy', 'Recall', 'MAE', 'RMSE']      
    }],
    series: [{
        type: 'bar',
        data:[220, 182, 191, 234, 290, 300],
        label: {
         	normal: {
              	show: true,
              	position: 'left',
              	textStyle: {color: '#000'},
              	formatter: 'RNN',              
            }
        }
    }, {
        type: 'bar',
        data:[210, 132, 91, 204, 220, 300],
        label: {
         	normal: {
              	show: true,
              	position: 'left',
              	textStyle: {color: '#000'},
              	formatter: 'WindowGRU',              
            }
        }      
    }, {
        type: 'bar',
        data:[120, 132, 131, 254, 278, 300],
        label: {
         	normal: {
              	show: true,
              	position: 'left',
              	textStyle: {color: '#000'},
              	formatter: 'DAE',              
            }
        }      
    },{
        type: 'bar',
        data:[210, 132, 91, 204, 220, 300],
        label: {
         	normal: {
              	show: true,
              	position: 'left',
              	textStyle: {color: '#000'},
              	formatter: 'Seq2Seq',              
            }
        }      
    },{
        type: 'bar',
        data:[210, 132, 91, 204, 220, 300],
        label: {
         	normal: {
              	show: true,
              	position: 'left',
              	textStyle: {color: '#000'},
              	formatter: 'Seq2Point',              
            }
        }      
    },{      
        type: 'bar',
        data:['-', '-', '-', '-', '-', '-'],
      	yAxisIndex: 1
    }, {
        type: 'bar',
        data:['-', '-', '-', '-', '-', '-'],
      	yAxisIndex: 2
    }]
};
