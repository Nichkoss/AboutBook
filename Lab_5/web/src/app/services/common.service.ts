import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class CommonService {
  public MY_URL = 'http://localhost:5000/'; 
  public isAuthorized: boolean = false;
  public userData: any;
  constructor() { }

}
