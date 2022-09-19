import { HttpClient } from '@angular/common/http';
import { Component, Input, OnInit } from '@angular/core';
import { EChartsOption } from 'echarts';
import { AnalyticsService } from 'src/app/features/dashboard/dashboard.service';
import { LabelBarChartComponent } from '../bar-chart-label/bar-chart-label.component';

@Component({
  selector: 'app-scatter-chart',
  templateUrl: './scatter-chart.component.html',
  styleUrls: ['./scatter-chart.component.scss'],
})
export class ScatterChartComponent implements OnInit {
  @Input() chartUrl = '';
  _chartOption: EChartsOption = {};
  private showLegend: boolean = true;

  constructor(private http:HttpClient,private dashboard:AnalyticsService) {}

  ngOnInit() {
    this.dashboard.getsscatter().subscribe((responseData:any)=>{
      this.loadChart(responseData.sulphur)
    })
    // this.http.get<{data:number[]}>("http://127.0.0.1:5000/qcount_plot").subscribe(responseData=>{
    //   console.log(responseData.data)
    //   if(responseData.data!==null){
    //     console.log("inside if")
    //     this.loadChart(responseData.data)
    //   }
    // })
    // let data = [820, 932, 901, 934, 1290, 1330, 1320];
    // if (this.chartUrl === 'first') {
    //   data = [820, 932, 901, 934, 990, 930, 920];
    //   this.showLegend = false;
    // }
    // if (this.chartUrl === 'second') {
    //   data = [20, 32, 41, 34, 50, 30, 20];
    //   this.showLegend = false;
    // }
    // if (this.chartUrl === 'third') {
    //   data = [1820, 1932, 1901, 1934, 1990, 1930, 1920];
    //   this.showLegend = false;
    // }
    // console.log(this.chartUrl, this.showLegend);
    // this.loadChart(data);
  }

  private loadChart(data: any): void {
    console.log(data)
    this._chartOption = {
        xAxis: {},
        yAxis: {},
        series: [
          {
            symbolSize: 10,
            data: data,
            type: 'scatter',
            color:"yellow"
            
            
          }
        ]
      };
  }
}