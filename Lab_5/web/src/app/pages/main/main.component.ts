import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { CommonService } from '../../services/common.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit {
  books: any;
  public snowfall:number[] = [];
  constructor(
    private http: HttpClient,
    private router: Router,
    public storage: CommonService,
  ) {
    this.http.get(`${this.storage.MY_URL}products`).subscribe({
      next: (data: any) => {
        console.log(data.items);
        for (let i = 0; i < 52; i++) {
          data.items.push(data.items[this.random(0,4)])
        }
        data.items.push(data.items[this.random(0, 4)])
        data.items.forEach(i => i.filtered = true);
        this.books = data.items;
        console.log(this.books)
      },
      error: e => alert(e)
    });
  }

  ngOnInit(): void {
    this.snowfall = [];
    for(let x = 159; x > 0; x--){
      this.snowfall.push(0);
    }
  }

  public random(min: number, max: number) {
    return Math.floor(Math.random() * (max - min + 1) + min)
  }

  public navToBook(item){
    this.router.navigateByUrl(`books/${item.id}`);
  }
}
