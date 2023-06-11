import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { CommonService } from '../../services/common.service';
import { DomSanitizer } from '@angular/platform-browser'


@Component({
  selector: 'app-book-page',
  templateUrl: './book-page.component.html',
  styleUrls: ['./book-page.component.scss']
})
export class BookPageComponent implements OnInit {
  private id;
  public item;
  public imageUrl: string = '';
  public hovered: boolean = false;
  image: any;
  MY_URL = 'http://localhost:5000/';

  constructor(
    private http: HttpClient,
    public storage: CommonService,
    private route: ActivatedRoute,
    private sanitizer: DomSanitizer,
  ) {

  }

  ngOnInit(): void {
    this.id = Number(this.route.snapshot.paramMap.get('id'));

    this.http.get(`${this.storage.MY_URL}product/${this.id}`).subscribe({
      next: (data: any) => {
        console.log(data.item);
        this.item = data.item;
        this.imageUrl = 'url(../../../assets/covers/' + this.item.img;
        this.image = this.sanitizer.bypassSecurityTrustStyle(this.imageUrl);
      },
      error: e => alert(e)
    });
  }

  public toggle() {
    this.hovered = !this.hovered;
  }

  public buy(id) {
    if (Number(localStorage.getItem('luckyNumber')) === 0) {
      alert('Please, register if u want to make order!')
      return;
    }
    let quantity = prompt('Number of items u want to order?');
    if (Number(quantity) < 0) {
      alert('Nice try)))');
      return;
    }
    if (Number(quantity) > this.item.quantity) {
      alert('We don\'t have so many items(((');
      return;
    }
    let comment = prompt('Any notes for us?');
    let data = {
      quantity: quantity,
      status: comment,
      userId: Number(localStorage.getItem('luckyNumber')),
      productId: id,
    }
    return this.http.post(`${this.MY_URL}/store/order`, JSON.stringify(data)).subscribe({
      next: (res) => { alert(res['res']); window.location.reload() },
      error: e => { alert(e?.error) }
    });
  }
}
