import { Component, OnInit } from '@angular/core';
import { EChartsOption } from 'echarts';
import { AnalyticsService } from 'src/app/features/dashboard/dashboard.service';

@Component({
  selector: 'app-area-chart-animated',
  templateUrl: './area-chart-animated.component.html',
  styleUrls: ['./area-chart-animated.component.scss'],
})
export class AreaChartAnimatedComponent implements OnInit {
  _chartOption: EChartsOption = {};

  constructor(private dashboard:AnalyticsService) {}

  ngOnInit() {
    this.dashboard.getsscatter().subscribe(responseData=>{
      this.loadChart(responseData)

    })


    
  }

  private loadChart(data:any): void {
    const xAxisData = [];
    const data1 = data["sulphur"]
    // const data2 = [];

    // for (let i = 0; i < 100; i++) {
    //   xAxisData.push('category' + i);
    //   data1.push((Math.sin(i / 5) * (i / 5 - 10) + i / 6) * 5);
    //   data2.push((Math.cos(i / 5) * (i / 5 - 10) + i / 6) * 5);
    // }

    this._chartOption = {
      legend: {
        data: ["Sulphur Scatter plot"],
        align: 'left',
      },
      tooltip: {},
      xAxis: {
        // data: xAxisData,
        silent: false,
        name:"free sulphur dioxide",
        nameLocation:"middle",
        nameGap:50,
        splitLine: {
          show: false,
          

        },
      },
      yAxis: {name:"total sulphur dioxide",
      nameLocation:"middle",
      nameGap:50,},
      series: [
        {
          symbolSize:3,
          name: 'scatter',
          type: 'scatter',
          data: data1,
          animationDelay: (idx: number) => idx * 2,
        },
        // {
        //   name: 'bar2',
        //   type: 'bar',
        //   data: data2,
        //   animationDelay: (idx: number) => idx * 10 + 100,
        // },
      ],
      animationEasing: 'elasticOut',
      animationDelayUpdate: (idx: number) => idx * 2,
    };
  }
}
