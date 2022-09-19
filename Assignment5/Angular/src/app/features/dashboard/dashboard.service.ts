import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable, tap } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AnalyticsService {
  private _data: BehaviorSubject<any> = new BehaviorSubject(null);

  /**
   * Constructor
   */
  constructor(private _httpClient: HttpClient) {}

  // -----------------------------------------------------------------------------------------------------
  // @ Accessors
  // -----------------------------------------------------------------------------------------------------

  /**
   * Getter for data
   */
  get data$(): Observable<any> {
    return this._data.asObservable();
  }

  // -----------------------------------------------------------------------------------------------------
  // @ Public methods
  // -----------------------------------------------------------------------------------------------------

  /**
   * Get data
   */
  getData(): Observable<any> {
    return this._httpClient
      .get('https://fakerapi.it/api/v1/persons?_locale=fr_FR')
      // .get('http://127.0.0.1:5000/qcount_plot')
      .pipe(
        tap((response: any) => {
          this._data.next(response);
        })
      );
  }
  getqcount(): Observable<any>{
    return this._httpClient
      // .get('https://fakerapi.it/api/v1/persons?_locale=fr_FR')
      .get('http://127.0.0.1:5000/qcount_plot');
     
  }
  getsscatter(): Observable<any>{
    return this._httpClient
      // .get('https://fakerapi.it/api/v1/persons?_locale=fr_FR')
      .get('http://127.0.0.1:5000/s_scatter_plot');
     
  }
  getlabelcount(): Observable<any>{
    return this._httpClient
      // .get('https://fakerapi.it/api/v1/persons?_locale=fr_FR')
      .get('http://127.0.0.1:5000/label_count');
     
  }
  getdscatter(): Observable<any>{
    return this._httpClient
      // .get('https://fakerapi.it/api/v1/persons?_locale=fr_FR')
      .get('http://127.0.0.1:5000/densityPh_scatter_plot');
     
  }
}
