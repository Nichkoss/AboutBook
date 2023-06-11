import { HttpClient } from '@angular/common/http';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { Router } from '@angular/router';
import { of } from 'rxjs';
import { CommonService } from '../../services/common.service';

import { MainComponent } from './main.component';

describe('MainComponent', () => {
  let component: MainComponent;
  let fixture: ComponentFixture<MainComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MainComponent ],
      providers: [
        {
          provide: HttpClient, useValue: {
            get() {
              return of({})
            },
            post() {
              return of({})
            },
          }
        },
        {
          provide: CommonService, useValue: {
            MY_URL: 'http://localhost:5000/'
          }
        },
        {
          provide: Router, useValue: {
            navigateByUrl(){}
          }
        },
      ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MainComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should return random number between given values', () => {
    let mock = component.random(12, 15)
    expect(mock).toBeLessThanOrEqual(15);
    expect(mock).toBeGreaterThanOrEqual(12);
  });
});
