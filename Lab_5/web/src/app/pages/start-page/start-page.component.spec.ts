import { HttpClient } from '@angular/common/http';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { FormBuilder } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { of } from 'rxjs';
import { CommonService } from '../../services/common.service';

import { StartPageComponent } from './start-page.component';

describe('StartPageComponent', () => {
  let component: StartPageComponent;
  let fixture: ComponentFixture<StartPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ StartPageComponent ],
      providers: [
        {provide: FormBuilder},
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
          provide: ActivatedRoute, useValue: {
            snapshot: {
              paramMap: {
                get(val) { return val }
              }
            }
          }
        },
      ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(StartPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should return null as luckyNumber', () => {
    localStorage.removeItem('luckyNumber');
    let mock = component.getLuckyNumber();
    expect(mock).toBe(null);
  });

  it('should set Lucky Number to localStorage', () => {
    let mock = 1
    component.setLuckyNumber(mock);
    expect(localStorage.getItem('luckyNumber')).toBe(String(mock));
  });

  it('should edit profile', () => {
    component.giveAccess('Summer', 1);
    spyOn(window, "alert");
    component.enabledForm.value = {
      pUsername: 'Test',
      pPassword: '1234',
      pPassword2: '1284',
    }
    component.editProfile();
    expect(window.alert).toHaveBeenCalledWith("Ur passwords don\'t match. Try again");
  });

  it('should set the level of access', () => {
    let mySpy = spyOn(component, 'setLuckyNumber');
    let mySpy2 = spyOn(component, 'refreshEditForm');
    let mySpy3 = spyOn(component, 'refreshName');

    component.giveAccess('Summer', 1);

    expect(mySpy).toHaveBeenCalled();
    expect(component.isAuthorized).toBe(true);
    expect(mySpy2).toHaveBeenCalled();
    expect(mySpy3).toHaveBeenCalled();
  });
});
