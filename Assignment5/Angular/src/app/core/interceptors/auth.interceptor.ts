import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { Injectable } from '@angular/core';
import { HttpInterceptor, HttpErrorResponse } from '@angular/common/http';
import { HttpRequest } from '@angular/common/http';
import { HttpHandler } from '@angular/common/http';
import { HttpEvent } from '@angular/common/http';
import { tap } from 'rxjs/operators';

import { AuthenticationService } from '../services/auth/auth.service';
import { MatDialog } from '@angular/material/dialog';


@Injectable( {providedIn: 'root'})
// @Injectable()
export class AuthInterceptor implements HttpInterceptor {
  constructor(
    private authService: AuthenticationService,
    private router: Router,
    private dialog: MatDialog
  ) {}

  intercept(
    req: HttpRequest<any>,
    next: HttpHandler
  ): Observable<HttpEvent<any>> {
    const user = this.authService.getCurrentUser();
    

    // if (user && user.token) {
    //   const cloned = req.clone({
    //     headers: req.headers.set('Authorization', 'Bearer ' + user.token),
    // //   });
    if (user.token) {
      let access_token:string=user.token
      console.log(typeof(user.token))
      const cloned = req.clone({
        headers: req.headers.set('Authorization', 'JWT ' + access_token),
        
        // headers: req.headers.set('Authorization', `JWT ${user.token}` ),
      });
      console.log(cloned)
      console.log(user.token)

      return next.handle(cloned).pipe(
        tap(
          () => {console.log(cloned)},
          (err: any) => {
            if (err instanceof HttpErrorResponse) {
              if (err.status === 401) {
                // console.log("inside dailog box")
                this.dialog.closeAll();
                this.router.navigate(['/auth/signin']);
              }
            }
          }
        )
      );
    } else {
      return next.handle(req);
    }
  }
}
