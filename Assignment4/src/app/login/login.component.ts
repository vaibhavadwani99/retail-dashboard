import { Component, OnInit } from '@angular/core';

import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
// import { HttpHeaders } from '@angular/common/http'


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  access_token: string = "";
  feedback: string = "invalid credentials";
  permission = false;


  constructor(private http: HttpClient, private router: Router) { }

  ngOnInit(): void {
  }
  onLogin(data: { username: string, password: string }) {
    console.log(data)
    if (data.username === "vaibhav" && data.password === "abc") {
      this.http
        .post<{ access_token: string }>("http://127.0.0.1:5000/auth", data)
        .subscribe(responseData => {
          // console.log(responseData)
          this.access_token = responseData.access_token
          // console.log(this.access_token)
          this.router.navigate(["/dashboard"])

        })
      // console.log(this.access_token)

    }
    else {
      this.permission = true

    }
  }

}


