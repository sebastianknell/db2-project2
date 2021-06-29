import { Component } from '@angular/core';
import { New } from './new';
import { NewsService } from './news.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'ang-material';
  query = "";
  news: New[] = [];

  constructor(private newsService: NewsService) {}

  sendQuery() {
    this.newsService.postQuery(this.query).subscribe(data => {
      console.log(data);
      this.news.push(data);
    })
  }
}
