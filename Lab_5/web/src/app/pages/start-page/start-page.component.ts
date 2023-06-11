import { Component, OnInit } from '@angular/core';
import { HttpClient } from "@angular/common/http";
import { CommonService } from '../../services/common.service';
import { FormBuilder, FormControl, FormGroup } from '@angular/forms';

@Component({
  selector: 'app-start-page',
  templateUrl: './start-page.component.html',
  styleUrls: ['./start-page.component.scss']
})
export class StartPageComponent implements OnInit {

  MY_URL = 'http://localhost:5000/';
  request: any;
  isAuthorized: boolean = false;
  enabledForm: any;
  name: string | null = 'Stranger';

  constructor(
    private http: HttpClient,
    private cs: CommonService,
    public fb: FormBuilder
  ) {
  }

  ngOnInit(): void {
    const luckyNumber = this.getLuckyNumber();
    console.log(luckyNumber);
    if (luckyNumber != undefined) {
      this.refreshName();
      this.refreshEditForm();
      this.cs.userData = Number(luckyNumber);
    }
    this.isAuthorized = luckyNumber != undefined;
  }

  public logIn() {
    const username = (<HTMLInputElement>document.getElementById("l-u")).value;
    const password = (<HTMLInputElement>document.getElementById("l-p")).value;
    return this.http.get(`${this.MY_URL}user/login?username=${username}&password=${password}`).subscribe({
      next: (res) => { this.giveAccess(username, res['res']) },
      error: e => { alert(e?.error) }
    });
  }

  public signIn() {
    if ((<HTMLInputElement>document.getElementById("policy")).checked) {
      let data: { username: string, password: string, email: string } = {
        username: (<HTMLInputElement>document.getElementById("s-u")).value,
        password: (<HTMLInputElement>document.getElementById("s-p")).value,
        email: (<HTMLInputElement>document.getElementById("s-e")).value,
      }
      return this.http.post(`${this.MY_URL}user`, JSON.stringify(data)).subscribe({
        next: (res) => { this.giveAccess(data.username, res['id']) },
        error: e => { alert(e?.error) }
      });
    } else {
      alert('Sorry, can\'t let u be registered if u not accepting our rules');
      return;
    }
  }

  public refreshName() {
    this.name = localStorage.getItem('name');
  }

  public giveAccess(name, id?) {
    if (id != undefined) {
      this.cs.userData = Number(id)
      this.setLuckyNumber(Number(id));
    };
    this.isAuthorized = true;
    this.refreshEditForm();
    this.cs.isAuthorized = true;
    localStorage.setItem('name', name);
    this.refreshName();
  }

  public refreshEditForm() {
    this.enabledForm = new FormGroup({
      pUsername: new FormControl(''),
      pPassword: new FormControl(''),
      pPassword2: new FormControl(''),
      pPhone: new FormControl(''),
    });
  }

  public editProfile() {
    let data: { username?: string, password?: string, phone?: string } = {};
    let name: string;
    for (let prop in this.enabledForm.value) {
      if (this.enabledForm.value[prop] != '' && prop != 'pPassword2') {
        name = prop;
        name = name.slice(1, name.length);
        data[name.toLowerCase()] = this.enabledForm.value[prop];
      }
    }

    if (data.hasOwnProperty('password')) {
      if (data.password === this.enabledForm.value.pPassword2) {
        this.http.put(`${this.MY_URL}user/${this.cs.userData}`, JSON.stringify(data)).subscribe({
          next: (res) => { this.giveAccess(data.username); this.refreshName() },
          error: e => { alert(e?.error) }
        });
      } else {
        alert('Ur passwords don\'t match. Try again')
        return;
      }
    } else {
      this.http.put(`${this.MY_URL}user/${Number(this.cs.userData)}`, JSON.stringify(data)).subscribe({
        next: (res) => { this.giveAccess(data.username, res['user'].id); this.refreshName(); },
        error: e => { alert(e?.error) }
      });
    }
  }

  public setLuckyNumber(id = this.cs.userData) {
    localStorage.setItem('luckyNumber', id);
  }

  public getLuckyNumber() {
    return localStorage.getItem('luckyNumber');
  }

  public logOut() {
    localStorage.removeItem('luckyNumber');
    history.back();
  }
}
