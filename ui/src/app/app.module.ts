import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MaterialModule } from './shared/material/material.module';
import { UserModule } from './user/user.module';

import { HTTP_INTERCEPTORS } from '@angular/common/http';
import { TokenInterceptor } from './shared/token.interceptor';

import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { TasksComponent } from './svc/tasks/tasks.component';
import { HttpClientModule } from '@angular/common/http';
import { FlexLayoutModule } from '@angular/flex-layout';
import { CreateComponentDialog } from './task/create/create.component';


@NgModule({
  declarations: [
    AppComponent,
    DashboardComponent,
    TasksComponent,
    CreateComponentDialog
  ],
  imports: [
    UserModule,
    BrowserModule,
    MaterialModule,
    AppRoutingModule,
    HttpClientModule,
    FlexLayoutModule,
    BrowserAnimationsModule,
  ],
  providers: [{
    provide: HTTP_INTERCEPTORS,
    useClass: TokenInterceptor,
    multi: true
  }],
  bootstrap: [AppComponent]
})
export class AppModule { }
