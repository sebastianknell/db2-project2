import { Component, Input, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { New } from '../new';
import { NewsService } from '../news.service';


@Component({
  selector: 'app-news-preview',
  templateUrl: './news-preview.component.html',
  styleUrls: ['./news-preview.component.css']
})
export class NewsPreviewComponent implements OnInit {
  @Input()
  data!: New

  constructor() {
  }

  ngOnInit(): void {
  }

}
