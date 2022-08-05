import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http'
import { get } from "./get.model"
// import { LoginComponent } from '../login/login.component';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  access_token: string = "";

  total_sales = 0;
  average_sales = 0;
  unique_visitors = 0
  daily_sales: get[] = []
  data = { username: "vaibhav", password: "abc" }




  constructor(private http: HttpClient) {


  }



  ngOnInit() {
    this.http
      .post<{ access_token: string }>("http://127.0.0.1:5000/auth", this.data)
      .subscribe(responseData => {

        this.access_token = responseData.access_token
        this.login(this.access_token)
      })





  }

  login(token: string) {
    const headers = new HttpHeaders()
      .set('Authorization', 'JWT ' + token)


    this.http.get<{ ["total sales"]: number }>("http://127.0.0.1:5000/total_sales/21-02-2022", { headers: headers })
      .subscribe(responseData => {
        this.total_sales = responseData["total sales"]
        console.log(this.total_sales)
        console.log(responseData)
      }
      )
    // console.log(this.total_sales)

    this.http.get<{ ["average sales per customer"]: number }>("http://127.0.0.1:5000/average_sales/21-02-2022", { headers: headers })
      .subscribe(responseData => {
        this.average_sales = responseData['average sales per customer']
        console.log(this.average_sales)
        console.log(responseData)
      })

    this.http.get<{ unique_visitors: number }>("http://127.0.0.1:5000/unique_visitors/21-02-2022", { headers: headers })
      .subscribe(responseData => {
        this.unique_visitors = responseData.unique_visitors;
        console.log(this.unique_visitors)
        console.log(responseData)
      })

    this.http.get<{ [items: string]: [get] }>("http://127.0.0.1:5000/sales", { headers: headers })
      .subscribe(responseData => {

        console.log(responseData)
        this.daily_sales = responseData["items"];
        console.log(this.daily_sales)

      })




  }









}
