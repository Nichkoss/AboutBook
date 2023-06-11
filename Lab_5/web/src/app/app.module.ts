import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { RouterModule } from "@angular/router";
import { AppComponent } from './app.component';
import { HttpClientModule } from "@angular/common/http";
import { CoverComponent } from './components/cover/cover.component';
import { ChapterComponent } from './components/chapter/chapter.component';
import { MainComponent } from './pages/main/main.component';
import { StartPageComponent } from './pages/start-page/start-page.component';
import { DemoComponent } from './pages/demo/demo.component';
import { BookPageComponent } from './pages/book-page/book-page.component';
import { NavMenuComponent } from './components/nav-menu/nav-menu.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    CoverComponent,
    ChapterComponent,
    MainComponent,
    StartPageComponent,
    DemoComponent,
    BookPageComponent,
    NavMenuComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule,
    HttpClientModule,
    FormsModule, ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
