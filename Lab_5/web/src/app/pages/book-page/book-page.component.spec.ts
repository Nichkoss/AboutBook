import { HttpClient } from '@angular/common/http';
import { ComponentFixture, TestBed } from '@angular/core/testing';
import { DomSanitizer } from '@angular/platform-browser';
import { ActivatedRoute } from '@angular/router';
import { of } from 'rxjs';
import { CommonService } from '../../services/common.service';

import { BookPageComponent } from './book-page.component';

describe('BookPageComponent', () => {
  let component: BookPageComponent;
  let fixture: ComponentFixture<BookPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [BookPageComponent],
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
          provide: ActivatedRoute, useValue: {
            snapshot: {
              paramMap: {
                get(val) { return val }
              }
            }
          }
        },
        { provide: DomSanitizer },
      ]
    })
      .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(BookPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
