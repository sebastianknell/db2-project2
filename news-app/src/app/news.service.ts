import { Injectable } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { Observable } from 'rxjs';
import { New } from './new';

@Injectable({
  providedIn: 'root'
})
export class NewsService {
  private newsApi = "http://127.0.0.1:5000/search"

  constructor(private http: HttpClient) { }

  postQuery(query: string): Observable<New> {
    return this.http.post<New>(this.newsApi, {query: query})
  }
}
