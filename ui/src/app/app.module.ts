import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MaterialModule } from './shared/material/material.module';
import { ClientModule } from './client/client.module';

import { DashboardComponent } from './pages/dashboard/dashboard.component';
import { TasksComponent } from './svc/tasks/tasks.component';

@NgModule({
  declarations: [
    AppComponent,
    DashboardComponent,
    TasksComponent
  ],
  imports: [
    ClientModule,
    BrowserModule,
    MaterialModule,
    AppRoutingModule,
    BrowserAnimationsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
